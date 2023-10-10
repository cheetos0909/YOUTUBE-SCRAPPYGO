from googleapiclient.discovery import build
from api import api_key
youtube=build('youtube','v3',developerKey=api_key)



##GET CHANNEL ID



def get_channel_id(channel_name):
    """
    This Function is made to return Channel ID of Single Channel Name you invoke into the Function.
    """
    search_response=youtube.search().list(
        q=channel_name,
        type='channel',
        part='id'
    ).execute()

    if 'items' in search_response:
        channel_id=search_response['items'][0]['id']['channelId']
        return channel_id
    else:
        return None
    
##GET CHANNEL ID LIST
def get_channel_id_list(lst):
    """
    This Function is made to return list of Channel IDs of multiple Channel Names you invoke into the Function,in form of list.
    """
    j=[]
    for i in lst:
        dicto=dict(Name=i,ID=get_channel_id(i))
        j.append(dicto)
    return j ##RETURNS LIST OF DICTIONARY

##GET PLAYLIST ID LIST OF MANY CHANNEL

def get_playlist_id(channel_names): ##INPUT TYPE SHOULD BE LIST
    """
    This Function is made to return playlist IDs of multiple Channel Names you invoke into the Function,in form of list.
    """
    all_data=[]
    doco=get_channel_id_list(channel_names)
    channel_ids=[]
    for id in doco:
        channel_ids.append(id['ID'])
    request=youtube.channels().list(
        part='contentDetails',
        id=channel_ids).execute()
    for i in range(0,len(request['items'])):
        dicto=(
            request['items'][i]['contentDetails']['relatedPlaylists']['uploads']
        )
        all_data.append(dicto)
    return all_data ##RETURNS LIST OF DICTIONARY
# print(get_playlist_id(['Saket Gokhale','Samay Raina','Matt Rife']))




##GET VIDEO ID LIST OF A SINGLE CHANNEL

def get_video_ids( channel_name):
    """Input Type: List
    
    This function Returns all video ids of a channel name you invoke into the function.
    """
    # channel_name=list(channel_name)
    a=get_playlist_id(channel_name)
    playlist_id=a[0]
    request= youtube.playlistItems ().list(
            part='contentDetails',
            playlistId = playlist_id,
            maxResults = 50)
    response = request.execute()
    video_ids = []
    for i in range (len (response ['items'])):
        video_ids.append(response ['items'] [i] ['contentDetails']['videoId'])
        next_page_token= response.get('nextPageToken')
    more_pages = True


    while more_pages:
        if next_page_token is None:
            more_pages=False
        else:
            request = youtube.playlistItems().list(
                        part='contentDetails',
                        playlistId = playlist_id,
                        maxResults = 50,
                        pageToken = next_page_token)
            response = request.execute()

            for i in  range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            next_page_token=response.get('nextPageToken')

    return video_ids
# print(get_video_ids(['Saket Gokhale']))