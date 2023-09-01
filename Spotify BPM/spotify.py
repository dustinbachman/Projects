import config # Used to store keys
import spotipy # Used to access the Spotify API
from spotipy.oauth2 import SpotifyOAuth # Used for Spotify user authentication

# Global Variables
scope = 'user-read-playback-state'
cid = config.clientID
secret = config.secretKey
redirect_uri = 'http://localhost:8000'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, redirect_uri=redirect_uri, scope=scope))
songInfo = []
songs = [songInfo]
# Enter your Spotify username
username = sp.current_user()['id']

# Get currently playing track
def getPlaybackState():
    songInfo.clear()
    result = sp.current_playback()
    songInfo.extend(result['name'])
    songs.extend(songInfo)

getPlaybackState()
