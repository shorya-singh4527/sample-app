from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>Hello World ! Good Morning !</title></head>
        <body style="background-color: pink; color: white; text-align: center; padding-top: 200px;">
            <h1>Hello World</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
