# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.ContactListView.as_view(), name='contact-list'),
    path('contacts/add/', views.add_contact, name='add-contact'),
    path('contacts/<int:pk>/delete/', views.delete_contact, name='delete-contact'),
    path('todo/', views.todo, name='todo'),
    path('reminders/', views.reminders, name='reminders'),
]