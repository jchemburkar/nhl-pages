import { useState, useEffect } from "react";

function App() {
  const [currentPlayer, setCurrentPlayer] = useState("");

  useEffect(() => {
    fetch('/players/8470638').then(res => res.json()).then(data => {
      setCurrentPlayer(data.firstName.concat(' ', data.lastName));
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>The current time is {currentPlayer}.</p>
      </header>
    </div>
  );
}

export default App;
