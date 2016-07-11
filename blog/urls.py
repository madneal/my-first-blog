from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$',views.post_list,name='post_list'),
    url(r'^$',views.index,name='index'),
    url(r'^cv-en/',views.cv),
    url(r'^cv_zh/',views.cv_zh),
    url(r'^download_file/',views.download_file),
    url(r'^download_cv/',views.download_cv),
    url(r'^project/',views.project),
    url(r'^myself/',views.myself),
    url(r'^paper/',views.paper),
    url(r'^project_zh',views.project_zh),
    url(r'^weatherapp/',views.weatherapp),


    # url(r'^index/',views.index,name='index'),
    # url(r'$',views.index,name='index'),
]