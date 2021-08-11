from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


# Profile view
def profile(request):
    """
    A view to return the users profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)

    template = 'user_profiles/profile.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
