from methods import *
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

	choice = int(input('Enter -1 to quit, 0 to short URL and 1 to make a search :'))
	
	#Enter -1 to quit
	if choice == -1:
		break
	
	#Enter 0 to short URL
	elif choice == 0:
		url = input('Enter URL :')
		short_url = nb_shortener.shortenUrl(url)

		#print last shorten  url
		print(short_url)

		#updating dict after every iteration
		dict_obj[short_url] = url

		#updating db after every iteration and avoiding the chances of duplicity
		for i in range(2): 
		    dict_obj['i'] = i 
		    if '_id' in dict_obj: 
		        del dict_obj['_id'] 
		mongoUrlList = urllist.insert_one(dict_obj)


	#Enter 1 to make a search
	elif choice == 1:
		keyUrl = input('Enter the shortern url to get original one :')
		print(urllist.find({},{keyUrl}))
		
		

	#bad input
	else:
		print('Opps! Try again.')