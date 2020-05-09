import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
import json



def albumSongs(uri):
    spotify_albums = {}
    album = uri #assign album uri to a_name
    # print(album)
    spotify_albums[album] = {} #Creates dictionary for that specific album
    #Create keys-values of empty lists inside nested dictionary for album
    spotify_albums[album]['album'] = [] #create empty list
    spotify_albums[album]['track_number'] = []
    spotify_albums[album]['id'] = []
    spotify_albums[album]['name'] = []
    spotify_albums[album]['uri'] = []
    # print(spotify_albums)
    tracks = sp.album_tracks(album) #pull data on album tracks
    for n in range(len(tracks['items'])): #for each song track
        # spotify_albums[album]['album'].append(album_names[album_count]) #append album name tracked via album_count
        spotify_albums[album]['track_number'].append(tracks['items'][n]['track_number'])
        spotify_albums[album]['id'].append(tracks['items'][n]['id'])
        spotify_albums[album]['name'].append(tracks['items'][n]['name'])
        spotify_albums[album]['uri'].append(tracks['items'][n]['uri'])
    return spotify_albums

def audio_features(album):
    #Add new key-values to store audio features
    spotify_albums[album]['acousticness'] = []
    spotify_albums[album]['danceability'] = []
    spotify_albums[album]['energy'] = []
    spotify_albums[album]['instrumentalness'] = []
    spotify_albums[album]['liveness'] = []
    spotify_albums[album]['loudness'] = []
    spotify_albums[album]['speechiness'] = []
    spotify_albums[album]['tempo'] = []
    spotify_albums[album]['valence'] = []
    spotify_albums[album]['popularity'] = []
    #create a track counter
    track_count = 0
    for track in spotify_albums[album]['uri']:
        #pull audio features per track
        features = sp.audio_features(track)
        
        #Append to relevant key-value
        spotify_albums[album]['acousticness'].append(features[0]['acousticness'])
        spotify_albums[album]['danceability'].append(features[0]['danceability'])
        spotify_albums[album]['energy'].append(features[0]['energy'])
        spotify_albums[album]['instrumentalness'].append(features[0]['instrumentalness'])
        spotify_albums[album]['liveness'].append(features[0]['liveness'])
        spotify_albums[album]['loudness'].append(features[0]['loudness'])
        spotify_albums[album]['speechiness'].append(features[0]['speechiness'])
        spotify_albums[album]['tempo'].append(features[0]['tempo'])
        spotify_albums[album]['valence'].append(features[0]['valence'])
        #popularity is stored elsewhere
        pop = sp.track(track)
        spotify_albums[album]['popularity'].append(pop['popularity'])
        track_count+=1


def mapping(item):
    uri_list = {}
    for info in item:
        name = info['name']
        
        uri = info['uri']
        ID = info['id']
        # print(ID)
        uri_list[name] = ID
        
    return uri_list

#To access authorised Spotify data
client_id = '716259e99ecd421580450ad70b0107d1'
client_secret = 'f857d4c4cd9d462089c03d846bc5bb60'
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) 

#spotify object to access 
APIname = 'sample' #chosen artist
result = sp.search(APIname) #search query
items = result['tracks']['items']

artists = []
for i,albums in enumerate(items):
# print(uri)
    artist = albums['artists']
    artists.append(artist)

# print(artists)
with open('spotify_monthly_listners.json', 'w') as outfile:
    json.dump(artists, outfile, sort_keys=True, indent=4)


album_uris = map(mapping, artists)
# print(list(album_uris))






spotify_albums = {}
album_count = 0
album_names = []
for i in album_uris: #each album
    key = list(i.keys())[0]
    uri = i[key]#[15:]
    # print(uri)
    spotify[key] = albumSongs(uri)
    # print("Album " + str(album_names[album_count]) + " songs has been added to spotify_albums dictionary")
    album_count+=1 #Updates album count once all tracks have been added

# print(spotify_albums)

# import time
# import numpy as np
# sleep_min = 2
# sleep_max = 5
# start_time = time.time()
# request_count = 0
# for i in spotify_albums:
#     audio_features(i)
#     request_count+=1
#     if request_count % 5 == 0:
#         print(str(request_count) + " playlists completed")
#         time.sleep(np.random.uniform(sleep_min, sleep_max))
#         print('Loop #: {}'.format(request_count))
# print('Elapsed Time: {} seconds'.format(time.time() - start_time))   


# dic_df = {}
# dic_df['album'] = []
# dic_df['track_number'] = []
# dic_df['id'] = []
# dic_df['name'] = []
# dic_df['uri'] = []
# dic_df['acousticness'] = []
# dic_df['danceability'] = []
# dic_df['energy'] = []
# dic_df['instrumentalness'] = []
# dic_df['liveness'] = []
# dic_df['loudness'] = []
# dic_df['speechiness'] = []
# dic_df['tempo'] = []
# dic_df['valence'] = []
# dic_df['popularity'] = []
# for album in spotify_albums: 
#     for feature in spotify_albums[album]:
#         dic_df[feature].extend(spotify_albums[album][feature])
        
# len(dic_df['album'])

# import pandas as pd
# df = pd.DataFrame.from_dict(dic_df)
# df

# print(len(df))
# final_df = df.sort_values('popularity', ascending=False).drop_duplicates('name').sort_index()
# print(len(final_df)) 

# final_df.to_csv("{a file location to store your csv}") 






