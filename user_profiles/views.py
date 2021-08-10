from django.shortcuts import render, get_object_or_404
from .models import UserProfile


# Profile view
def profile(request):
    """
    A view to return the users profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'user_profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
