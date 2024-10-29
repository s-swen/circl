# dash/views.py
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
    category_choices = Contact.CATEGORY_CHOICES
    return render(request, 'dash/contact_list.html', {'contacts': contacts, 'category_choices': category_choices})

@login_required
def edit_contact(request, pk=None):
    if pk:
        contact = get_object_or_404(Contact, pk=pk, user=request.user.profile)
    else:
        contact = None

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            if not contact.pk:
                contact.user = request.user.profile
            contact.save()
            return redirect('contact-detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)

    return render(request, 'dash/edit_contact.html', {'form': form, 'contact': contact})

@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user.profile)
    return render(request, 'dash/contact_detail.html', {'contact': contact})


@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk, user=request.user.profile)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact-list')
    return render(request, 'dash/delete_contact.html', {'contact': contact})
    
@login_required
def todo(request):
    return render(request, 'dash/todo.html')

@login_required
def reminders(request):
    return render(request, 'dash/reminders.html')

@login_required
def settings(request):
    return render(request, 'dash/settings.html')

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

@login_required
def category_contacts(request, category):
    contacts = Contact.objects.filter(user=request.user.profile, category=category)
    category_name = dict(Contact.CATEGORY_CHOICES)[category]
    return render(request, 'dash/category_contacts.html', {'contacts': contacts, 'category_name': category_name})