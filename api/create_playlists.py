import sys
import spotipy
import spotipy.util as util
import pickle
import time
import numpy as np

## UserID = 12161016676
#username = sys.argv[1]

username = '12161016676'

## Setting permissions of app
scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)


playlists = [['6hUbZBdGn909BiTsv70HP6','2YQJCYnf4Ab1wS5bA89nHE','1lqIkknUGp0TofqKUhxT4W'],
			 ['6NEIkFHpYkKY1P02ABHOYR','0jvdbjPWrHsNxJMClw61t0','2WLaRlaBmBHL6dqaovdO0m']]

if token:
	sp = spotipy.Spotify(auth=token)
	sp.trace = False

	for i, playlist in enumerate(playlists):

		## Create a playlist
		pname = "Cluster"+str(i)
		r1 = sp.user_playlist_create(username, pname, public=True)
		playlist_id = r1['id']

		print("Created Playlist", playlist_id)


		## Getting list of tracks into correct format
		tracks = ["spotify:track:" + track for track in playlist]

		## Adding tracks in batches of 50
		for i in range(0, len(tracks)//50):

			ts = tracks[i:i+50]
			print(ts)

			sp.user_playlist_add_tracks(username, playlist_id, ts)
			print("Added Tracks")

else:
	print("Can't get token for", username)