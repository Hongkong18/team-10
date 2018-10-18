from django.urls import path
from . import views

app_name = 'intermgmt'
urlpatterns = [
	path('', views.index, name='index'),
	path('event/1/', views.event, name='event'),#no space is allowed within <>
	path('event/1/resultvol', views.resultvol, name='resultvol'),
	path('event/1/selectvol', views.selectvol, name='selectvol'),
	path('event/1/balance', views.balance, name='balance'),
	
	# path('authorid/<int:author_id>/results/', views.results, name='results'),
	# path('authorid/<int:author_id>/vote/', views.vote, name='vote'),
	path("login", views.login_view, name="login"), #'django.contrib.auth.views.login' 
    path("signup", views.signup, name="signup"),
    path("logout", views.logout_view, name="logout"),
     #path("portfolio", views.portfolio, name="portfolio"),
]