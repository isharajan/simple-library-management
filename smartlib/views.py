from django.shortcuts import render, redirect
from .models import Book, User, Library
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def login_view(request):
	if request.method == "POST":
		email=request.POST['email']
		password=request.POST['password']
		print (request.POST,">>>>>>>>>>>>")
		user = authenticate(request, username=email, password=password)
		if user is not None:
			login(request, user)
			return redirect(view_books)
		else:
			return render(request,'login.html', {"error": "Wrong Credentials"})			
	else:
		return render(request,'login.html')

def register(request):
	if request.method=="POST":
		try:
			user = User.objects.create_user(first_name=request.POST['name'], username=request.POST['email'], password=request.POST['password'])
			user = authenticate(username=request.POST['email'], password=request.POST['password'])
			login(request, user)
			return redirect(view_books)
		except IntegrityError:
			return render(request,'register.html',{'error': "Email already registered"})
	else:
		return render(request,'register.html')

@login_required(login_url='login')
def view_books(request):
	book_data  = []
	for book in Book.objects.all():
		data = {
				'bid':book.id,
				'bname':book.bname,
				'available':(book.current_owner is book.libery.admin) or (book.current_owner is None)
			}
		data['current_owner'] = book.libery.admin.username if data['available'] else book.current_owner.username
		book_data.append(data)
	return render(request,'view_books.html',{'books':book_data, 'user':request.user})

@login_required(login_url='login')
def buy_book(request, bid):
	book = Book.objects.get(id=bid)
	request.user.books.add(book)
	return redirect(view_books)

@login_required(login_url='login')
def return_book(request, bid):
	book = Book.objects.get(id=bid)
	book.current_owner = None
	book.save()
	return redirect(profile)

@login_required(login_url='login')
def profile(request):
	return render(request,'profile.html', {'user':request.user})

def logout_view(request):
    logout(request)
    return redirect(login_view)