from django.contrib import admin
from .models import Problem, Submission, TestCase #,User

admin.site.register(Problem)
# admin.site.register(User)
admin.site.register(Submission)
admin.site.register(TestCase)