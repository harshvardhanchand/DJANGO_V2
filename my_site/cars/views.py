from django.shortcuts import render, redirect, reverse

from .forms import ReviewForm
from .forms import reviewForm

# Create your views here.


def rental_view(request):
    # post request ->form contents->thank you
    if request.method == 'POST':
        #form = ReviewForm(request.POST)
        form = reviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('cars:thank_you'))

    # else,render form
    else:
        form = ReviewForm()
    return render(request, 'cars/rental_review.html', context={'form': form})


def thankyou_view(request):
    return render(request, 'cars/thank_you.html')
