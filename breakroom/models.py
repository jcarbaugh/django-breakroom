from django.db import models
import uuid

class ChannelManager(models.Manager):
    def create(self):
        c = Channel(id=uuid.uuid4().hex)
        c.save()
        return c

class Channel(models.Model):
    objects = ChannelManager()
    id = models.CharField(max_length=64, primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    is_enabled = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-timestamp',)
    
    def __unicode__(self):
        return self.name or self.id

class Subscriber(models.Model):
    channel = models.ForeignKey(Channel, related_name='subscribers')
    url = models.URLField(verify_exists=False)
    is_enabled = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-timestamp',)
        unique_together = ('channel','url')
    
    def __unicode__(self):
        return u"%s %s" % (self.channel, self.url)