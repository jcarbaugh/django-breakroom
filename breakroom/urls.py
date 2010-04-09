from django.conf.urls.defaults import *

urlpatterns = patterns('breakroom.views',
    url(r'^channels/$', 'channels', name='breakroom_channels'),
    url(r'^subscribers/$', 'subscribers', name='breakroom_subscribers'),
    url(r'^messages/$', 'messages', name='breakroom_messages'),
)