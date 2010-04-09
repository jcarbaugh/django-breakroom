from breakroom.models import Channel, Subscriber
from django.http import HttpResponse, Http404
from django.utils import simplejson as json
import urllib, urllib2

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        kwargs['mimetype'] = 'application/json'
        content = json.dumps(data)
        super(JSONResponse, self).__init__(content, **kwargs)

def channels(request):
    data = {'status': 'FAIL'}
    if request.method == 'POST':
        data['id'] = Channel.objects.create().id
        data['status'] = 'OK'
    return JSONResponse(data)
        
def subscribers(request):
    
    data = {'status': 'FAIL'}
    
    if request.method == 'POST':
        
        channel_id = request.POST.get('channel', None)
        url = request.POST.get('url', None)
        
        try:
            
            c = Channel.objects.get(pk=channel_id, is_enabled=True)
            s = Subscriber(channel=c, url=url)
            s.save()
            
            data['status'] = 'OK'
        
        except Channel.DoesNotExist:
            pass
            
    return JSONResponse(data)

def messages(request):
    
    data = {'status': 'FAIL'}
    
    if request.method == 'POST':
        
        channel_id = request.POST.get('channel', None)
        message = request.POST.get('message', None)
        
        try:
            
            c = Channel.objects.get(pk=channel_id, is_enabled=True)
            
            data = urllib.urlencode({'message': message})
            
            for subscriber in c.subscribers.filter(is_enabled=True):
                try:
                    urllib2.urlopen(subscriber.url, data).close()
                except:
                    pass
            
            data['status'] = 'OK'
        
        except Channel.DoesNotExist:
            pass
            
    return JSONResponse(data)