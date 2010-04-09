from django.contrib import admin
from breakroom.models import Channel, Subscriber

class SubscriberInline(admin.TabularInline):
    model = Subscriber

class ChannelAdmin(admin.ModelAdmin):
    
    def enable_channels(self, request, queryset):
        count = queryset.update(is_enabled=True)
        self.message_user(request, "%i successfully enabled." % count)
    
    def disable_channels(self, request, queryset):
        count = queryset.update(is_enabled=False)
        self.message_user(request, "%i successfully disabled." % count)
    
    enable_channels.short_description = "Enable selected channels"
    disable_channels.short_description = "Disable selected channels"
    
    actions = [enable_channels, disable_channels]
    inlines = (SubscriberInline,)
    list_display = ('id','name','timestamp','is_enabled')
    list_filter = ('is_enabled',)

admin.site.register(Channel, ChannelAdmin)