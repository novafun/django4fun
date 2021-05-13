from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.template import loader


# Create your views here.
# To call the view, we need to map it to a URL - and for this we need a URLconf.
# To create a URLconf in the polls directory, create a file called urls.py.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    template = loader.get_template('polls/index.html')  # update our index view in polls/views.py to use the template
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request, question_id):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse(f"You're voting on question  {question_id}.")
