from flask import Flask, redirect, request, render_template, url_for
import requests


app = Flask(__name__)

user_url = "192.168.1.8:5009/receive"

conv = []
cur_user = None


@app.route('/', methods=["GET"])
def home():
    return render_template("me.html", data=conv)


@app.route('/send', methods=['POST'])
def send():
    msg = request.form.get("message")
    body = {
        "name": cur_user,
        "messge": msg,
    }
    conv.append(body)

    res = requests.post(user_url, body=body, headers={"Content-Type": "application/json"}) 
    print(res)
    return 200




@app.route("/receive", methods=["POST"])
def receive():
    data = request.json
    conv.append(data)

    return redirect(url_for('home'))


if __name__ == '__main__':
    cur_user = input("Enter Name")
    app.run(host='0.0.0.0', port=5009, debug=True)
