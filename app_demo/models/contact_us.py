from django.db import models


class ContactUs(models.Model):
    """
    Model For Problem
    """
    id = models.BigAutoField(primary_key=True)
    subject = models.CharField(max_length=40)
    message = models.CharField(max_length=40)
    userid = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.userid.username

    class Meta:
        db_table = "contact_us"
