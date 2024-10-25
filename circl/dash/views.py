# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Contact, Category, Profile
from .forms import ContactForm
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def home(request):
    # Ensure the user has a profile
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    total_contacts = Contact.objects.filter(user=profile).count()
    upcoming_birthdays = Contact.objects.filter(
        user=profile,
        birthday__gte=timezone.now().date(),
        birthday__lte=timezone.now().date() + timedelta(days=30)
    ).order_by('birthday')[:5]
    recent_contacts = Contact.objects.filter(user=profile).order_by('-last_contact')[:5]

    context = {
        'total_contacts': total_contacts,
        'upcoming_birthdays': upcoming_birthdays,
        'recent_contacts': recent_contacts,
    }
    return render(request, 'dash/home.html', context)

# ... (rest of the views remain the same)

class ContactListView(generic.ListView, LoginRequiredMixin):
    model = Contact
    template_name = 'contact_list.html'
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user.profile)

@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user.profile
            contact.save()
            return redirect('contact-list')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})

@login_required
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact-list')
    return render(request, 'delete_contact.html', {'contact': contact})

@login_required
def todo(request):
    return render(request, 'todo.html')

@login_required
def reminders(request):
    return render(request, 'reminders.html')