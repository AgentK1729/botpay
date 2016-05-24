from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth import login, authenticate, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'botpay.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
					   
	url(r'^$', 'botpay.chatbot.views.home'),
					   
	url(r'^home/', 'botpay.chatbot.views.home'),
					   
	url(r'^profile/', 'botpay.chatbot.views.profile'),
					   
	url(r'^logout/', 'botpay.chatbot.views.Logout'),
					   
	url(r'^history/', 'botpay.banker.views.history', name='history'),
					   
	url(r'^chat/', 'botpay.chatbot.views.chat', name='chat'),
					   
	url(r'^process/', 'botpay.banker.views.process'),
)
