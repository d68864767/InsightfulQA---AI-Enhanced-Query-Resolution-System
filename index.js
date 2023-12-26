import React from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import QueryComponent from './QueryComponent';
import ResponseComponent from './ResponseComponent';
import FeedbackComponent from './FeedbackComponent';
import AnalyticsComponent from './AnalyticsComponent';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      query: '',
      response: '',
      feedback: '',
      analytics: {}
    };
  }

  handleQueryChange = (event) => {
    this.setState({ query: event.target.value });
  }

  handleQuerySubmit = () => {
    axios.post('/api/query', { query: this.state.query })
      .then(res => {
        this.setState({ response: res.data });
      })
      .catch(err => {
        console.error(err);
      });
  }

  handleFeedbackSubmit = (feedback) => {
    this.setState({ feedback });
    axios.post('/api/feedback', { feedback })
      .then(res => {
        console.log(res.data);
      })
      .catch(err => {
        console.error(err);
      });
  }

  componentDidMount() {
    axios.get('/api/analytics')
      .then(res => {
        this.setState({ analytics: res.data });
      })
      .catch(err => {
        console.error(err);
      });
  }

  render() {
    return (
      <div className="App">
        <QueryComponent 
          query={this.state.query} 
          onQueryChange={this.handleQueryChange} 
          onQuerySubmit={this.handleQuerySubmit} 
        />
        <ResponseComponent response={this.state.response} />
        <FeedbackComponent onFeedbackSubmit={this.handleFeedbackSubmit} />
        <AnalyticsComponent analytics={this.state.analytics} />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById('root'));
