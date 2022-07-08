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
    print(output)
    print(correct_ouput)
    if len(output) != len(correct_ouput):
        print("first")
        return False
    for i in range(len(output)):
        if list(filter(None, output[i].split(' '))) != \
            list(filter(None, correct_ouput[i].split(' '))):
            print("second")
            print(list(output[i].split(' ')))
            print(list(correct_ouput[i].split(' ')))
            return False
    return True

def evaluate(submission):
	with open("sol.cpp", "w") as f:
		f.write(submission.code)
	cmd =['g++ sol.cpp']
	test_case = get_object_or_404(TestCase, problem = submission.problem)
	f_input = test_case.input
	print(input)
	res = ""
	try:
		res = subprocess.run(cmd, capture_output = True, shell = True, check = True, timeout=3)
	except subprocess.CalledProcessError:
		print("CE")
		submission.verdict = "CE"
		submission.save()
		return
	submission.verdict = "Compiled"
	submission.save()
	if sys.platform == 'linux':
		cmd = ['./a.out']
	else:
		cmd = ['a.exe']
	try:
		output = subprocess.run(cmd, capture_output = True, shell =True, \
				text = True, input = f_input, check = True, timeout = 2)
	except subprocess.TimeoutExpired:
		submission.verdict = "TLE"
		submission.save()
		return
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