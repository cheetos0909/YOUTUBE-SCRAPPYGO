##CHANNEL NAME
def fetch_channel_name():
    inputs=str(input("Enter one Channel Names Here with comma seperated  :"))
    return inputs

##CHANNEL NAME LIST
def fetch_channel_name_list():
    inputs=str(input("Enter Channel Names Here with comma seperated  :"))
    lists=inputs.split(sep=',')
    return lists

##CHANNEL ID
def fetch_channel_ID_list():
    inputs=str(input("Enter Channel IDs Here with comma seperated  :"))
    lists=inputs.split(sep=',')
    return lists

##PLAYLIST ID
def fetch_PLAYLIST_ID_list():
    inputs=str(input("Enter Playlist IDs Here with comma seperated  :"))
    lists=inputs.split(sep=',')
    return lists

##VIDEO ID list
def fetch_VIDEO_ID_list():
    inputs=str(input("Enter VIDEO IDs Here with comma seperated  :"))
    lists=inputs.split(sep=',')
    return lists

##VIDEO ID
def fetch_VIDEO_ID():
        inputs=str(input("Enter VIDEO ID Here   :"))
        return inputs


