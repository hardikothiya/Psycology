from django.db import models


class User(models.Model):
    """
    """
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=64, unique=True, error_messages={'unique': "Email has already been Registered"})
    verification_code = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey('country', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='country')

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "demo_user"
