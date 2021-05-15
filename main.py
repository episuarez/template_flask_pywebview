import threading

import webview
from flask import Flask, render_template, request

app = Flask(__name__);

@app.route("/")
def index():
    return render_template("index.html");

def launch_webserver():
    app.run();

webserver = threading.Thread(target=launch_webserver, daemon=True);
webserver.start();

window = webview.create_window("App", "http://127.0.0.1:5000");
webview.start(window);
