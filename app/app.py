from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "version 2 deployed using Gitops and Argo CD!"

@app.route("/health")
def health():
    return "healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
