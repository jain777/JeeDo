import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';



const getCurrentDate = () => {   //arrow function, can use function istead of =>
  const date = new Date();
  return date.toDateString();
}
const greeting = <h1> Welcome to JeeDo:{getCurrentDate()}</h1>
const dt = <h2></h2>



ReactDOM.render(
greeting,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
