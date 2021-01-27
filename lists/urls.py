from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^new$',views.new_lists,name='new_list'),
    url(r'^(\d+)/$',views.view_lists,name='view_list'),
    url(r'^user/(.+)/$',views.my_lists,name='my_lists'),
]
