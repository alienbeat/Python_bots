from instapy import InstaPy

#login credentials
insta_username = 'tuputacuenta'
insta_password = 'tuputopasword'

#login session
session = InstaPy(username=insta_username, password=insta_password)
session.login()

#follow by list

#target_users = session.target_list('accs.txt') 
#session.follow_by_list(target_users, times=1, sleep_delay=600)


session.follow_user_followers(['sanchezcastejon'], sleep_delay=150, amount=40, randomize=False, interact=True)

#like by Tag
session.like_by_tags(["YoMeVacunoSeguro", "socialistas","10N"], amount=10)

#Unfollow the back followers
#session.unfollow_users(amount=20, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=600)


session.set_do_comment(enabled=True, percentage=50)
session.set_comments(['que buena gente que eres pedro!', 'que si hombre, que si!', 'muy buena la mandanga'])