def program():
    from packages import get_channels_data
    from packages import get_videos_data
    from packages import get_comments_data
    
    
    
    inp=int(input('''What do you want to perform?
                  1)To Get DataFrame of Statistical Details of YouTube Channels 
                  2)To Get DataFrame of Video Details of only one YouTube Channel
                  3)To Get DataFrame of Comments of Video
                  
                  '''))
    if inp==1:
        return get_channels_data() 
          
    elif inp==2:
        return get_videos_data()
        
    elif inp==3:
        return get_comments_data()
        
    else:
        print('Invalid Input')

def omega():
    from main import main
    inp=str('Want to go back to Main Menu? [y/n]')
    if inp=='y' or 'Y':
        return main()
    else :
        return None