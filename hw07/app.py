from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about_jh')
def about_jh():
    return render_template('kjh.html')

@app.route('/about_sy')
def about_sy():
    return render_template('isy.html')


app.run(debug=True)