const fetchDeleteCookie = async () => {
    try {
      const response = await fetch(
        'http://127.0.0.1:5000/api/delete-cookie',
        {
          credentials: "include",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      const data = await response.json();
      return data.message;
    } catch (error) {
      console.log("error logging out: ", error)
      throw error; // Re-throw the error to be caught higher up the call stack
    }
  };
  
  export default fetchDeleteCookie;
  