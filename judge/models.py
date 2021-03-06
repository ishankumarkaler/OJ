from django.db import models

# class User(models.Model):
#     userName = models.TextField()

#     def __str__(self):
#         return self.userName

class Problem(models.Model):
    name = models.TextField()
    problemStatement = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name

class Submission(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.TextField()
    verdict = models.TextField(default="None")
    submitTime = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.problem.name + "-" + str(self.id) + "-" + str(self.verdict)

class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    # caseNumber = models.IntegerField()
    input = models.TextField()
    output = models.TextField()
    
    def __str__(self):
        return self.problem.name + "-" + str(self.id)