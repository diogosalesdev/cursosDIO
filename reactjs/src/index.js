import React from 'react';
import ReactDOM from 'react-dom';
import './styles.css';

function sum(a, b) {
  return a + b  
}

function primeiroJSX() {
  return (
    <div className="teste">
      Deia Ribeiro
      <h1>Soma: {sum(10, 20)}</h1>
    </div>
  )
}

const App = () => {
  return (
    <div className="App">
      {element1}
      {element2}
    </div>
  )
}

const element1 = 'Digital Innovation'
const element2 = <h1>Olá pessoal! ;D</h1>

const rootElement = document.getElementById("root")
ReactDOM.render(<App />, rootElement)