from django.contrib import admin

# from .models import Choice, Question, Response
from .models import Response


class ChoiceInline(admin.TabularInline):
    # model = Choice
    extra = 3


class ResponseAdmin(admin.ModelAdmin):
    fields = ('name', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11')

    radio_fields = {'q1': admin.VERTICAL}


admin.site.register(Response, ResponseAdmin)
