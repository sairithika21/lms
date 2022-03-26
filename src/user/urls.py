from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('login/',views.login,name='login'),
	path('register', views.register, name='register'),
	path('faillogin/',views.logincheck,name='logincheck'),
	path('issuesuccess/',views.issuesuccess,name='issuesuccess'),
	path('issuefail/',views.issuefail,name='issuefail'),
	path('request/',views.request, name = 'request'),
	path('request/active', views.requestactive, name='requestacive'),
	path('userdata/',views.userdata,name='userdata'),
	path('user/<str:userid>/', views.userprofile, name='profile'),
	path('books/',views.books, name='books'),
	path('book/add', views.addbook, name='addbook'),
	path('book/add/success', views.addbooksuccess, name = 'bookaddsuccess'),
	path('book/<str:bookid>/', views.bookdetails, name='bookinfo'),
]