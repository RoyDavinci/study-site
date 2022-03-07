from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('room/<str:pk>', views.rooms, name="rooms"),
    path('profile/<str:pk>', views.profile_request, name='profile'),
    path('create-room/', views.create_room, name="create-room"),
    path('update-room/<str:pk>', views.update_room, name="update-room"),
    path('update-user/', views.update_user, name="update-user"),
    path('topics/', views.topics_page, name="topics"),
    path('activity/', views.activity_page, name="activity"),
    path('edit-message/<str:pk>', views.edit_message, name="edit-message"),
    path('delete-room/<str:pk>', views.delete_room, name="delete-room"),
    path('delete-message/<str:pk>', views.delete_message, name="delete-message"),
    path('profile/<str:pk>', views.profile_request, name='profile')
]
