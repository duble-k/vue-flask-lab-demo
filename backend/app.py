from flask import Flask, request, jsonify, make_response, send_file, Response
from flask_cors import CORS
from pymongo.mongo_client import MongoClient
import boto3
import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from functions.verify_token import verify_token
import certifi

app = Flask(__name__)
CORS(app, origins=['http://127.0.0.1:3000', 'http://127.0.0.1:4173'], supports_credentials=True)
ca = certifi.where()

# Load environment variables from the .env file
load_dotenv()

# Initialize AWS S3 client
try:
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
        region_name=os.environ.get('AWS_REGION')
    )
    print("Connected to AWS S3")
except Exception as e:
    print(f"Failed to connect to AWS S3. Error: {e}")

# MongoDB connection
try:
    mongo = MongoClient(os.environ.get('CONNECTION_STRING'), tlsCAFile=ca)
    mongo.admin.command('ping')
    print("Connected to MongoDB")
except Exception as e:
    print(f"Failed to connect to MongoDB. Error: {e}")
    mongo = None

# Endpoints go here...

# Authentication endpoint
@app.route('/api/authenticate', methods=['POST'])
def authenticate():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Validate the username and password
    if (
        (username == os.environ.get('BASIC_USER') and password == os.environ.get('BASIC_PASSWORD'))
    ):
        secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')
        token = jwt.encode({'username': username, 'exp': datetime.utcnow() + timedelta(hours=1)}, secret_key, algorithm='HS256')

        response = make_response(jsonify({'message': 'Successful Login'}), 200)
        response.set_cookie('userToken', token, max_age=3600, httponly=True, samesite='None', secure=True)
        response.set_cookie('loggedIn', token, max_age=3600, httponly=False, samesite='None', secure=True)
        return response
    return make_response(jsonify({'message': 'Incorrect Username or Password'}), 401)

# Endpoint to delete a cookie and log a user out
@app.route("/api/delete-cookie", methods=['GET'])
def delete_cookie():
    # Set the cookie's expiration date to a date in the past
    response = make_response(jsonify({'message': 'Cookie deleted successfully'}), 200)
    response.set_cookie('userToken', '', expires=0, httponly=True, samesite='None', secure=True)
    response.set_cookie('loggedIn', '', expires=0, httponly=False, samesite='None', secure=True)
    return response


# Endpoint to get names of demo items with token verification
@app.route("/api/names", methods=['GET'])
@verify_token
def get_names():
    try:
        # Get a list of all names in MongoDB collection
        names = mongo.test.labdatas.distinct('name')
        if names:
            print(names)
            return jsonify(names), 200
        else:
            print("No names found")
            return '', 404
    except Exception as e:
        print("Error: ", e)
        return '', 500

# Endpoint to get demo data with token verification
@app.route("/api/receive", methods=['POST'])
@verify_token
def receive_data():
    try:
        # Get the name from the request body
        name = request.json.get('name')

        # Find data in MongoDB
        lab_data = mongo.test.labdatas.find_one({'name': name})

        if lab_data:
            # Convert ObjectId to string
            lab_data['_id'] = str(lab_data['_id'])
            
            print("Lab info:", lab_data)
            return jsonify(lab_data), 200
        else:
            print("No entries found.")
            return '', 404
    except Exception as e:
        print("Error:", e)
        return '', 400

# Endpoint to get pdfs from s3
@app.route("/api/get-pdf", methods=["POST"])
@verify_token
def get_pdf():    
    # Extract required data from the request body
    pdf_name = request.json.get("pdfName")
    name = request.json.get("name")
    print(name)
    bucket_name = "vikan-lab-data"

    # Configure the parameters for the get_object call
    params = {
        "Bucket": bucket_name,
        "Key": f"{name}/{pdf_name}",  # Specify the S3 object key
    }

    try:
        # Get the PDF object from S3
        response = s3.get_object(**params)

        # Set the response headers to indicate a PDF file
        headers = {
            "Content-Type": "application/pdf",
            "Content-Disposition": f'inline; filename="{pdf_name}"',
        }

        # Send the PDF data as the response
        return Response(response["Body"].read(), headers=headers)
    
    except Exception as e:
        print("Error fetching PDF:", e)
        return Response("Internal server error", status=500)


if __name__ == '__main__':
    app.run(debug=True)