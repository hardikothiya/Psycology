from django.db import models


class Mood(models.Model):
    """
    Model For Problem
    """
    MOODS = (
        (1, 'sorrow'),
        (2, 'sad'),
        (3, 'fine'),
        (4, 'happy'),
        (5, 'exicted'),
    )

    id = models.BigAutoField(primary_key=True)
    mood = models.IntegerField(choices=MOODS, default=3, max_length=40)
    userid = models.ForeignKey('User', on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.userid.username

    class Meta:
        db_table = "mood_table"
