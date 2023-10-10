
def framer(lst):
    """Frames your list into a dataframe"""
    import pandas as pd
    frame=pd.DataFrame(lst)
    return frame

def preproces_video_details(video_data):
    
    """This function helps to convert dtypes of dataframe containing video statistical details of a single channel """
    import pandas as pd
    video_data['Published_date']=pd.to_datetime(video_data['Published_date']).dt.date
    video_data['Views']=pd.to_numeric(video_data['Views'])
    video_data['Likes']=pd.to_numeric(video_data['Likes'])
    video_data['Comments']=pd.to_numeric(video_data['Comments'])
    return video_data
