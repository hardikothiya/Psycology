from django.db import models


class ContactUs(models.Model):
    """
    Model For Problem
    """
    id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=40, unique=True)
    message = models.CharField(max_length=40, unique=True)
    username = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username.username

    class Meta:
        db_table = "contact_us"
