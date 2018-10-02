from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import Tweet
from .forms import LoginForm, UserForm, TweetForm
from django.contrib.auth import authenticate, login, logout
from .models import User


class Index(View):

    def get(self,request):
        return render(request, 'base.html')

class MainPage(View):

    def get(self, request):
        #all_tweet = Tweet.objects.all()
        all_tweet = Tweet.objects.filter(dependence__username=request.user)
        return render(request, 'mainpage.html', {'all_tweet': all_tweet})

    def post(self, request):
        pass


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        loginuser = request.POST['login']
        passworduser = request.POST['password']
        if loginuser and passworduser:
            user = authenticate(username=loginuser, password=passworduser)
            if user is not None:
                login(request, user)
                return redirect('mainpage')
        else:
            return redirect('login-view')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login-view')

class AddTwitter(View):

    def get(self, request):
        form = TweetForm()
        user = request.user
        if user.is_authenticated:
            return render(request,'addtweet.html', {'form': form})
        else:
            return redirect('login-view')


    def post(self, request):
        form = TweetForm(request.POST)
        if form.is_valid():
            Tweet.objects.create(dependence=request.user, content=form.cleaned_data['content'])
            return redirect('mainpage')


class AddUserView(View):

    def get(self, request):
        return render(request, 'sign.html')

    def post(self, request):
        loginuser = request.POST['login']
        passworduser = request.POST['password']
        emailuser = request.POST['email']
        if loginuser and passworduser and emailuser:
            User.objects.create(username=loginuser, password=passworduser, email=emailuser)

            return redirect('login-view')
        else:
            return redirect('adduser-view')
