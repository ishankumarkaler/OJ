from multiprocessing import context
from django.shortcuts import render, get_object_or_404
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
    return  render (request, 'problemDescription.html', context)

def submit(request, prob_id):
    obj = get_object_or_404(Problem, id = prob_id)
    if request.method == 'POST':
        form = codeForm(request.POST)
        if (form.is_valid()):
            sub = form.save()
            sub.problem = obj
            sub.save()