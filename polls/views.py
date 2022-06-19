from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import ResponseForm

from polls.libraries.RC import exec as generate_religion


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ResponseForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        print(form.data)
        print(generate_religion(form.data)[0])

        # form.save()
        return HttpResponseRedirect('results/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ResponseForm()

    return render(request, 'polls/detail.html', {'form': form})

def results(request):
    pass
