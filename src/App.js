import './App.css';
import React, { useState } from 'react';
import PostForm from './components/PostForm';

function App() {
  const [sentence, setSentence] = useState("");
  return (
    <div className="App">
      <h1> Welcome the the Emotion Detection Model Demonstration</h1>
      <h2>Find out the major emotion in your text! </h2>
      <PostForm />
    </div>
  );
}

export default App;