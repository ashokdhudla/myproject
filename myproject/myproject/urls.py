from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from myapp.views import *
admin.autodiscover()

urlpatterns = patterns('myapp.views',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/','Login'),
    url(r'^logout/','Logout'),
    url(r'^dashboard/','DashBoard'),
    # url(r'^myview/',Myview.as_view()),
)
