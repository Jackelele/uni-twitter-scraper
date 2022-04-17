
# importing the modules
from ast import keyword
import json
import sys, time, signal
import os
from twitter_scraper_selenium import scrap_keyword


# ~~~~ Keybord interruption ~~~~
def signal_handler(signal, frame):
    print('\033[1;m [\033[1;31mX\033[1;m] You pressed Ctrl+C!')
    time.sleep(2)
    EXITMENU()

#~~~~ EXIT ~~~~
def EXITMENU():
	time.sleep(1)
	print("\033[1;m Thanks for using Twitter Scraper\033[1;m")
	time.sleep(2)
	print
	print("\033[1;m[\033[1;31mX \033[1;32mClosing")
	time.sleep(1)
	sys.exit()
		

#~~~~ Tool ~~~~
signal.signal(signal.SIGINT, signal_handler)

print("What Kewyword do you want to search for?")
keyword = input()
print("How many tweets do you want to search?")
numoftweets = int(input())
tweet = scrap_keyword(keyword=keyword, browser="firefox",
                      tweets_count=numoftweets, output_format="json")
print(tweet)
#try:
#    with open(f'output/scrapped_data.json', 'w') as outfile:
#        json.dump(tweet, outfile, indent=5)
#except:
#    print("An error has occured, please check console for details.")
