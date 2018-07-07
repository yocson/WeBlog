import React, { Component } from 'react';
import './App.css';
import Editor from './Editor'
import { DatePicker } from 'antd';
import 'antd/dist/antd.css';

class App extends Component {
  render() {
    return (
      <div>
        <h1> WeBlog </h1>
        <Editor />
      </div>
    );
  }
}

export default App;
