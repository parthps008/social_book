from django.urls import path
from .views import signup_view, login_view, home_view, upload_books_view, uploaded_files_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', home_view, name='home'),
    path('upload_books/', upload_books_view, name='upload_books'),
    path('uploaded_files/', uploaded_files_view, name='uploaded_files'),
]