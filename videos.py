from googleapiclient.discovery import build
from api import api_key
youtube=build('youtube','v3',developerKey=api_key)



###GET VIDEO DETAILS OF ALL VIDEOS OF A CHANNEL
def get_videos_details(channel_name):
    """
    Input:Channel Name
     Returns : Video IDs , Titles,Published Date,Views,Likes,Comments Counts of all Videos of channel """
    from get_id import get_video_ids
    video_ids=get_video_ids(channel_name)
    all_video_stats=[]
    for i in range(0,len(video_ids),50):
        request=youtube.videos().list(
            part='snippet,statistics',
            id=','.join(video_ids[i:i+50]))
        response= request.execute()

        for video in response[ 'items']:
            
            
            if 'statistics' in video and 'commentCount' in video['statistics']:

                video_stats=dict(Title= video['snippet']['title'],
                                Published_date=video['snippet']['publishedAt'],
                                Views = video['statistics']['viewCount'],
                                # Likes= video['statistics']['likeCount'],
                                Comments= video['statistics']['commentCount'],
                                VIDEO_ID=video['id']

                                
                )
                all_video_stats.append(video_stats)
        
    return all_video_stats 
    