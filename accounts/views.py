from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.sites.shortcuts import get_current_site

from accounts.models import UserModel, UserNotificationSettings
from .forms import CreateUserCreationForm
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from .token_generator.token import account_activation_token
from django.core.mail import EmailMessage  




# Create your views here.
def loginPage(request):

    if request.user.is_authenticated:
        return redirect('app_main:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request=request, username=username, password=password)

            if user is not None:
                login(request, user = user)
                return redirect('app_main:index')
            else:
                messages.error(request, 'User Auth Failed')
                return render(request, 'auth/login.html')

        return render(request, 'auth/login.html')

def signup(request):

    form = CreateUserCreationForm()

    if request.user.is_authenticated:
        return redirect('app_main:index')
    else:        
        if request.method == 'POST':
            form = CreateUserCreationForm(request.POST)

            if form.is_valid():
                form.save()     # Save the user is database
                user:UserModel = form.save(commit=False) # save data in memory without saving it in database

                current_site = get_current_site(request)

                mail_subject = 'Activation link has been sent to your email id'  
                message = render_to_string('auth/email_temp.html', {  
                    'user': user,  
                    'domain': current_site.domain,  
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                    'token':account_activation_token.make_token(user),  
                })  
                to_email = form.cleaned_data.get('email')  

                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                    
                messages.success(request, 'Account for User '+form.cleaned_data['username']+' created')
            
                return redirect('accounts:login')
        context = {'form' : form,}
        return render(request, 'auth/signup.html', context=context)


def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('accounts:login')
    else:
        messages.error(request, 'User is not authenticated')
        return redirect('app_main:index')

# Send E-mail verification mail
def send_mail(request, uidb64, token):
    user_model = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = user_model.objects.get(pk=uid)

        if user is not None:
            
            if account_activation_token.check_token(user, token):
              
                user.email_verification = True
                user.save()

                return HttpResponse("The User _ email is confirmed !")
        
            else:
                return HttpResponse(" Not confirmed")
        
    except Exception as e:
        print("Except")
        user = None


# Get Profile and settings of the account.
def user_profile(request):
    if request.user.is_authenticated:
        
        user_settings_form = UserNotificationSettings(request.GET)
        
        if request.method == 'POST':
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')

            # update the details of the user.
            UserModel.objects.filter(username=request.user.username).update(first_name=first_name, last_name=last_name, email=email)
            
        context = {
            'user_settings' : user_settings_form, 
        }

        return render(request, 'profile.html', context)
    else:
        return redirect('accounts:login')
