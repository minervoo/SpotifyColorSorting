# Spotify Playlist by Album Cover Hue
This project allows you to create a new Spotify playlist where your saved songs are sorted by the dominant hue of their album covers. The code extracts album covers from your Spotify library, analyzes the primary color hue of each cover, and then arranges your tracks in the playlist based on this hue order, creating a visually unique musical experience.

### Features
- Retrieves your saved songs from Spotify
- Extracts the album cover images of each song
- Analyzes the dominant hue of each album cover
- Sorts the songs according to their album cover's hue
- Creates a new playlist in your Spotify account with the sorted songs

### How It Works
- Spotify Authentication: the script connects to the Spotify API using OAuth for authentication and retrieves your saved songs
- Album Cover Analysis: the script downloads the album cover for each track, resizes the image, and computes the dominant hue using the colorsys library
- Sorting by Hue: the tracks are sorted by their album cover's hue value to create a visually organized playlist
- Playlist Creation: a new private playlist is created in your Spotify account, and the sorted tracks are added to it

#### Note
Update the credentials (lines 39 and 40 of the code) in the main() function of the script creating a new personal app from https://developer.spotify.com/dashboard:
- client_id="CLIENT_ID"
- client_secret="CLIENT_SECRET"

## Help me make Spotify see this idea be implemented:
## https://community.spotify.com/t5/Live-Ideas/Sorting-songs-by-album-cover-s-colors/idi-p/6897183#M315934
