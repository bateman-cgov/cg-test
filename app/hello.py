import os, json
from flask import Flask

app = Flask(__name__)

app.debug = True

@app.route('/')
def hello():
	env = json.loads(os.getenv('VCAP_SERVICES'))

	return json.dumps(env)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))
