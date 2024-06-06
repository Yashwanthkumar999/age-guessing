import requests
from flask import Flask, render_template
AGE_API = "https://api.agify.io?"
GENDER_API = "https://api.genderize.io?"

PARAMS = {
     "name": input("enter your name")
}
result1 = requests.get(AGE_API, params=PARAMS)
result2 = requests.get(GENDER_API, params=PARAMS)
data1 = result1.json()
data2 = result2.json()
age = (data1["age"])
gender = (data2["gender"])
app = Flask(__name__)


@app.route('/')
def greet():
    return render_template("main.html", name=PARAMS["name"], gender=gender, age=age)


if __name__ == "__main__":
    app.run(debug=True)
