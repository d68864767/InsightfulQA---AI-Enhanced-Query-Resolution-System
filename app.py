```python
from flask import Flask, request, jsonify
from openai_interface import OpenAIInterface
from database_manager import DatabaseManager
from analytics import Analytics
from feedback import Feedback

app = Flask(__name__)

# Initialize the classes
openai_interface = OpenAIInterface()
database_manager = DatabaseManager()
analytics = Analytics()
feedback = Feedback()

@app.route('/')
def home():
    return "Welcome to InsightfulQA - AI-Enhanced Query Resolution System"

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    user_query = data.get('query')
    language = data.get('language', 'en')
    
    # Log the query for analytics
    analytics.log_query(user_query, language)
    
    # Get the response from OpenAI
    response = openai_interface.get_response(user_query, language)
    
    return jsonify(response)

@app.route('/feedback', methods=['POST'])
def handle_feedback():
    data = request.get_json()
    feedback_data = data.get('feedback')
    
    # Handle the feedback
    feedback.handle_feedback(feedback_data)
    
    return jsonify({"message": "Feedback received successfully"})

@app.route('/analytics', methods=['GET'])
def get_analytics():
    # Get the analytics data
    analytics_data = analytics.get_analytics()
    
    return jsonify(analytics_data)

if __name__ == "__main__":
    app.run(debug=True)
```
