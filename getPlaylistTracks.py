import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIFY_CLIENT_ID = 'CLIENT ID'
SPOTIFY_CLIENT_SECRET = 'CLIENT SECRET'
SPOTIFY_REDIRECT_URI = 'http://localhost/callback'

auth_manager = SpotifyClientCredentials(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def show_tracks(results, uriArray):
    for i, item in enumerate(results['items']):
        track = item['track']
        uriArray.append(track['id'])
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'], track['name']))

def get_playlist_track_id(username, playlist_id):
    trackID = []
    results = sp.user_playlist(username, playlist_id)
    tracks = results['tracks']
    show_tracks(tracks, trackID)
    while tracks['next']:
            tracks = sp.next(tracks)
            show_tracks(tracks, trackID)
    return trackID

playlists = sp.user_playlists('u0bo3pmy9fw2ifn5e8wsaxdti')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s" % (i + 1 + playlists['offset'],  playlist['name']))
        trackID = get_playlist_track_id('u0bo3pmy9fw2ifn5e8wsaxdti', playlist['id'])
        print(trackID)
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None


