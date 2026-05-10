from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():

    return """
    <h1>🚀 Training Trains</h1>

    <h2>Website Working Successfully 😎</h2>

    <p>Internship Portal Live</p>
    """

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=10000)
