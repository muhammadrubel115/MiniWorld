from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from miniaccounts import views 


from django.urls import path
from miniaccounts.views import Register, verify_email

# URL patterns for miniaccounts app
urlpatterns = [
    path('', views.Register, name="register"),
   
    path('verify-email/<uuid:token>/', views.verify_email, name='verify_email'),
    path('forgot_email/', views.ForgotEmail, name="forgot_email"),
    path('forgot_password/', views.ForgotPassword, name="forgot_password"),
    path('forgot_username/', views.ForgotUsername, name="forgot_username"),
    path('forgot_phone_number/', views.ForgotPhoneNumber, name="forgot_phone_number"),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
