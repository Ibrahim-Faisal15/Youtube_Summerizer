from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/genSummary', methods=['POST'])
def Index():
  data = request.get_json()
  print(data)
  return "hello"


if __name__ == "__main__":
  app.run(debug=True, port=3000)