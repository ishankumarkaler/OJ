from django.db import models


class Problem(models.Model):
    name = models.TextField()
    problemStatement = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name

class User(models.Model):
    userName = models.TextField()

    def __str__(self):
        return self.userName
class Submission(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verdict = models.TextField(blank=True)
    submitTime = models.DateTimeField(auto_now=True)
    code = models.TextField()
    
    def __str__(self):
        return self.verdict

class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    # caseNumber = models.IntegerField()
    input = models.TextField()
    output = models.TextField()
    def __str__(self):
        return self.input