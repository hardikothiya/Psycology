from django.db import models

class question(models.Model):
    """
    Model For Problem
    """
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)
    problem_answer = models.CharField(max_length=40, unique=True)
    problem = models.ForeignKey('problem', on_delete=models.CASCADE, blank=True, null=True)
    problem_level = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "demo_problem"
