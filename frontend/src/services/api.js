const API_URL = "http://127.0.0.1:8000"; //fastapi server

export async function sendMessage(sessionId, message) {

    //fetch the response from the server
try{
 
    const response = await fetch(
        `${API_URL}/chat`,
        {
            method: "POST",

            //tell server what type data (json) we are sending
            headers: { "Content-Type": "application/json"},
            //convert to string the message ur sending because in server we expect to receive a strin
            //Class UserRequest(BaseModel), expects a string
            body: JSON.stringify(
                {
                    session_id:sessionId,
                    message:message
                }
            )

        }
    );

    if(!response.ok){
        throw new Error("Failed to communicate with backend");
    }

    //fetch the data which backend sends back, and convert it to json
    const data = await response.json()

    return data
    //now react can access the final response and selected agent


}
catch(error){
    console.error(
        "API ERROR:",
        error
    );
    throw error;
}

}