from django.shortcuts import render
from django.http import HttpResponse
from .models import Memory
from random import choice


def index(request):
    """
    The home view should show lovely pictures with sounds playing under them

    """
    memory = choice(Memory.objects.all())

    context = {
        'memory': memory
    }
    return render(request, 'memories/memory.html', context=context)
