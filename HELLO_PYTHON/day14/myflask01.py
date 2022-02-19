from flask import Flask, request, render_template
from flask.json import jsonify

app = Flask(__name__,static_url_path='',static_folder='static')

@app.route('/janggi')
def janggi():
    return render_template('janggi3.html')


if __name__=='__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    