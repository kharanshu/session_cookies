from django.http import HttpResponse
from django.http import response
from django.shortcuts import render, redirect
from django.http.response import HttpResponse

# Create your views here.

def set_cookie(request):
    response = render(request, template_name="cookie.html")
    if request.COOKIES.get('visits'):
        response.set_cookie('data', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))  # 2
        response.set_cookie('visits', value + 1)  # 3 
    else:
        value = 1
        text = "Welcome for the first time"
        response.set_cookie('visits', value)
        response.set_cookie('data', text)
    # response.set_cookie("name","Kharanshu")
    # response.set_cookie("age","25")
    return response

def get_cookie(request):
    nm = request.COOKIES.get('name')
    ag = request.COOKIES.get('age')
    print(nm, ag)
    return render(request, "show_cookie.html")

def homepage(request):
    print(request.COOKIES.items())
    return HttpResponse("Hi u r in Homepage...!!!")


def del_cookie(request):
    response = redirect("home")
    response.delete_cookie("name")
    response.delete_cookie("age")
    return response

def cookie_session(request):
    print(request.session)
    request.session.set_test_cookie()
    return HttpResponse("<h1>Welcome to Django Session</h1>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        print("In delete cookie")
        print(request.session.delete_test_cookie())
        response = HttpResponse("Cookie Deleted...!!!")
    else:
        response = HttpResponse("Your browser does not accept cookies")
    return response

def demo_view(request):
    print(request.session.__dict__)
    return HttpResponse("In Demo View")



def create_session(request):
    print(request.session.__dict__)
    request.session['name'] = 'admin'
    request.session['password'] = 'admin'
    request.session['age'] = 25
    request.session['city'] = "Pune"
    print(request.session.__dict__)
    return HttpResponse("The session is Created...!!!")

def show_session_data(request):
    print(request.session.items())
    return render(request, 'session.html')


def delete_session(request):
    print(request.session.items())
    del request.session['name']
    del request.session['password']
    del request.session['age']
    return HttpResponse(f"Session data deleted:- {['name', 'password', 'age']}")



