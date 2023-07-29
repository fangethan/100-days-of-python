from bs4 import BeautifulSoup
import requests

import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input(
    "Which year do you want to travel to? Type the date in this format YYYY--MM-DD:"
)

URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(URL)
content = response.text

soup = BeautifulSoup(content, "html.parser")
soup_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in soup_names_spans]
print(song_names)

client_id = "82f065b1202148fc883de03e5d2e155b"
client_secret = "b1224c4776864c2581e70814973abe72"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="ethan.fang@gmail.com",
    )
)
user_id = sp.current_user()["id"]

date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False
)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
