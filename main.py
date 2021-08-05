from instabot import Bot
import schedule

# Deleting Config JSON 
import os 
import glob

exits = os.path.isdir('config')

if exits:
    cookie_del = glob.glob("config/*cookie.json")
    os.remove(cookie_del[0])


# Bot Initialise 
bot = Bot()

username = input("Enter username: ");
password = input("Enter password: ")
bot.login(username = username, password = password)

def _follow():
    # get followers of target account 
    target = input("Enter target account: ")
    target_followers = bot.get_user_followers(target)

    #Follow target followers
    for user in range(target_followers):
        bot.follow(target_followers[user])

def _unfollow():
    with open('config/followed.txt') as f:
        number_of_elements = len(f.readlines())
        for item in range(number_of_elements):
            user = f.readline()
            bot.unfollow(user) 


# Run Unfollow() every Monday:
schedule.every().monday.do(_unfollow)

while True:
    schedule.run_pending()
    _follow()