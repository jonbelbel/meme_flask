from flask import Flask, render_template
import requests
import json

def get_meme():
    url = "https://meme-api.herokuapp/gimme/wholesomememes"
    reponse = json.loads(requests.requests("GET", url).text)
    meme_large = reponse["preview"][-2]
    subreddit = response["subreddit"]
    return meme_large, subreddit
 
app = Flask(__name__)

@app.route("/")
def index():
    meme_large,subreddit = get_meme()
    return render_template("meme_index.html", meme_large=meme_large, subreddit=subreddit)

app.run(host="0.0.0.0", port=80)