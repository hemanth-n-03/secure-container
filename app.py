from flask import Flask

app = Flask(__name__)
AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
github_token = "ghp_123456789012345678901234567890123456"



@app.route('/')
def home():
    return "Secure Container Pipeline Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)