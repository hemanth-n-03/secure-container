from flask import Flask

app = Flask(__name__)
AWS_SECRET_ACCESS_KEY="demo_test_secret_123"

@app.route('/')
def home():
    return "Secure Container Pipeline Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)