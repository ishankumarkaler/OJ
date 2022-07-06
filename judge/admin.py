from django.contrib import admin
from .models import Problem, User, Submission, TestCase

admin.site.register(Problem)
admin.site.register(User)
admin.site.register(Submission)
admin.site.register(TestCase)