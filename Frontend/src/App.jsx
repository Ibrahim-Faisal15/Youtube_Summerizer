import React, { useState } from "react";

function App() {
  let [inputData, setInputData] = useState("");

  let fetching = (win) => {
    win.preventDefault();
    fetch("http://127.0.0.1:3000/genSummary", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(inputData),
    });
  };
  console.log(inputData);

  return (
    <>
      <form onSubmit={fetching}>
        <input
          type="text"
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
