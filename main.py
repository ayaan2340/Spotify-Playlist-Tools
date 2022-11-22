import getPlaylistTracks as gpt
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import random

def main():
    user = input("Enter your Spotify username: ")

    scope = "user-library-read,playlist-modify-public"
    SPOTIFY_CLIENT_ID = 'client id'
    SPOTIFY_CLIENT_SECRET = 'client secret'
    SPOTIFY_REDIRECT_URI = 'redirect uri'


    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=user,scope=scope, client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri=SPOTIFY_REDIRECT_URI))
    playlists = sp.user_playlists(user)
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print("%4d %s" % (i + 1 + playlists['offset'],  playlist['name']))
        if playlists['next']:
            playlists = None
        else:
            playlists = None
    
    shuffle = input("Do you want to shuffle your playlists? (y/n): ")
    if shuffle == "y":
        playlistNumber = int(input("Enter the number of the playlist you want to shuffle: "))
        playlists = sp.user_playlists(user)
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                if i == playlistNumber - 1:
                    trackID = gpt.get_playlist_track_id(user, playlist['id'])
                    random.shuffle(trackID)
                    createdPlaylist = sp.user_playlist_create(user, 'Shuffled Playlist')
                    for j in range(0, len(trackID) - 1, 100):  
                        sp.user_playlist_add_tracks(user, createdPlaylist['id'], trackID[j:j+100])
            if playlists['next']:
                playlists = sp.next(playlists)
            else:
                playlists = None

    merge = input("Do you want to merge your playlists? (y/n): ")
    if merge == "y":
        playlists = sp.user_playlists(user)
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                print("%4d %s" % (i + 1 + playlists['offset'],  playlist['name']))
            if playlists['next']:
                playlists = None
            else:
                playlists = None
        playlistOne = int(input("Enter the number of the first playlist you want to merge: "))
        playlistTwo = int(input("Enter the number of the second playlist you want to merge: "))
        playlists = sp.user_playlists(user)
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                if i == playlistOne - 1:
                    trackID = gpt.get_playlist_track_id(user, playlist['id'])
                if i == playlistTwo - 1:
                    trackID += gpt.get_playlist_track_id(user, playlist['id'])
            if playlists['next']:
                playlists = sp.next(playlists)
            else:
                playlists = None
        createdPlaylist = sp.user_playlist_create(user, 'Merged Playlist')
        for j in range(0, len(trackID) - 1, 100):
            sp.user_playlist_add_tracks(user, createdPlaylist['id'], trackID[j:j+100])

if __name__ == '__main__':
    main()