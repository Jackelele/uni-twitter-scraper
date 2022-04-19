
# importing the modules
from ast import keyword
import json
import sys
import time
import signal
import os
from twitter_scraper_selenium import scrap_keyword, scrap_profile

# ~~~ Function EHU ~~~~

def EHU():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# ~~~~ Keybord interruption ~~~~


def signal_handler(signal, frame):
    print('\033[1;m [\033[1;31mX\033[1;m] You pressed Ctrl+C!')
    time.sleep(2)
    EXITMENU()
signal.signal(signal.SIGINT, signal_handler)
# ~~~~ EXIT ~~~~


def EXITMENU():
    time.sleep(1)
    print("\033[1;m Thanks for using Twitter Scraper\033[1;m")
    time.sleep(2)
    print
    print("\033[1;m[\033[1;31mX \033[1;32mClosing")
    time.sleep(1)
    sys.exit()

# ~~~~ M E N U ~~~~


def menu():
    time.sleep(1)
    print("""
\033[1;33m    	1.\033[1;m Twitter Profile Tweets
\033[1;33m     	2.\033[1;m Keyword Search
\033[1;33m     	3.\033[1;m Scrape Profile Info
	""")

    OPT = input("\033[1;35m  Select:\033[1;m ")
    if OPT == "1":
        ProfileTweets()
    elif OPT == "2":
        Keyword()
    elif OPT == "3":
        Profile()
    else:
        EHU()
        print("\033[1;31m[ERROR]\033[1;m selection invalid!")
        time.sleep(3)
        menu()

def ProfileTweets():
    EHU()
    time.sleep(1)
    print("\033[1;35m What Profile do you want to scrape?")
    profile = input()
    print("\033[1;35m How many tweets do you want to scrape?")
    amount = int(input())
    SProfile = scrap_profile(twitter_username=profile, output_format="csv", browser="firefox", tweets_count=amount, filename=profile)
    print("\033[1;32m Tweets have been placed in output file " + profile + ".csv")

def Keyword():
    EHU()
    time.sleep(1)
    print("\033[1;35m What keyword do you want to search?")
    keyword = input()
    print("\033[1;35m How many tweets do you want to scrape?")
    numoftweets = int(input())
    tweet = scrap_keyword(keyword=keyword, browser="firefox", tweets_count=numoftweets, output_format="csv", filename=keyword)
    print("\033[1;32m Tweets have been placed in output file " + keyword + ".csv")

def Profile():
    print("SoonTm")
    
menu()

