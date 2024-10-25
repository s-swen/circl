# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact, Profile
from .forms import ContactForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

@login_required
def dashboard(request):
    return render(request, 'dash/dashboard.html')

@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user.profile)
    return render(request, 'dash/contact_list.html', {'contacts': contacts})

@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user.profile
            contact.save()
            return redirect('contact-list')
    return redirect('contact-list')

@login_required
def delete_contact(request, pk):
    if request.method == 'POST':
        contact = Contact.objects.get(pk=pk, user=request.user.profile)
        contact.delete()
    return redirect('contact-list')

@login_required
def todo(request):
    return render(request, 'dash/todo.html')

@login_required
def reminders(request):
    return render(request, 'dash/reminders.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Create a profile for the new user
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'dash/signup.html', {'form': form})

# dash/views.py
@login_required
def settings(request):
    return render(request, 'dash/settings.html')