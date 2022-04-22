import random
from flask import Flask, render_template
from data import get_data
import os


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')

def hello():

    artists = ["1Cd373x8qzC7SNUg5IToqp", "6s22t5Y3prQHyaHWUN1R1C"]
    rand = random.randint(0, len(artists) - 1)
    data = get_data(artists[rand])

    return render_template(
        'index.html',
        song_name=data[0],
        artist_names=data[1],
        album_cover=data[2],
        preview_url=data[3],
        spotify_url=data[4]
    )


if __name__ == '__main__':
    app.run(
        debug=True,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080))
    )
