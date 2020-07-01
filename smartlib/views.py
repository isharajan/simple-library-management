from django.shortcuts import render, redirect
from .mymodels import Book, mylib, Person

Users = []

def register_sess(request,person):
	request.session['login'] = True
	request.session['email'] = person.email

def is_loggedin(request):
	if request.session.get('login',False):
		person = Person.is_available(request.session['email'])
		if person!=False:
			return person
	return False

def login(request):
	person = is_loggedin(request)
	if person:
		return redirect('view_books')
	if request.method == "POST":
		email=request.POST['email']
		password=request.POST['password']
		person = Person.is_valid_cred(email,password)
		if person!= False:
			register_sess(request,person)
			return redirect(view_books)
		else:
			return render(request,'login.html', {"error": "Wrong Credentials"})
	else:
		return render(request,'login.html')

def register(request):
	person = is_loggedin(request)
	if person:
		return redirect('view_books')
	if request.method=="POST":
		person = Person.register(
				name=request.POST['name'],
				email=request.POST['email'],
				phone=request.POST['phone'],
				password=request.POST['password'],
			)
		if person:
			register_sess(request,person)
			return redirect(view_books)
		else:
			return render(request,'register.html',{'error': "Email already registered"})
	else:
		return render(request,'register.html')


def view_books(request):
	person = is_loggedin(request)
	if person==False:
		return redirect('login')
	book_data  = []
	for book in mylib.books:
		book_data.append({
				'bid':book.bid,
				'bname':book.bname,
				'current_owner':book.current_owner.name,
				'available':book.current_owner is mylib.admin
			})
	return render(request,'view_books.html',{'books':book_data, 'user':person})

def buy_book(request, bid):
	person = is_loggedin(request)
	if person==False:
		return redirect('login')
	mylib.buy_book(bid, person)
	return redirect(view_books)

def return_book(request, bid):
	person = is_loggedin(request)
	if person==False:
		return redirect('login')
	mylib.submit(bid, person)
	return redirect(profile)

def profile(request):
	person = is_loggedin(request)
	if person==False:
		return redirect('login')
	return render(request,'profile.html', {'user':person})

def logout(request):
	request.session['login'] = False
	request.session['email'] = None
	return redirect('login')