import React from 'react';

class AnalyticsComponent extends React.Component {
  render() {
    const { analytics } = this.props;
    const { total_queries, queries_per_language, total_feedback, feedback_counts } = analytics;

    return (
      <div className="AnalyticsComponent">
        <h2>Analytics</h2>
        <p>Total Queries: {total_queries}</p>
        <h3>Queries per Language:</h3>
        <ul>
          {Object.entries(queries_per_language).map(([language, count]) => (
            <li key={language}>{language}: {count}</li>
          ))}
        </ul>
        <p>Total Feedback: {total_feedback}</p>
        <h3>Feedback Counts:</h3>
        <ul>
          {Object.entries(feedback_counts).map(([feedback, count]) => (
            <li key={feedback}>{feedback}: {count}</li>
          ))}
        </ul>
      </div>
    );
  }
}

export default AnalyticsComponent;
</h3></h3></h2>