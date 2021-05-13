import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # question_text, pub_date: database column name, machine friendly
    # 'date published': human-readable name for documentation

    # Give the Question a couple of Choices. The create call constructs a new
    # Choice object, does the INSERT statement, adds the choice to the set
    # of available choices and returns the new Choice object. Django creates
    # a set to hold the "other side" of a ForeignKey relation

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)


# Each model has a number of class variables, each of which represents a database field in the model.
# By running makemigrations, you’re telling Django that you’ve made some changes to your models
# (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

# The sqlmigrate command doesn’t actually run the migration on your database
# - instead, it prints it to the screen so that you can see what SQL Django thinks is required.


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # set the default value of votes to 0.
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
