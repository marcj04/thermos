from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/index')
@app.route('/')

def index():
    return render_template('index.html', title="TEST", text="This is the text")

if __name__ == '__main__':
    app.run(debug=True)
