#---------------------------------------------------------------------------------
#Name:		Lyric Downloader
#Author:	Shujin Wu		
#Description: Search and download lyric for given song 
#---------------------------------------------------------------------------------

import urllib
from bs4 import BeautifulSoup

song=raw_input("Enter the correct name of the song:	").strip(" ").lower()

artist=raw_input("Enter the correct name of the artist:	").strip(" ").lower()

song=song.replace(" ","")
artist=artist.replace(" ","")


url_list=['http://www.azlyrics.com/lyrics/'+artist+'/'+song+'.html']
is_found = False
for url in url_list:
	#url="http://www.azlyrics.com/lyrics/adele/daydreamer.html"
	htmlText=urllib.urlopen(url).read()
	soup = BeautifulSoup(htmlText,"lxml")
	find_lyrics=soup.find_all("div")
	div = [x for x in find_lyrics if str(x).find("class=") == -1]

	print div[1]
	