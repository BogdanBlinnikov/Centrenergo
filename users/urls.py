from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.ProfilesListView.as_view(), name='index'),
    path('login/', views.LoginCreateView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.CreateUserView.as_view(), name='registration'),
    path('<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('<int:pk>/edit_profile/', views.ProfileEditView.as_view(), name='edit_profile'),
]
