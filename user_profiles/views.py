from django.shortcuts import render


# Profile view
def profile(request):
    """
    A view to return the users profile
    """
    template = 'user_profiles/profile.html'
    context = {

    }

    return render(request, template, context)
