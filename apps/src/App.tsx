import React, { useState, useEffect } from "react";
import Standings from "./components/standings/Standing"

function App() {
  return (
    <div className="App">
      <body>{Standings()}</body>
    </div>
  );
}

export default App;
