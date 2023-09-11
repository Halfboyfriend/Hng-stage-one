from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h2>WELCOME TO 0X3DEVOID API</h2>'



@app.route('/api', methods=['GET', 'POST'])
def apiroute():
      
    if request.method == 'GET':
        name = request.args.get('slack_name')
        day = request.args.get('current_day')
        if name and day:
              data = {
            'slack_name': name,
            'current_day': day,
            'track': 'backend',
            'github_repo': 'https://github.com/Halfboyfriend?tab=repositories',
            'github_file_url': 'https://github.com/Halfboyfriend/Hng-stage-one.git',
            'status_code': 200
            

        }
           
        else:
             data = {'error': 'Please parse in parameters (slack_name and current_day)', 'status_code': 404}

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)