from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserSettingsForm


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserSettingsForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your profile has been updated successfully!')
            return redirect('profile_settings')
    else:
        form = UserSettingsForm(instance=request.user)

    return render(request, 'users/settings.html', {'form': form})
