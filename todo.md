### There still exist some changes to be made in order to make this GetShortURL more smart

* As explained in the readme.md file the 'range counter' method to shorten url has a privacy issue.
It generates the url in a sequential manner which can cause a serious threat and on the contrary it can be tackled quite easily. One just need to add few character around the generated short url.

* MongoDB doesn't support keys with a dot.
There isn't a standard workaround to this issue, the best approach is too dependent upon the specifics of the situation.
we can replace the character used in place of [dot] after retrieving the data from DB or problem can be avoided by using other storage methods like Apache ZooKeeper etc.
