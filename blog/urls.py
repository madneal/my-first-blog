from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'$',views.post_list,name='post_list'),
    url(r'$',views.index,name='index'),
    url(r'^cv',views.cv,name='cv'),
    url(r'^cv_zh',views.cv_zh,name='cv_zh'),
    # url(r'^index/',views.index,name='index'),
    # url(r'$',views.index,name='index'),
]