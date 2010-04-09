# django-breakroom

django-breakroom is a Django implementation of [Watercoolr](http://watercoolr.nuklei.com/), a Ruby webhooks application.


## Requirements

python >= 2.5

django >= r10650


## Installation

To install run

    python setup.py install

which will install the application into python's site-packages directory.

Add to INSTALLED_APPS:

	'breakroom',

Add to urls.py:

	url(r'^path/to/breakroom/', include('breakroom.urls')),


## Usage

The following usage examples were taken from the [Watercoolr](http://watercoolr.nuklei.com/) web site.


### Create a channel

	→ POST /channels
	← { 'id': '2d0128d' }


### Add subscribers

	→ POST /subscribers data={ 'channel':'2d0128d', 'url':'http://api.otherservice.com/your-message-handler' }
	← { 'status': 'OK' }


### Post messages

	you → POST /messages data={ 'channel':'2d0128d', 'message':'hey guys!' }
	   us → POST http://api.otherservice.com/your-message-handler data='hey guys!'
	   ...for every subscriber...
	← { 'status': 'OK' }

