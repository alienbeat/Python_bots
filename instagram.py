# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'ponetuusuario'  # <- enter username here
insta_password = 'tuputacontraseña'  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    

    # activity
    #target_users = session.target_list('accs.txt') 
    #session.follow_by_list(target_users, times=1, sleep_delay=600)
    session.like_by_tags(["disney", "mickey"], amount=5)
    session.set_do_follow(True, percentage=100)
    session.set_do_comment(True, percentage=50)
    session.set_comments(["Nice!", "Sweet!", "Beautiful"])
    session.end()



    
    