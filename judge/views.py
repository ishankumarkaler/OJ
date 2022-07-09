from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Problem, Submission, TestCase
from .submissionForm import codeForm
import os, subprocess, sys

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
        'data': Problem.objects.get(id = prob_id),
        'form': form,
    }
    return  render (request, 'problemDescription.html', context)

def checker(output, correct_ouput):
    output = output.split('\n')
    correct_ouput = correct_ouput.split('\n')
    if len(output) != len(correct_ouput):
        return False
    for i in range(len(output)):
        if list(filter(None, output[i].split(' '))) != \
            list(filter(None, correct_ouput[i].split(' '))):
            return False
    return True

def evaluate(submission):
    with open("sol.cpp", "w") as f:
        f.write(submission.code)
    if sys.platform == 'linux':
        command =['g++ sol.cpp']
    else:
        path_to_code = r'C:\Users\kumar\Documents\OJ'
        command = 'g++ ' + os.path.join(path_to_code, 'sol.cpp')

    # Try code compilation
    try:
        subprocess.run(command, capture_output = True, check = True)
    except subprocess.CalledProcessError:
        submission.verdict = "CE"
        submission.save()
        return
    submission.verdict = "Compiled"
    submission.save()
    if sys.platform == 'linux':
        command = ['./a.out']
    else:
        command = ['a.exe']
    test_case = get_object_or_404(TestCase, problem = submission.problem)
    f_input = test_case.input
    # Try code execution
    try:
        output = subprocess.run(command, capture_output = True, \
                text = True, input = f_input, check = True, timeout = 2)
    except subprocess.TimeoutExpired:
        submission.verdict = "TLE"
        submission.save()
        return
    # Calculate the verdict and save it
    if checker(output.stdout, test_case.output):
        submission.verdict = "AC"
        submission.save()
    else:
        submission.verdict = "WA"
        submission.save()


def submit(request, prob_id):
    obj = get_object_or_404(Problem, id = prob_id)
    if request.method == 'POST':
        form = codeForm(request.POST)
        if (form.is_valid()):
            submission = form.save()
            submission.problem = obj
            submission.save()
            evaluate(submission)
        return redirect('problem_list_page')