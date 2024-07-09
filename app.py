# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
from recommendation_algo import recommend_games
import os

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Get favorite games from request body
        favorite_games = request.json.get('favorite_games', [])

        # Call recommend_games function
        recommendations = recommend_games(favorite_games)

        # Return recommendations as JSON response
        return jsonify(recommendations)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
