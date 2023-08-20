from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login,logout
from .forms import CustomAuthenticationForm,ForgotPasswordForm,ResetPasswordForm
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.encoding import force_bytes,force_str
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode
# from django.utils.encoding import force_str



User = get_user_model()

def login_view(request):
    form=CustomAuthenticationForm(request.POST or None)
    print("inside login_view",request.method,User)
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        print(user)
        if user:
            print('inside user')
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('first_app:about_us')
    return render(request, 'login.html',{'form':form})



def logout_view(request):
    logout(request)
    return redirect('login')



def forgot_pass(request):
    form=ForgotPasswordForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = request.POST.get('email')
            user = get_user_model().objects.filter(email=email).first()
            print(user)
            if user:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_url = request.build_absolute_uri(reverse('password_reset', args=[uid, token]))
                print(reset_url)
                message = render_to_string('send_email.html', {'reset_url': reset_url})
                print("sending email")
                messages.success(request,"Email sent succesfully")
                send_mail(
                    'Password Reset Request',
                    "nothing just reset password",
                    'ppppppppp1234pp@gmail.com',
                    [email],
                    fail_silently=False,
                    html_message=message
                )
            
            return redirect('forgot_password')

    return render(request,'forgot_password.html',{'form':form})


def main_page(request):
    print("in first page",request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect('first_app:contact_us')
    else:
        return redirect('login')


def password_reset(request,uidb64=None,token=None):
    form=ResetPasswordForm(request.POST or None)
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            new_password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request,"password Reset successfully!!")
                return redirect('login')

    return render(request, 'forgot_password.html',{'form':form})
    

    


 

    
