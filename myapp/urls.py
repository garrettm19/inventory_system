from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('weapon_list', views.weapon_list, name='weapon_list'),
    path('user-autocomplete/', views.UserAutocomplete.as_view(), name='user-autocomplete'),
    path('weapon-autocomplete/', views.WeaponAutocomplete.as_view(), name='weapon-autocomplete'),

]
