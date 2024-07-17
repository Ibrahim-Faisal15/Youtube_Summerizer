import React, { useState } from "react";

function App() {
  let [inputData, setInputData] = useState("");

  let fetching = async (win) => {
    win.preventDefault();


    let get_link = await fetch(inputData)
    let response = await get_link.response
    console.log(response)

    //   fetch("http://127.0.0.1:3000/genSummary", {
    //     method: "POST",
    //     headers: { "Content-Type": "application/json" },
    //     body: JSON.stringify(inputData),
    //   });
    // };
    // console.log(inputData)
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
    </>
  );
}

export default App;
