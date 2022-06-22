from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import ResponseForm
from polls.libraries.RC import exec as generate_religion
import ast
import re


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

        formData = str(form.data)

        # print(formData)

        formData = formData.split("{")[1]
        formData = formData.split("}")[0]
        formData = "{" + formData + "}"

        # print(formData)

        RCresults = generate_religion(ast.literal_eval(formData))

        formResults = RCresults[0]

        # print(formResults)

        religionList = []

        i = 0
        while i < 6:
            i += 1
            myFormResults = formResults.split("</religion>", 1)[0]
            myFormResults = myFormResults + "</religion>"
            religionName = re.search('<religion>(.*)</religion>', formResults)
            formResults = formResults.replace("<religion>", f"<h2 id=\"{religionName.group(1)}\">", 1)
            formResults = formResults.replace("</religion>", "</h2>", 1)
            # religionList.append(religionName)

        formResults = formResults.replace("\n", "<br />")
        # formResults = formResults.replace("--------", "")
        formResults = formResults.replace("<br /><br />", "")
        formResults = formResults.replace("<pros>", "<h3>")
        formResults = formResults.replace("</pros><br />", "</h3>")
        formResults = formResults.replace("<cons>", "<h3>")
        formResults = formResults.replace("</cons><br />", "</h3>")
        formResults = formResults.replace("-<answers>", "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp-&nbsp")
        formResults = formResults.replace("</answers>", "")
        formResults = formResults.replace("<questions>", "")
        formResults = formResults.replace("</questions>", "")

        # religion1 = religionList[0]
        # religion2 = religionList[1]
        # religion3 = religionList[2]
        # religion4 = religionList[3]
        # religion5 = religionList[4]
        # religion6 = religionList[5]
        # religion7 = religionList[6]

        # print(formResults)

        # form.save()
        # return render(request, 'polls/result.html', {'results': formResults, 'selectedReligion': RCresults[1][0], 'religion1': religion1, 'religion2': religion2, 'religion3': religion3, 'religion4': religion4, 'religion5': religion5, 'religion6': religion6, 'religion7': religion7})
        return render(request, 'polls/result.html', {'results': formResults, 'selectedReligion': RCresults[1]})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ResponseForm()

    return render(request, 'polls/detail.html', {'form': form})

def results(request):
    return render(request, 'polls/result.html', {})
