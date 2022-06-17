from django.contrib import admin

from .models import Choice, Question, Response


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']

    search_fields = ['question_text']


class ResponseAdmin(admin.ModelAdmin):
    fields = ('name', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11')

    radio_fields = {'q1': admin.VERTICAL}


admin.site.register(Question, QuestionAdmin)
admin.site.register(Response, ResponseAdmin)
