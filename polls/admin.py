from django.contrib import admin
from .models import Question


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']  # determines the representation order


# create a model admin class, then pass it as the second argument to admin.site.register()
admin.site.register(Question, QuestionAdmin)  # Make the poll app modifiable in the admin¶
