from django.contrib import admin
from .models import Question


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),  # Date information title
    ]


# create a model admin class, then pass it as the second argument to admin.site.register()
admin.site.register(Question, QuestionAdmin)  # Make the poll app modifiable in the admin¶
