from django.db import models


class UserTemp(models.Model):
    """
    """
    id = models.BigAutoField(primary_key=True)

    email = models.CharField(max_length=64, unique=False)
    verification_code = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "user_temp"
