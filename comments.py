from googleapiclient.discovery import build
from api import api_key
youtube=build('youtube','v3',developerKey=api_key)

###TO EXTRACT COMMENTS OF EACH VIDEO
def get_comments(video_id):
    """Input Type :Video ID Returns Comments with Author Name
    """    
    
    response=youtube.commentThreads().list(
        part='snippet,id',
        videoId=video_id,
        maxResults=100
    ).execute()

    list=[]
    for i in range(len(response['items'])):
        datag=dict(Author_Name= response['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                   Comment = response['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay'],
                   Like_Count=response['items'][i]['snippet']['topLevelComment']['snippet']['likeCount'],
                   Author_Channel_ID=response['items'][i]['snippet']['topLevelComment']['snippet']['authorChannelId']['value'],
                   Published_at=response['items'][i]['snippet']['topLevelComment']['snippet']['publishedAt']
        )
        list.append(datag)
    next_page_token= response.get('nextPageToken')
    more_pages = True

    while more_pages and len(list) < 100:
        if next_page_token is None:
            more_pages=False
        else:
            response=youtube.commentThreads().list(
                part='snippet,id',
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token
                ).execute()

    
            for i in range(len(response['items'])):
                datag=dict(Author_Name= response['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                        Comment = response['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay'],
                        Like_Count=response['items'][i]['snippet']['topLevelComment']['snippet']['likeCount'],
                        Author_Channel_ID=response['items'][i]['snippet']['topLevelComment']['snippet']['authorChannelId']['value'],
                        Published_at=response['items'][i]['snippet']['topLevelComment']['snippet']['publishedAt']
                )
                list.append(datag)
            next_page_token= response.get('nextPageToken')

    
    return list



    
    
    