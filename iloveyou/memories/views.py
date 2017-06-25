from django.shortcuts import render
from django.http import HttpResponse
from .models import Memory
from random import choice, shuffle, randint


def index(request):
    """
    The home view should show lovely pictures with sounds playing under them

    """
    next_memory = None

    # Try to get a shuffled list of memories
    try:
        memories = list(Memory.objects.all())
        shuffle(memories)
    except TypeError:
        memories = None
        pass

    if memories:

        # We have reached the end of the list, just grab a new memory and start again
        if not any(memory.shown is False for memory in memories):

            # Get all the memories and update their shown fields
            Memory.objects.all().update(shown=False)
            memories = list(Memory.objects.all())
            shuffle(memories)

        for memory in memories:

            # We got a new memory to show, break out
            if not memory.shown:
                next_memory = memory
                break

        # Do one last check to iron out bugs
        if not next_memory:
            Memory.objects.all().update(shown=False)
            next_memory = memories[0]

        next_memory.shown = True
        next_memory.save()

    context = {
        'memory': next_memory
    }
    return render(request, 'memories/memory.html', context=context)
