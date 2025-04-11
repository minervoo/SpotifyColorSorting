pip install spotipy requests pillow numpy scikit-learn scipy

import spotipy 
from spotipy.oauth2 import SpotifyOAuth
import requests
from io import BytesIO
import colorsys
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
import scipy
import scipy.cluster
import binascii


def get_saved_tracks(sp):
    tracks = []
    results = sp.current_user_saved_tracks()
    while results:
        for item in results['items']:
            track = item['track']
            image_url = track['album']['images'][0]['url'] if track['album']['images'] else None
            tracks.append((track['id'], track['name'], image_url))
        results = sp.next(results) if results['next'] else None
    return tracks

def get_dominant_hue(image_url):

    NUM_CLUSTERS = 5

    response = requests.get(image_url)
    im = Image.open(BytesIO(response.content)).convert('RGB')
    im = im.resize((150, 150))
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(np.prod(shape[:2]), shape[2]).astype(float)

    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)
    num_bins = len(codes)
    counts, bins = np.histogram(vecs, bins=num_bins, range=(0, num_bins))

    index_max = np.argmax(counts)
    peak = codes[index_max]
    colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
    rgb = tuple(int(colour[i:i+2], 16) for i in (0, 2, 4))
    hue = colorsys.rgb_to_hsv(rgb[0], rgb[1], rgb[2])
    
    return hue

def create_ordered_playlist(sp, user_id, tracks):
    playlist = sp.user_playlist_create(user_id, "Sorted by Cover Hue", public=False)
    track_ids = [track[0] for track in tracks]
    chunk_size = 100
    for i in range(0, len(track_ids), chunk_size):
        chunk = track_ids[i:i + chunk_size]
        sp.playlist_add_items(playlist['id'], chunk)
    print("Playlist created successfully!")

def main():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="user-library-read playlist-modify-private"
    ))
    
    user_id = sp.me()['id']
    
    tracks = get_saved_tracks(sp)
    tracks_with_hue = [(t[0], t[1], get_dominant_hue(t[2])) for t in tracks if t[2]]
    tracks_with_hue.sort(key=lambda x: x[2])
    
    create_ordered_playlist(sp, user_id, tracks_with_hue)

if __name__ == "__main__":
    main()
