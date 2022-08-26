from django.db import models

class problem(models.Model):
    """
    Model For Problem
    """
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "demo_problem"
