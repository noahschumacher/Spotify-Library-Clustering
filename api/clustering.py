'''
File clustering a users songs using sSpotify features

Need:
	- Pickled dictionary of library.
	- Pickled dictionnary of song features.

Saves:
	- Pickled list of playlists:
		- Each list contains song_ids
'''

import numpy as np
import pandas as pd

from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


def standardize(df):
    cols = df.columns
    for col in cols:
        mean = df[col].mean()
        std = df[col].std()
        
        df[col] = (df[col] - mean) / std
        
    return df


## Finds the silhouette_score
def sil_scores(data, k):
    scores = []
    for i in range(2, k):
        kmeans = KMeans(n_clusters=i, random_state=0, n_jobs=-1).fit(data)
        scores = silhouette_score(data, kmeans.labels_)
        scores.append(scores)
        
    return scores 



if __name__ == '__main__':

	## Loading in pickled music lib and pickled music lib features
	songs = pickle.load(open('data/noah_mlib.p', 'rb'))
	features = pickle.load(open('data/noah_mlib_features.p', 'rb'))


	## Setting index as song_id, converting duration to seconds, removing useless rows
	feat_df = pd.DataFrame.from_records(features).set_index('id')
	feat_df['duration'] = np.round(feat_df['duration_ms'] / 1000)
	feat_df.drop(['track_href', 'type', 'uri', 'analysis_url', 'duration_ms'], axis=1, inplace=True)

	## Standardize the matrix of features
	feat_df = standardize(feat_df)


	## Setting the feature matrix (numpy 2d)
	X = feat_df.values

	## Pick number of clusters from sil_scores
	s_scores = sil_scores(X)


