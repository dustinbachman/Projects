import spotipy # Used to access the Spotify API
from spotipy.oauth2 import SpotifyOAuth # Used for Spotify user authentication

# Global Variables
scope = 'playlist-read-private playlist-modify-public'
cid = '39f5821dd2054aab8569027dca377677'
secret = '2677007bd3e0456a98b45d7a98457d17'
redirect_uri = 'http://localhost:8000'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, redirect_uri=redirect_uri, scope=scope))
allPlaylists = []

# Get credenti

# Enter your Spotify username
username = sp.current_user()['id']

# Get tracks of playlist
def getPlaylistTracks(playlist_id):
    tracks = []
    offset = 0
    while True:
        results = sp.playlist_items(playlist_id=playlist_id, offset=offset)
        tracks.extend(results['items'])
        offset += len(results['items'])
        if len(results['items']) == 0:
            break
    track_info = [(track['track']['name'], ', '.join([artist['name'] for artist in track['track']['artists']])) for track in tracks]
    return track_info

# Get every playlist that the user follows
def getAllPlaylists():
    offset = 0
    # Get first results, then start while loop
    while True:
        results = sp.current_user_playlists(offset=offset)
        allPlaylists.extend(results['items'])
        offset += len(results['items'])
        if(len(results['items']) == 0):
            break

# Get only the user owned playlists
def getUserPlaylists():
    getAllPlaylists()
    global userPlaylists
    userPlaylists = [playlist for playlist in allPlaylists if playlist['owner']['id'] == username ]

# Create a playlist on the user's account with the parameter name
def createPlaylist(n):
    sp.user_playlist_create(username, n)
    





# Print the name and track count of each user-created playlist
#print(len(userPlaylists))
#for playlist in userPlaylists:
    #print(getPlaylistTracks(playlist[playlist['id']]))




