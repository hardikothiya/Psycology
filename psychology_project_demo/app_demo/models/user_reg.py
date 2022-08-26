from django.db import models

class User(models.Model):
    """
    """
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=210, unique=True, error_messages={'unique': "UserName is already exists",
                                                                             'required': 'UserName is required'
                                                                             })
    password = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000, blank=True, null=True)
    phone = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=64, unique=True, error_messages={'unique': "Email has already been Registered"})
    verification_code = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey('country', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='country')

    def __str__(self):
        return self.username

    class Meta:
        db_table = "demo_user"