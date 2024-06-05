import React from "react";
import Navbar from "./Navbar"
import Statistics from "./subpages/Statistics";
import NewCard from "./subpages/NewCard";
import Search from "./subpages/Search";
import './style.css';
import { Route, Routes} from "react-router-dom"

function App() {
  return  (
    <>
      <Navbar />
      <div>
        <Routes>
          <Route path="/statistics" element={<Statistics />}/>
          <Route path="/newCard" element={<NewCard />}/>
          <Route path="/search" element={<Search />}/>
        </Routes>
      </div>
    </>
  )
  

}

export default App;
