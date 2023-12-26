import React from 'react';

class ResponseComponent extends React.Component {
  render() {
    return (
      <div className="ResponseComponent">
        <h2>Response</h2>
        <p>{this.props.response}</p>
      </div>
    );
  }
}

export default ResponseComponent;
</h2>