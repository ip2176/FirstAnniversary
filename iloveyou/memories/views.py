from django.shortcuts import render
from django.http import HttpResponse
from .models import Memory
from random import choice, shuffle, randint


def index(request):
    """
    The home view should show lovely pictures with sounds playing under them

    """
    next_memory = None
    show_link = False

    # Try to get a list of memories
    try:
        memories = Memory.objects.all()
    except TypeError:
        memories = None
        pass

    if memories:

        # We have reached the end of the list, just grab a new memory and start again
        if not any(memory.shown is False for memory in memories):

            # Pull up the link div!
            show_link = True

            # Get all the memories and update their shown fields
            Memory.objects.all().update(shown=False)
            memories = Memory.objects.all()

        for memory in memories:

            # We got a new memory to show, break out
            if not memory.shown:
                next_memory = memory
                break

        # Do one last check to iron out bugs
        if not next_memory:
            show_link = True
            Memory.objects.all().update(shown=False)
            next_memory = Memory.objects.all().first()

        next_memory.shown = True
        next_memory.save()

    context = {
        'memory': next_memory,
        'show_link': show_link
    }
    return render(request, 'memories/memory.html', context=context)
