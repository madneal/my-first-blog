from django.db import models
from django.utils import timezone
from django.http import HttpResponse
#from django_decorators.decorators import json_response
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# class weatherApp(models.Model):
#     city = models.ForeignKey()
#     api = "http://api.openweathermap.org/data/2.5/weather?q=";
#     units = "&units=metric";
#     appid = "&APPID=061f24cf3cde2f60644a8240302983f2"
#     cb = "&callback=JSON_CALLBACK";
#
#     url = "http://ipinfo.io/json?callback=JSON_CALLBACK"
#     def get_location(self,url):
#         obj = 'JSON'
#         city = obj.city