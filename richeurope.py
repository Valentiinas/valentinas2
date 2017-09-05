from instapy import InstaPy

session = InstaPy(username='richeurope', password='videogaga321')
session.login()

session.set_do_comment(enabled=True, percentage=25)
session.set_comments(['Awesome stuff you have', 'Keep it up!', 'I like your work'])
session.set_do_follow(enabled=True, percentage=10, times=2)
session.like_by_tags(['richlife', 'richkidsofinstagram', 'richkids', 'luxury' , 'luxurycars'], amount=100)

session.set_user_interact(amount=5, random=True, percentage=50, media='Photo')
session.follow_user_followers(['richkidsofdubai', 'richkidsontheworld', 'richrussiankids'], amount=30, random=False, sleep_delay=60, interact=True)

session.set_user_interact(amount=5, random=True, percentage=50, media='Photo')
session.set_do_follow(enabled=False, percentage=70)
session.set_do_like(enabled=True, percentage=70)
session.set_comments(["Cool", "Super!"])
session.set_do_comment(enabled=True, percentage=80)
session.interact_user_followers(['exclusiv'], amount=50, random=True)


session.unfollow_users(amount=500, onlyInstapyFollowed = True )

session.end()
