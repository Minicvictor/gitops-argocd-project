from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "GitOps deployment with Argo CD is working!"

@app.route("/health")
def health():
    return "healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
