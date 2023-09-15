from flask import Flask, jsonify, request
import time
from datetime import datetime


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def apiroute():
    current_time_utc = datetime.utcnow()
    current_day = current_time_utc.strftime('%A')
    current_time = current_time_utc.strftime('%H:%M:%S')
      
    if request.method == 'GET':
          
          data = {
               'full_name': 'Owoyemi Idris  Olamilekan',
                'age': 22,
                'slack_name': '0x3Devoid',
                'current_day': current_day,
                "utc_time": current_time,
                'track': 'backend',
                'github_repo_url': 'https://github.com/Halfboyfriend',
                'contact': '08170585143',
                'status': 'serving punishment',
                'status_code': 200 }
    return jsonify(data)

@app.route('/calculate', methods=['POST'])
def calculate():
     if not request.json:
          return jsonify({'error': 'invalid input'}), 400
     input_data = request.json.get('data')
     if not isinstance(input_data, int):
          return jsonify({'error': 'Input is not an integer'}), 400

     result = input_data * 2
     return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)