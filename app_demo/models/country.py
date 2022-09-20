from django.db import models

class country(models.Model):
    """
    Model For Country
    """
    sortname = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=40, unique=True)
    phonecode = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "demo_country"
