from methods import *

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

#print list of shorten url
print(dict_obj)