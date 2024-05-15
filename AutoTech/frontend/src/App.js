import React from "react";
import Navbar from "./Navbar"
import Statistics from "./subpages/Statistics";
import NewCard from "./subpages/NewCard";
import Search from "./subpages/Search";

import './style.css';

function App() {
  let Component
  switch(window.location.pathname){
    case "/statistics":
      Component = Statistics;
      break;
    case "/newCard":
      Component = NewCard;
      break;
    case "/search":
      Component = Search;
      break;
  }
  return  (
    <>
      <Navbar />
      <Component />
    </>
  )
  

}

export default App;
