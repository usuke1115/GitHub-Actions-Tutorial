from flask import Flask

app=Flask(__name__)

@app.get("/hello")
def hello_world():
    return "<h1>Hello World</h1>"

app.run(host="0.0.0.0", port=8080, debug=True)

