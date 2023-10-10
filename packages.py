###PACKAGES 

###To Get DataFrame of Statistical Details of Channel Names you Enter
def get_channels_data():
    """Input:Fetches List of Channel Names from You Comma Seperated
    Returns: DataFrame of Statistical Details of Channel Names you Enter
    """
    
    
    from fetch import fetch_channel_name_list
    from channels import get_channels_stats
    from framer import framer
    inp=fetch_channel_name_list()
    ret=get_channels_stats(inp)
    ret_df=framer(ret)
    return ret_df

### To Get DataFrame of Video Details of only one Channel Name you Enter
def get_videos_data():
    """Input:Fetches Channel Name from You
    Returns: DataFrame of Video Details of Channel Name you entered
    """
    from fetch import fetch_channel_name_list
    from videos import get_videos_details
    from framer import framer
    name=fetch_channel_name_list()
    lst=get_videos_details(name)
    df=framer(lst)
    return df

### To Get DataFrame of Comments of Video ID you Enter
def get_comments_data():
    """Input:Fetches VIDEO ID from You
    Returns: DataFrame of 100 COMMENTS  of VIDEO ID you entered
    """
    from fetch import fetch_VIDEO_ID
    from framer import framer
    from comments import get_comments
    video_id=fetch_VIDEO_ID()
    lst=get_comments(video_id)
    df=framer(lst)
    return df

