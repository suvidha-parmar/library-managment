from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from lms.models import Book
from .forms import UserRegisterForm


# Create your views here.

def index(request):
    return render(request, 'index.html', {'title':'index'})

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() 
            username= form.cleaned_data.get('username')     
            email= form.cleaned_data.get('email')
            password= form.cleaned_data.get('password')
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request,"register.html",{'form':form})


def Login(request):

    if request.method == 'POST':
        
        
        username = request.POST['username']
        #email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            form = login(request, user)
            
            if  user.is_superuser:
                messages.success(request, f' welcome {username} !!')
                return redirect('add_book')
            else:
                messages.success(request, f' welcome  {username} student!!')
                return redirect('view_books')

        else:
            messages.info(request, f'account  not exit plz sign up')

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    



@login_required
def add_book(request) :
    
    if request.method == 'POST':
        bookname= request.POST['bookname']
        author = request.POST['author']
        isbnum = request.POST['isbn']
        category = request.POST['category']
        
        Book.objects.create(name=bookname,author=author, isbn=isbnum, category=category)
        return redirect('view_books')
    return render(request,'add_book.html')

@login_required
def delete_book(request,id):
    book=Book.objects.filter(id=id)
    book.delete()
    return redirect('view_books')

@login_required 
def edit_book(request,id):
    book=Book.objects.get(id=id) 
    if request.method == "POST":
        bookname= request.POST['bookname']
        author = request.POST['author']
        isbnum = request.POST['isbn']
        category = request.POST['category']
        
        book.name = bookname
        book.author = author
        book.isbn = isbnum
        book.category = category
        book.save()
        return redirect('view_books')


    return render(request,'edit_book.html',{'book':book})

@login_required 
def view_books(request):
   
    is_superuser = request.user.is_superuser        
    books=Book.objects.all()
   
    return render(request,'view_books.html',{'books':books,'is_superuser':is_superuser})
