from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask! 🚀 CI/CD with Docker working pradeep Akila Poelami aadhyanth success!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


