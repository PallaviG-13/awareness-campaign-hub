from django.shortcuts import render, redirect, get_object_or_404
from .models import Campaign
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.

def home(request):
    campaigns = Campaign.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'campaigns': campaigns})

def campaign_detail(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    return render(request, 'campaign_detail.html', {'campaign': campaign})

@login_required
def create_campaign(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        Campaign.objects.create(
            title=title,
            description=desc,
            category=category,
            image=image,
            created_by=request.user
        )
        return redirect('home')

    return render(request, 'create_campaign.html')

@login_required
def join_campaign(request, id):
    campaign = get_object_or_404(Campaign, id=id)
    campaign.participants.add(request.user)
    return redirect('campaign_detail', id=id)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})