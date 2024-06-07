from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# chatgpt results are here !!!

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# varify email
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import EmailVerification
import uuid


# varification view
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages




# Views for user registration and authentication
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from miniaccounts.models import ProfileInfo
from django.core.mail import send_mail


def Register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        email = email.lower()

        if password != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        try:
            validate_email(email)
        except ValidationError:
            messages.error(request, "Enter a valid email address")
            return redirect('register')

        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('register')
        else:
            # Create user
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.is_active = False  # Deactivate the user until email verification
                user.save()

                # Create profile info
                profile = ProfileInfo.objects.create(user=user)
                profile.save()

                # Send verification email
                send_verification_email(user)

                messages.success(request, "Account created successfully. Please verify your email.")
                return redirect('/')
            except Exception as e:
                messages.error(request, f"Error creating account: {e}")
                return redirect('register')

    return render(request, 'miniaccounts/register.html')


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from miniaccounts.models import ProfileInfo






import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from miniaccounts.models import EmailVerification  # Assuming EmailVerification is a custom model

def send_verification_email(user):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    verification_link = f"http://yourdomain.com/verify-email/{uid}/{token}/"
    
    subject = "Verify your email address"
    message = render_to_string('verification_email.html', {'user': user, 'verification_link': verification_link})
    sender_email = "your@example.com"  # Enter your email address here
    recipient_email = user.email
    
    send_mail(subject, message, sender_email, [recipient_email])

def send_verification_email(user):
    token = uuid.uuid4()
    verification_link = f"http://127.0.0.1:8000/register/verify-email/{token}/"
    send_mail(
        'Verify your email address',
        f'Click the link to verify your email: {verification_link}',
        settings.EMAIL_HOST,
        [user.email],
    )
    EmailVerification.objects.create(user=user, token=token)




def verify_email(request, token):
    try:
        verification = EmailVerification.objects.get(token=token)
    except EmailVerification.DoesNotExist:
        messages.error(request, "Invalid verification token. Please request a new one.")
        return redirect('/')
    
    user = verification.user
    user.is_active = True
    user.save()
    
    verification.delete()
    
    messages.success(request, "Email verified successfully. You can now log in.")
    return redirect('/')



def ForgotEmail(request):
    """Render forgot email page."""
    return render(request, 'miniaccounts/forgot_email.html')


def ForgotPassword(request):
    """Render forgot password page."""
    return render(request, 'miniaccounts/forgot_password.html')


def ForgotUsername(request):
    """Render forgot username page."""
    return render(request, 'miniaccounts/forgot_username.html')


def ForgotPhoneNumber(request):
    """Render forgot phone number page."""
    return render(request, 'miniaccounts/forgot_phone_number.html')
