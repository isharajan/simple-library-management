# Create your models here.
class Book():
	bkid = 1
	def __init__(self,bname):
		self.bname = bname
		self.bid = Book.bkid
		Book.bkid = Book.bkid+1
		self.current_owner = None

	def __repr__(self):
		 return self.bname


class Person():
	pid = 0
	persons = []

	def __init__(self,name, email="", phone="", password=""):
		self.name = name
		self.email = email
		self.phone = phone
		self.pid = Person.pid
		self.password=password
		Person.pid = Person.pid +1
		self.books =[]
		Person.persons.append(self)

	@classmethod
	def is_available(cls, email):
		for person in cls.persons:
			if (person.email==email):
				return person
		return False

	@classmethod
	def is_valid_cred(cls,email,password):
		person = cls.is_available(email)
		if person!=False:
			if person.password==password:
				return person
		return False

	@classmethod
	def register(cls, name, email, phone, password):
		if cls.is_available(email) == False:
			person = cls(name,email,phone,password)
			return person
		else:
			return False

class Library():

	admin = Person('admin',email="admin@library.com", phone="9500012345")
	def __init__(self,books=[]):
		self.books = []
		for book in books:
			book.current_owner = Library.admin
			self.books.append(book)

	def buy_book(self,bid,person):
		for bk in self.books:
			if(bk.bid == bid and bk.current_owner is Library.admin):
				bk.current_owner = person
				person.books.append(bk)
				return True
		return False

	def submit(self,bid,person):
		for book in person.books:
			if book.bid==bid:
				book.current_owner = Library.admin
				person.books.remove(book)
				break

	def add(self,book):
		book.current_owner = Library.admin
		self.books.append(book)

	def get_availablebooks(self):
		available_books =[]
		for bk in self.books:
			if(bk.current_owner is Library.admin):
				available_books.append(bk) 
		return available_books

	def get_bookstatus(self):
		for book in self.books:
			print (book.bname,book.current_owner.name)

	def is_available(self,book):
		for avbl_book in self.available_books():
			if avbl_book.name == book.name:
				return True
		return False

	def __repr__(self):
		 return self.book_name

booklst =['tamil','english','maths','science','social']*10
objlst =[]
for book_name in booklst:
	bo=Book(book_name)
	print ("Added  ",book_name)
	objlst.append(bo)
mylib = Library(books=objlst)