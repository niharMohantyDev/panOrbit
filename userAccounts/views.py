from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@csrf_exempt
def signup(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email') if request.POST.get('email') else None
            first_name = request.POST.get('first_name') if request.POST.get('first_name') else None
            last_name = request.POST.get('last_name') if request.POST.get('last_name') else None
            gender = request.POST.get('gender')  if request.POST.get('gender') else None
            phone_number = request.POST.get('phone_number') if request.POST.get('phone_number') else None

            # Check if user with the provided email already exists
            if CustomUser.objects.filter(email=email).exists():
                return render(request, "alreadyExist.html")

            user = CustomUser.objects.create_user(email=email, first_name=first_name, last_name=last_name, gender=gender, phone_number=phone_number)
            user.send_otp()

            return redirect('/login')
        else:
            return render(request, 'signup.html')

    except Exception as ex:
        return HttpResponse(str(ex))


@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = request.POST.get('otp')

        try:
            user = CustomUser.objects.get(email=email)
            if user.verify_otp(otp):
                return render(request, 'search.html')
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid OTP'})
        except CustomUser.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Invalid email'})

    else:
        return render(request, 'login.html')

@csrf_exempt   
def oldUserLogin(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email') if request.POST.get('email') else None

            user = CustomUser.objects.create_user(email=email)
            user.send_otp()

            return redirect('/login')
        else:
            return render(request, 'oldUserLogin.html')

    except Exception as ex:
        return HttpResponse(str(ex))

@login_required
def search(request):
    return render(request, 'search.html')

def autosuggest(request):
    query = request.GET.get('query', '')  # Get the query from the request
    
    # Fetch the relevant data from the models based on the query
    cities = City.objects.filter(name__icontains=query)
    countries = Country.objects.filter(name__icontains=query)
    languages = CountryLanguage.objects.filter(language__icontains=query)
    
    context = {
        'query': query,
        'cities': cities,
        'countries': countries,
        'languages': languages
    }
    return render(request, 'autosuggest.html', context)

def logout_view(request):
    logout(request)
    return redirect('/login')
  