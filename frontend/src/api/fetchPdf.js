const fetchPdf = async (name, pdfName) => {
    try {
      const response = await fetch(
        `http://127.0.0.1:5000/api/get-pdf`,
        {
          method: "POST",
          credentials: "include",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ pdfName, name }), // Send the PDF name in the request body
        }
      );
  
      return response;
    } catch (err) {
      console.log(err);
      return { message: "Error occured getting the pdf" };
    }
  };
  
  export default fetchPdf;
  