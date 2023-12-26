import React from 'react';

class QueryComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      query: this.props.query
    };
  }

  handleInputChange = (event) => {
    this.setState({ query: event.target.value });
    this.props.onQueryChange(event);
  }

  handleFormSubmit = (event) => {
    event.preventDefault();
    this.props.onQuerySubmit();
  }

  render() {
    return (
      <div className="QueryComponent">
        <form onSubmit={this.handleFormSubmit}>
          <label>
            Enter your query:
            <input type="text" value={this.state.query} onChange={this.handleInputChange} />
          </label>
          <input type="submit" value="Submit" />
        </form>
      </div>
    );
  }
}

export default QueryComponent;
