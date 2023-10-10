from googleapiclient.discovery import build
from api import api_key
youtube=build('youtube','v3',developerKey=api_key)



##TO GET STATISTICAL DETAILS OF MUTLIPLE OR SINGLE CHANNELS 
def get_channels_stats(channel_names):
    """Input : List of Channel Names you wish to Analyze
       Return : List of Dictionary
    
    
    
    This Function is Used to Get Details of each channel like Description ,Country,Subscribers 
     Video Count ,  Views Count , Playlist ID """
    from get_id import get_channel_id_list
    all_data=[]
    channel_ids1=get_channel_id_list(channel_names)
    channel_ids=[]
    for k in channel_ids1:
        channel_ids.append(k['ID'])

    response=youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=channel_ids).execute()
    for i in range(0,len(response['items'])):
        data=dict(Channel_Name=response['items'][i]['snippet']['title'],
        Description=response['items'][i]['snippet']['description'],
        # Country=response['items'][i]['snippet']['country'],
        Subscribers=response['items'][i]['statistics']['subscriberCount'],
        Views=response['items'][i]['statistics']['viewCount'],
        Videos=response['items'][i]['statistics']['videoCount'],
        Playlist_ID=response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)
    return all_data
