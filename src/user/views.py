from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

users = [
    {'id': 1, 'name': 'rithika','password':'rithika','email' : 'rithika@unt.edu','firstname' : 'sai rithika','image':'https://www.iconsdb.com/icons/preview/gray/user-xxl.png','books_taken': 1, 'books_returned':4,'fine':50,'mobile_number' : 1234567890, 'books_due': 4},
    {'id': 2, 'name': 'pravalli','password':'pravalli', 'email' : 'pravalli@unt.edu','firstname': 'pravalli','image':'https://www.iconsdb.com/icons/preview/gray/user-xxl.png','books_taken': 1, 'books_returned':4,'fine':50,'mobile_number' : 1234567890, 'books_due': 4},
    {'id': 3, 'name': 'manohara chari','password':'manohara','email' : 'manoharachari@unt.edu','firstname' : 'manohara chari','image':'https://www.iconsdb.com/icons/preview/gray/user-xxl.png','books_returned':4,'fine':50,'books_taken': 1, 'mobile_number' : 1234567890, 'books_due': 4},
    {'id': 4, 'name': 'dinesh','password':'dinesh', 'email' : 'dinesh@unt.edu','firstname': 'dinesh','books_taken': 1,'image':'https://www.iconsdb.com/icons/preview/gray/user-xxl.png', 'books_returned':4,'fine':50,'mobile_number' : 1234567890, 'books_due': 4},
]

books_data = [
    {
        'id':1,
        'title': 'usability testing',
        'author': 'self',
        'short_desc': 'this is a short description about the book that renders here',
        'long_desc' : 'this is a long description that describes the author name and his intention to write this book and its uses of the book and his target audience',
        'count' : 5,
        'books_on_hand' : 2,
        'available': True,
        'fine': 20,
        'book_image' : 'https://images.unsplash.com/photo-1589998059171-988d887df646?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1176&q=80',
    }
]

lms = [
	{'title': 'number of books', 'count': 30},
	{'title': 'books issued', 'count': 30},
	{'title': 'number of books in library', 'count': 30},
	{'title': 'unique books total ', 'count': 30},

]

requests = [
	{'userid': 1, 'title' : 'usability testing', 'bookid' : 1, 'requestd_on': '03/24/2022', 'request_from': '03/25/2022', 'request_to': '05/01/2022'}
]

def home(request):
    return render(request,'home.html', {'lms' : lms})
def login(request):
    return render(request,'login.html')
def register(request):
	return render(request, 'register.html')
def request(request):
    return render(request,'request.html')
def logincheck(request):
    return render(request,'login_fail.html')
def issuesuccess(request):
    return render(request,'issuesuccess.html')
def issuefail(request):
    return render(request,'issuefail.html')
def userdata(request):
    return render(request,'user_data.html',{'users' : users})
def userprofile(request,userid):
    user_info = None
    for user in users:
        if user['id'] == int(userid):
            user_info = user 
    context = {'user_info': user_info}
    return render(request,'profile.html',context)
def books(request):
    return render(request,'books.html',{'books': books_data})
def addbook(request):
	return render(request, 'addbook.html')
def addbooksuccess(request):
	return render(request, 'addbooksuccess.html')
def requestactive(request):
	return render(request, 'activerequests.html')
def bookdetails(request,bookid):
    book_info = None
    for book in books_data:
        if book['id'] == int(bookid):
            book_info = book 
    context = {'book_info': book_info}
    return render(request,'book_detail.html',context)
