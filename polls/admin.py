from django.contrib import admin
from .models import Choice, Question


# Register your models here.
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


#  “Choice objects are edited on the Question admin page. By default, provide enough fields for 3 choices.”

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),  # Date information title
    ]
    inlines = [ChoiceInline]


# create a model admin class, then pass it as the second argument to admin.site.register()
admin.site.register(Question, QuestionAdmin)  # Make the poll app modifiable in the admin¶
