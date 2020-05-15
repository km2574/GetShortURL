# Setup and Installation of URL Shortner

Getting GetShortURL installed and ready-to-go should only take a few minutes.


### Local Installation

##### Requirements

Installing GetShortURL is easy and straightforward. Your system just needs to meet these few requirements:

* Python3.7
* MongoDB
* Linux 16.04 or newer version

##### Install Python

Install Python 3.9 using the following instructions.

```
$ sudo apt update sudo apt install python3.7
```

```
$ sudo apt install python3.7
```

##### Install MongoDB for python

I recommend using pip to install pymongo on all platforms

```
$ python -m pip install pymongo
```
##### Running the code on the local environment

One all the dependencies are installed, one need to execyte the main.py

```
$ python3 main.py
```
Then user will be asked to provide the input(s) as
```
$ Enter -1 to quit, 0 to short URL and 1 to make a search :
```
