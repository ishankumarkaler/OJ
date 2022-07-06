from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Problem, Submission
from .submissionForm import codeForm
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def displayProblems(request):
    context = {
        'probs' : Problem.objects.all()
    }
    return render(request, 'problemsPage.html', context)

def problemDescriptions(request, prob_id):
    form = codeForm()
    context = {
        'data': Problem.objects.get(id=prob_id),
        'form': form,
    }
    # print(form.is_valid())
    # print(problem.objects.get(id=prob_id).name)
    # print(form.errors.as_data)
    return  render (request, 'problemDescription.html', context)
