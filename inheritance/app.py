from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!, hy..."

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(debug=True)