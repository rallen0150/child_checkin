from django.conf.urls import url, include
from django.contrib import admin

from checkin_app.views import UserCreateView, IndexView, ChildCreateView, \
                              ChildDetailView, ChildUpdateView, EmployeeListView, \
                              SchoolDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls'), name='login'),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^child/create/$', ChildCreateView.as_view(), name='child_create_view'),
    url(r'^child/(?P<pk>\d+)/$', ChildDetailView.as_view(), name='child_detail_view'),
    url(r'^child/(?P<pk>\d+)/checkin/$', ChildUpdateView.as_view(), name='child_update_view'),
    url(r'^employee/$', EmployeeListView.as_view(), name='employee_list_view'),
    url(r'^school/$', SchoolDetailView.as_view(), name='school_detail_view'),
]
