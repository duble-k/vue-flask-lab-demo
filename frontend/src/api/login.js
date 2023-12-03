const login = async (username, password) => {
    try {
      const response = await fetch(
        'http://127.0.0.1:5000/api/authenticate',
        {
          method: "POST",
          credentials: "include",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ username, password }),
        }
      );
      console.log(response);
      return response;
    } catch (error) {
      console.error("Error:", error);
      return null;
    }
  };
  
  export default login;
  