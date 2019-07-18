# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'learn/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[0:5]
#     content = {
#         'latest_question_list': latest_question_list
#     }
#     return render(request, 'learn/index.html', content)
#


class DetailView(generic.DetailView):
    model = Question
    template_name = 'learn/detail.html'
    
    def get_queryset(self):
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        )
#
# def detail(request, question_id):
#     # try:
#     #   question = Question.objects.get_object_or_404(pk=question_id)
#     # except Question.DoesNotExist:
#     #   raise http404('Question does not exist')
#     question = get_object_or_404(Question, pk=question_id)
#     print(question)
#     return render(request, 'learn/detail.html', {'question': question})


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'learn/results.html'
    
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'learn/results.html', {'question': question})


def vote(request, question_id):
    print(question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'learn/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        print(question.id)
        return HttpResponseRedirect(reverse('learn:results', args=(question.id,)))
