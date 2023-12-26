import React from 'react';

class FeedbackComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      feedback: ''
    };
  }

  handleFeedbackChange = (event) => {
    this.setState({ feedback: event.target.value });
  }

  handleFeedbackSubmit = (event) => {
    event.preventDefault();
    this.props.onFeedbackSubmit(this.state.feedback);
    this.setState({ feedback: '' });
  }

  render() {
    return (
      <div className="FeedbackComponent">
        <h2>Feedback</h2>
        <form onSubmit={this.handleFeedbackSubmit}>
          <textarea 
            value={this.state.feedback} 
            onChange={this.handleFeedbackChange} 
            placeholder="Enter your feedback here..."
          />
          <button type="submit">Submit Feedback</button>
        </form>
      </div>
    );
  }
}

export default FeedbackComponent;
</h2>