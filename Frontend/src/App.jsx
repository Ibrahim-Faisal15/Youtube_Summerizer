import React, { useState } from "react";

function App() {
  let [inputData, setInputData] = useState("");
  let [ResponseData, setResponseData] = useState([]);

  let fetching = (win) => {
    win.preventDefault();


    fetch("http://127.0.0.1:3000/genSummary", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(inputData),
    })
      .then((repsonse) => {
        if (!repsonse.ok) {
          throw new Error("There was a network issue, please try again")
        }
        return repsonse.json()
      })
      .then(
        (jsonResponse) => {
          let array = jsonResponse.split('##')

          setResponseData(array)
          console.log(ResponseData)


        }
      )
      .catch(error => {
        console.error('Error:', error);
      });
  }

  return (
    <>
      <form onSubmit={fetching}>
        <input
          type="text"
          placeholder="Enter Youtube Video Link"
          value={inputData}
          onChange={(e) => {
            setInputData(e.target.value);
          }}
        />
        <button>Submit</button>
      </form>

      <div className="response">
        {ResponseData.map((item, index) => (
          <div key={index}>{item}</div>
        ))}
      </div>
    </>
  );
}

export default App;
