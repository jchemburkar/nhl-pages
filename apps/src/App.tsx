import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Standings from "./components/standings/Standing"
import Team from "./components/team/Team"

function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<Standings/>} />
          <Route path="/teams/:teamId" element={<Team/>}/>
        </Routes>
      </Router>
    </>
  );
}

export default App;
