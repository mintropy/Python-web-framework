from django.db import models

# Create your models here.
class snsUser(models.Model):
    username = models.CharField(max_length=10)
    friend = models.ManyToManyField(
        'self',
        symmetrical=True,
        blank=True,
    )


class Request(models.Model):
    from_user = models.ForeignKey(
        snsUser,
        on_delete=models.CASCADE,
        related_name='requset_from_user',
    )
    to_user = models.ForeignKey(
        snsUser,
        on_delete=models.CASCADE,
        related_name='request_to_user',
    )
