import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth

spotify_scope = "user-library-read playlist-read-private playlist-read-collaborative"
spotify_username = input("Enter username of your Spotify account: ")
spotify_token = SpotifyOAuth(scope=spotify_scope, username=spotify_username)
spotifyObj = spotipy.Spotify(auth_manager=spotify_token)

names_of_songs = []

#this method prints the user's playlists so the user can see their playlists' names
def get_user_playlists():
    response = spotifyObj.user_playlists(user=spotify_username)
    print("Your playlists")
    print("---------------------------")
    for item in response["items"]:
        print(item["name"])

#gets all the songs from the given playlist and puts them in names_of_songs
def choose_playlist(playlist_name):
    playlist_id = ""
    playlists = spotifyObj.user_playlists(user=spotify_username)
    for item in playlists["items"]:
        if item["name"] == playlist_name:
            playlist_id = item["id"]
        
    response = spotifyObj.user_playlist(user=spotify_username, playlist_id=playlist_id)
    
    for item in response["tracks"]["items"]:
        names_of_songs.append(item["track"]["name"])

get_user_playlists()
playlist_name = input("Enter the name of the playlist you want to transfer: ")
choose_playlist(playlist_name)
print(names_of_songs)
