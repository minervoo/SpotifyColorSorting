# Spotify Playlist by Album Cover Hue
This project lets you create a new Spotify playlist where the songs from another playlist are sorted by the dominant color of their album covers. The script pulls album covers from your Spotify library, analyzes the main color of each cover, and then arranges the tracks in the playlist based on this color order, giving you a visually unique music experience.

#### NOTE
The code is far from perfect, and any help would not only be welcomed but also greatly appreciated.

### How It Works
- Open "Run" with Windows button + R
- Type "cmd"
- Run this line: pip install spotipy requests colorthief matplotlib numpy
- Go to [Spotify for Developers](https://developer.spotify.com/dashboard)
- Create a new app with the Redirect URI "http://127.0.0.1:8888/callback" (the other options are not relevant)
- Download the [SpotifyColorSorting.py file](https://github.com/armeliens/SpotifyColorSorting/blob/main/SpotifyColorSorting.py) (the download button is on the top right of the code)
- Inside the script, change "CLIENT_ID" and "CLIENT_SECRET" with the ones in the new app you just created
- Change "PLAYLIST_ID" with the one of your selected playlist
- The playlist's ID is the string between 'playlist/' and '?' (for example from https://open.spotify.com/playlist/3gINh3VktzLMNTe9XfqOW5?si=7bbf7c0388354776 the PLAYLIST_ID would be 3gINh3VktzLMNTe9XfqOW5)
- Run the script

### Result
- Playlist created: [link](https://open.spotify.com/playlist/7KcaZp49FUo84UmSiXXsEm?si=bf4aa6cf28064061)
- Time: the code spent about 7min making it

#### Visual result:
![Visual result](https://github.com/armeliens/SpotifyColorSorting/blob/main/Visual%20result.png)

### To Do List
- Color-themed mini playlists
- Command line tool

## Help me make Spotify see this idea be implemented
#### https://community.spotify.com/t5/Live-Ideas/Sorting-songs-by-album-cover-s-colors/idi-p/6897183#M315934
