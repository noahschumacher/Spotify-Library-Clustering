## File for getting access to user account through API

import os
import sys
import json
import spotipy
import spotipy.util as util
import pickle
import time
import numpy as np

## UserID = 12161016676
#username = sys.argv[1]

username = '12161016676'

## Setting permissions of app
scope = 'user-library-read'

try:
	token = util.prompt_for_user_token(username, scope)
except:
	print("token not granted")
	sys.exit()


## Create spotify object
spotObj = spotipy.Spotify(auth=token)


lib = {}		## Dictionary of users songs
features = []	## list of list of features of each song

## Iterate for # of songs / 50
for i in range(20):
	off = i*50
	results = spotObj.current_user_saved_tracks(limit=50, offset=off)

	temp = {}
	for item in results['items']:
		track = item['track']
		
		temp[track['id']] = {'song_name':track['name'],
					   		'song_id':track['id'],
					   		'artist':track['artists'][0]['name'],
					   		'artist_id':track['artists'][0]['id'],
					   		'explicit':track['explicit'],
					   		'duration':track['duration_ms']}
	print("Completed:", i/22, '%')

	temp_f = spotObj.audio_features(tracks=temp.keys())

	lib.update(temp)
	features.append(temp_f)
	
	time.sleep(.5)

features = np.array(features).reshape(-1)

print(len(lib.keys()) == len(features))


pickle.dump(lib, open('data/noah_mlib.p', 'wb'))
pickle.dump(features, open('data/noah_mlib_features.p', 'wb'))

'''
{
  "href" : "https://api.spotify.com/v1/me/tracks?offset=5&limit=1&market=ES",
  "items" : [ {
	"added_at" : "2019-05-08T19:46:36Z",
	"track" : {
	  "album" : {
		"album_type" : "single",
		"artists" : [ {
		  "external_urls" : {
			"spotify" : "https://open.spotify.com/artist/238y1dKPtMeFEpX3Y6H1Vr"
		  },
		  "href" : "https://api.spotify.com/v1/artists/238y1dKPtMeFEpX3Y6H1Vr",
		  "id" : "238y1dKPtMeFEpX3Y6H1Vr",
		  "name" : "Parra for Cuva",
		  "type" : "artist",
		  "uri" : "spotify:artist:238y1dKPtMeFEpX3Y6H1Vr"
		} ],
		"external_urls" : {
		  "spotify" : "https://open.spotify.com/album/4FYwlG9sg2erQa6W0RCXLY"
		},
		"href" : "https://api.spotify.com/v1/albums/4FYwlG9sg2erQa6W0RCXLY",
		"id" : "4FYwlG9sg2erQa6W0RCXLY",
		"images" : [ {
		  "height" : 640,
		  "url" : "https://i.scdn.co/image/51af8770d34e66df9f9554880d942acf176ace95",
		  "width" : 640
		}, {
		  "height" : 300,
		  "url" : "https://i.scdn.co/image/f7495b1578a985ec84738ccf52e61374bea55cc8",
		  "width" : 300
		}, {
		  "height" : 64,
		  "url" : "https://i.scdn.co/image/16952971536fa862d0c5eeb4530ab0dea192ab4e",
		  "width" : 64
		} ],
		"name" : "Mood in C",
		"release_date" : "2017-02-17",
		"release_date_precision" : "day",
		"total_tracks" : 6,
		"type" : "album",
		"uri" : "spotify:album:4FYwlG9sg2erQa6W0RCXLY"
	  },
	  "artists" : [ {
		"external_urls" : {
		  "spotify" : "https://open.spotify.com/artist/238y1dKPtMeFEpX3Y6H1Vr"
		},
		"href" : "https://api.spotify.com/v1/artists/238y1dKPtMeFEpX3Y6H1Vr",
		"id" : "238y1dKPtMeFEpX3Y6H1Vr",
		"name" : "Parra for Cuva",
		"type" : "artist",
		"uri" : "spotify:artist:238y1dKPtMeFEpX3Y6H1Vr"
	  }, {
		"external_urls" : {
		  "spotify" : "https://open.spotify.com/artist/5Z61G9Y3C3VcEluD1cn6W2"
		},
		"href" : "https://api.spotify.com/v1/artists/5Z61G9Y3C3VcEluD1cn6W2",
		"id" : "5Z61G9Y3C3VcEluD1cn6W2",
		"name" : "Other",
		"type" : "artist",
		"uri" : "spotify:artist:5Z61G9Y3C3VcEluD1cn6W2"
	  } ],
	  "disc_number" : 1,
	  "duration_ms" : 275953,
	  "explicit" : false,
	  "external_ids" : {
		"isrc" : "DEQ121745037"
	  },
	  "external_urls" : {
		"spotify" : "https://open.spotify.com/track/09mGFNjpjCuivm4kFlWX5o"
	  },
	  "href" : "https://api.spotify.com/v1/tracks/09mGFNjpjCuivm4kFlWX5o",
	  "id" : "09mGFNjpjCuivm4kFlWX5o",
	  "is_local" : false,
	  "is_playable" : true,
	  "name" : "Unfinished Colours (feat. Other)",
	  "popularity" : 36,
	  "preview_url" : "https://p.scdn.co/mp3-preview/b1806e88395c934738e6b0ad7123aa1c979f5211?cid=774b29d4f13844c495f206cafdad9c86",
	  "track_number" : 3,
	  "type" : "track",
	  "uri" : "spotify:track:09mGFNjpjCuivm4kFlWX5o"
	}
  } ],
  "limit" : 1,
  "next" : "https://api.spotify.com/v1/me/tracks?offset=6&limit=1&market=ES",
  "offset" : 5,
  "previous" : "https://api.spotify.com/v1/me/tracks?offset=4&limit=1&market=ES",
  "total" : 1286
}'''