import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIFY_CLIENT_ID = 'client id'
SPOTIFY_CLIENT_SECRET = 'client secret'
SPOTIFY_REDIRECT_URI = 'redirect uri'

auth_manager = SpotifyClientCredentials(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def show_tracks(results, uriArray):
    for i, item in enumerate(results['items']):
        track = item['track']
        uriArray.append(track['id'])
        # print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))

def get_playlist_track_id(username, playlist_id):
    trackID = []
    results = sp.user_playlist(username, playlist_id)
    tracks = results['tracks']
    show_tracks(tracks, trackID)
    while tracks['next']:
            tracks = sp.next(tracks)
            show_tracks(tracks, trackID)
    return trackID




