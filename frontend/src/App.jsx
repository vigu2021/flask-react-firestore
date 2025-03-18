// App.jsx
import React from 'react';
import RegisterForm from './pages/Register'; // import Hello component
import './App.css';          // keep if you have styling
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';




function App() {
  return (
    <Router>
      <Routes>
        <Route path = "/Register" element = {<RegisterForm />} />
      </Routes>
    </Router>
   
  );
}

export default App;
