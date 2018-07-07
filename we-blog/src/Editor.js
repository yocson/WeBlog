import React from 'react'
import ReactDOM from 'react-dom'

// 引入编辑器以及编辑器样式
import BraftEditor from 'braft-editor'
import 'braft-editor/dist/braft.css'
import './Editor.css'

class Editor extends React.Component {

  render () {

    const editorProps = {
      height: 300,
      contentFormat: 'raw',
      initialContent: '<p>Hello World!</p>',
      onChange: this.handleChange,
      onRawChange: this.handleRawChange,
      controls: []
    }

    return (
      <div className="demo">
        <BraftEditor {...editorProps}/>
      </div>
    )

  }

  handleChange = (content) => {
    console.log(content)
  }

  handleRawChange = (rawContent) => {
    console.log(rawContent)
  }

}

export default Editor;