from django.conf.urls import url
from django.urls import path
from appraise import views

urlpatterns = [
    url(r'^photo/', views.show_indent, name='photo'),
    url(r'^upload/', views.upload, name="upload"),
    url(r'^delete/(\w+)', views.deletephoto, name="delete"),
    url(r'^download/(\w+)', views.download, name="dl")
]