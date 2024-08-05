from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/genSummary', methods=['POST'])
def Index():
 
  data = request.get_json()

  try:
    if len(data) == 43:
      parseData = data.split("=")[1]
    elif len(data) == 48:
      parseData = data.split("?")[0].split(".be/")[1]
    else:
      raise TypeError("Please enter an appropriate Youtube link.")
  except TypeError as e:
    return jsonify({
      'error': str(e)}), 400
  except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500 
  
  print(data)
  return jsonify(parseData)


if __name__ == "__main__":
  app.run(debug=True, port=3000)