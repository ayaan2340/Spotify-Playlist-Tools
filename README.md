# Spotify-Playlist-Tools
Allows users to shuffle and merge their playlists using Python. To use this app yourself, you will need to copy and paste your client IDs and redirect URI.

## Details
* Uses the Spotify API to request User Authetication using OAuth
* Gets user's playlist by batching up to 100 requests to handle rate limiting
* Shuffle and merge algorithms create new playlists by randomizing the order of a playlist or adding the songs between two playlists to one new playlist respectively 
