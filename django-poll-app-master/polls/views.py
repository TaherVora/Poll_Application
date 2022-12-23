from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

class QuestionListView(ListView):
    model = Question
    template_name = "home.html"
    context_object_name = "questions"

class UserQuestionListView(ListView):
    model = Question
    template_name = "user_questions.html"
    context_object_name = "questions"

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Question.objects.filter(publisher=user).all()

class QuestionDetailView(DetailView):
    model = Question
    template_name = "detail.html"
    context_object_name = "question"

class QuestionResultView(DetailView):
    model = Question
    template_name = "result.html"
    context_object_name = "question"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def about(request):
    context = {
        'title' : "About"
    }
    return render(request,'about.html',context)