from flask import Flask, render_template
import requests

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/logs')
def logs():
    return render_template('logs.html')
@app.route('/sources')
def sources():  
    return render_template('sources.html')
@app.route('/colab')
def colab():
    return render_template('colab_files.html')

if __name__ == "__main__":
    app.run(debug=True) 