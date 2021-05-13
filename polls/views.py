from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


# Create your views here.
# To call the view, we need to map it to a URL - and for this we need a URLconf.
# To create a URLconf in the polls directory, create a file called urls.py.


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # for ListView, the automatically generated context variable is question_list.
    # To override this we provide the context_object_name attribute,
    # specifying that we want to use latest_question_list instead

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    # return HttpResponse(f"You're voting on question  {question_id}.")
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST is a dictionary-like object that lets you access submitted data by key name.
        # In this case, request.POST['choice'] returns the ID of the selected choice, as a string.
        # request.POST values are always strings.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # checks for KeyError and redisplays the question form with an error message if choice isn’t given.
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1  # a race condition might occur
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        # The reverse function helps avoid having to hardcode a URL in the view function.
        # It is given the name of the view that we want to pass control to ('polls:results')
        # ,and the variable portion of the URL pattern that points to that view. [args=(question.id,)]
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
