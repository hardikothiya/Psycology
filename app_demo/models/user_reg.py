from django.db import models


class User(models.Model):
    """
    """
    GENDER = (
        ('m', 'male'),
        ('f', 'female'),
        ('n', 'non-binary'),
        ('u', 'Prefer Not To Say'),
    )


    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=256, unique=True)
    password = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=64, unique=True, error_messages={'unique': "Email has already been Registered"})
    verification_code = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER, verbose_name="gender", default='m')
    country = models.ForeignKey('country', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='country')
    age = models.IntegerField(max_length=256, blank=True, null=True)
    height = models.FloatField(max_length=256, blank=True, null=True)
    weight = models.FloatField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = "demo_user"
