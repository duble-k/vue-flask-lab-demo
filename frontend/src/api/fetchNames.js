const fetchNames = async () => {
    try {
      const response = await fetch(
        'http://127.0.0.1:5000/api/names',
        {
          credentials: "include",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
  
      if (!response.ok) {
        throw new Error("Error fetching country names");
      }
  
      const data = await response.json();
      return data;
    } catch (error) {
      console.error("Error fetching country names:", error);
      throw error; // Re-throw the error to be caught higher up the call stack
    }
  };
  
  export default fetchNames;
  