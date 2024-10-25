# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact-list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contacts/', views.contact_list, name='contact-list'),
    path('contacts/add/', views.add_contact, name='add-contact'),
    path('contacts/<int:pk>/delete/', views.delete_contact, name='delete-contact'),
    path('todo/', views.todo, name='todo'),
    path('reminders/', views.reminders, name='reminders'),
    path('signup/', views.signup, name='signup'),
    path('settings/', views.settings, name='settings'),
]