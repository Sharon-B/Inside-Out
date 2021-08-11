from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm


# Profile view
def profile(request):
    """
    A view to return the users profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated!')

    form = UserProfileForm(instance=profile)

    template = 'user_profiles/profile.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
