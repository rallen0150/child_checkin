from django.conf.urls import url, include
from django.contrib import admin

from checkin_app.views import UserCreateView, IndexView, ChildCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls'), name='login'),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^child/create/$', ChildCreateView.as_view(), name='child_create_view'),
]
