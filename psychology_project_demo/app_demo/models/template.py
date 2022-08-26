from django.db import models

class TemplateMail(models.Model):
    """
    Model For Problem
    """
    id = models.BigAutoField(primary_key=True)
    templatetype = models.CharField(max_length=40, unique=True)
    templatevalue = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.templatetype

    class Meta:
        db_table = "demo_mail_template"
