from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ View that renders the shopping bag page """

    return render(request, 'bag/bag.html')
