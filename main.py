from URLissue import *
from pymongo import MongoClient

# Establishing connection with database
try:
	client = MongoClient('mongodb://127.0.0.1:27017/')
except:
	print("Could not connect to MongoDB")


# Access database
urldb = client['Shorted_URL_list']

# Access collection of the database
urllist = urldb.urls


#creating a instance of the URLShortener method
nb_shortener = URLShortener()

#using dictionary
dict_obj = {}

#Driver Code
#keep on taking input untill encounters a NULL value
while True:

	url = input('URL:')

	if len(url) == 0:
		break
	else:
		sort_url = nb_shortener.shortenUrl(url)

	#updating dict after every iteration
	dict_obj[sort_url] = url
print(dict_obj)
mongoUrlList = urllist.insert_one(dict_obj)