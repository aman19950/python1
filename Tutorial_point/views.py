from django.http import HttpResponse
from django.shortcuts import redirect, render
from matplotlib.style import use
from . models import user_signup
# Create your views here.
from django.contrib.auth.hashers import check_password, make_password


def index(request):
    return render(request, 'home.html')


def contact_dtls(request):
    return render(request, 'contact.html')


def sign_up(request):
    if request.method == "POST":
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')

        save_info = user_signup(first_name=fname, last_name=lname, email=email,
                                password=make_password(password), mobile=mobile, gender=gender)
        save_info.save()

        return HttpResponse("registration succsessfull")


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            fetch_info = user_signup.objects.get(email=email)
            if(check_password(password, fetch_info.password)):

                # print("you have entered correct password")
                request.session['name'] = fetch_info.first_name
                return redirect('home')

            else:
                return HttpResponse("please enter a valid password")

        except:
            return HttpResponse("please enter a valid email....")
