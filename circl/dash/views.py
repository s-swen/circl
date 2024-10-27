# views.py
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

@login_required
def dashboard(request):
    return render(request, 'dash/dashboard.html')

@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user.profile)
    return render(request, 'dash/contact_list.html', {'contacts': contacts})

@login_required
def add_contact_detail(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user.profile
            contact.save()
            return redirect('contact-detail', pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, 'dash/add_contact_detail.html', {'form': form})

@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user.profile)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact-detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'dash/contact_detail.html', {'form': form, 'contact': contact})

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

# dash/views.py
@login_required
def settings(request):
    return render(request, 'dash/settings.html')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('contact-list')
    return render(request, 'dash/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('contact-list')
    else:
        form = UserCreationForm()
    return render(request, 'dash/signup.html', {'form': form})

