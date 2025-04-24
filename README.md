# Spotify Playlist by Album Cover Hue
This little project lets you create a new Spotify playlist where the songs from any other playlist are sorted by the dominant color of their album covers.
The script pulls album covers with the Spotify API, analyzes the main color of each cover and then arranges the tracks in the playlist based on this color order, giving you a visually unique music experience.

#### NOTE
The code is far from perfect, and any help would not only be welcomed but also greatly appreciated.

### How It Works
- Go to [Spotify for Developers](https://developer.spotify.com/dashboard)
- Create a new app with the Redirect URI "http://127.0.0.1:8888/callback" (the other options are not relevant)
- Download the [SpotifyColorSorting.py file](https://github.com/armeliens/SpotifyColorSorting/blob/main/SpotifyColorSorting.py) (the download button is on the top right of the code)
- Run the script and provide the "CLIENT_ID" and "CLIENT_SECRET" from the new app you just created when asked

### Result
- Playlist created: [link](https://open.spotify.com/playlist/7KcaZp49FUo84UmSiXXsEm?si=bf4aa6cf28064061)
- Time: the code spent about 7min making it

#### Visual result:
![Visual result](https://github.com/armeliens/SpotifyColorSorting/blob/main/Visual%20result.png)

### Methods for sorting to check out
- Most common color (but what if there are 2 colors both dominant but completely different?)
- Average color (but how to find the average of an image that is half blue and half orange?)
- OkLAB / OkLCH
- [TV Ambilight using Arduino](https://www.instructables.com/Make-your-own-TV-ambilight-using-Arduino/)
- [Gamma / sRGB encoding](https://www.gimp-forum.net/Thread-What-is-the-gamma-encoding-and-why-are-my-color-computations-wrong)
- [Color quantization](https://en.wikipedia.org/wiki/Color_quantization)

### To Do List
- Color-themed mini playlists
- Command line tool

## Help me make Spotify see this idea be implemented
#### https://community.spotify.com/t5/Live-Ideas/Sorting-songs-by-album-cover-s-colors/idi-p/6897183#M315934
