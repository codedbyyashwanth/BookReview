from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from .models import BookData, FavBookData, ReviewData
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def Home(request):
        popular_books = BookData.objects.filter(book_review_star = 4)[:4]
        rated_books = BookData.objects.filter(book_review_star = 5)[:4]
        loginValue = False
        if request.session.keys() :
                if request.session['mail']:
                        loginValue = True
        context = { "data" : popular_books, "rated" : rated_books , 'iterator':range(1,6), "loggedIn" : loginValue }
        return render(request, 'index.html', context)

def Books(request):
        data = BookData.objects.all()
        loginValue = False
        if request.session.keys() :
                if request.session['mail']:
                        loginValue = True
        context = { "data" : data, 'iterator':range(1,6), "loggedIn" : loginValue }
        return render(request, 'books.html', context)

def Favourite(request):
        book_data = []
        data = FavBookData.objects.all()
        for values in data:
                book_id_data = BookData.objects.get(id=values.book_id)
                raw_data = { "book_image" : book_id_data.book_image, "book_review_star" : book_id_data.book_review_star, "book_name" : book_id_data.book_name, "id" : book_id_data.id }
                book_data.append(raw_data)
        loginValue = False
        if request.session.keys() :
                if request.session['mail']:
                        loginValue = True
        context = { "data" :  book_data, "iterator" : range(1, 6) ,"loggedIn" : loginValue }
        return render(request, 'favourite.html', context)

def AddToFav(request, id):
        mail = request.session['mail']
        FavData = FavBookData(book_id=id, user_email=mail)
        FavData.save()
        return redirect(Favourite)

def Login(request):
        if request.session.keys() :
                if request.session['mail']:
                        return redirect(Home)
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                        login(request, user)
                        request.session['mail'] = user.email
                        request.session['username'] = username
                        return redirect(Home)
        return render(request, 'login.html')

def Signup(request):
        if (request.method == "POST"):
                username = request.POST['username']
                mail = request.POST['mail']
                password = request.POST['password']
                user = User.objects.create_user(username, mail, password)
                request.session['mail'] = mail
                request.session['username'] = username
                user.save()
                return redirect(Home)
        if request.session.keys() :
                if request.session['mail']:
                        return redirect(Home)
        return render(request, 'signup.html')

def BookDetails(request, id):
        if request.method == "POST":
                review_title = request.POST['title']
                review_star = request.POST['rating']
                print(review_star)
                review_message = request.POST['message']
                mail = request.session['mail']
                book_review_count = request.POST['review_count']
                review_stars = ( int(book_review_count) + int(review_star) ) / 2
                review_stars = int(review_star)
                updateBookData = BookData.objects.get(id=id)
                updateBookData.book_review_star = review_stars
                updateBookData.save()
                reviewdata = ReviewData(book_id = id, user_email=mail, review_title=review_title, review_desc=review_message, review_star=review_star)
                reviewdata.save()
        data = BookData.objects.get(id=id)
        review_data = ReviewData.objects.filter(book_id=id)
        loginValue = False
        if request.session.keys() :
                if request.session['mail']:
                        loginValue = True
        context = { "data" : data, "review_data" : review_data ,"loggedIn" : loginValue }
        return render(request, 'book_details.html', context)