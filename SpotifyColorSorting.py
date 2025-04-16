import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from colorthief import ColorThief
from matplotlib import colors
import numpy as np

CLIENT_ID = 'your_client_ID'
CLIENT_SECRET = 'your_client_secret'
PLAYLIST_ID = 'your_playlist_ID'
REDIRECT_URI = 'http://127.0.0.1:8888/callback'
SCOPE = "playlist-modify-public playlist-modify-private user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

def get_tracks_from_playlist(playlist_id):
    tracks = []
    offset = 0
    while True:
        results = sp.playlist_tracks(playlist_id, offset=offset)
        tracks.extend(results['items'])
        if len(results['items']) < 100:
            break
        offset += 100
    return tracks

def get_dominant_color(image_url):
    response = requests.get(image_url)
    with open('temp_image.jpg', 'wb') as file:
        file.write(response.content)
    
    color_thief = ColorThief('temp_image.jpg')
    dominant_color = color_thief.get_color(quality=1)
    hsl_color = rgb_to_hsl(dominant_color)
    return hsl_color

def rgb_to_hsl(rgb):
    rgb = np.array(rgb) / 255.0
    h, s, v = colors.rgb_to_hsv(rgb)  
    l = (2 - s) * v / 2
    if l != 0:
        s = (2 * (1 - l / v)) * s
    h = h * 360
    s = s * 100
    l = l * 100
    return (h, s, l)

def sort_tracks_by_color(tracks):
    track_colors = []
    for track in tracks:
        album = track['track']['album']
        image_url = album['images'][0]['url']
        dominant_color = get_dominant_color(image_url)
        track_colors.append((track, dominant_color))
    
    sorted_tracks = sorted(track_colors, key=lambda x: x[1][0])
    return [track[0] for track in sorted_tracks]

def create_sorted_playlist(sorted_tracks):
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user_id, 'Playlist Ordered by Color', public=True)
    playlist_id = playlist['id']

    for i in range(0, len(sorted_tracks), 100):
        track_ids = [track['track']['id'] for track in sorted_tracks[i:i+100]]
        sp.playlist_add_items(playlist_id, track_ids)

def main():
    tracks = get_tracks_from_playlist(PLAYLIST_ID)
    sorted_tracks = sort_tracks_by_color(tracks)
    create_sorted_playlist(sorted_tracks)

if __name__ == '__main__':
    main()
