from flask import Flask
app=Flask(__name__)

@app.route("/")
def home():
    return "hello world, this is jenkins pipeline"

if __name__=="__main__":
    app.run(debug=True)


