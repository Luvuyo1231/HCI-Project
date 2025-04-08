from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
     path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('about/',views.about,name='about'),
    path('logout/', views.logout_view, name='logout'),
      path('book-tutor/', views.book_tutor, name='book_tutor'),
      path('become-tutor/', views.become_tutor, name='become_tutor'),
]