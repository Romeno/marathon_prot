from django.db import models
from marathon_common.models import Marathon, MarathonRoute


class MarathonRunner(models.Model):
    class Meta:
        db_table = 'marathon_runner'

    id = models.BigAutoField(primary_key=True)

    id_external = models.BigIntegerField()
    first_name = models.TextField()
    last_name = models.TextField()
    age = models.IntegerField()
    birthday = models.DateField()
    sex = models.BooleanField()
    email = models.TextField()
    citizenship = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    registration_date = models.DateField(blank=True, null=True)
    second_phone = models.TextField(blank=True, null=True)
    city = models.TextField()
    emergency_contact = models.TextField()
    emergency_phone = models.TextField()
    t_shirt_size = models.CharField(max_length=20, blank=True, null=True)
    running_club = models.TextField(blank=True, null=True)
    is_disabled = models.BooleanField()
    is_prof = models.BooleanField()
    is_child = models.BooleanField()
    is_elite = models.BooleanField()
    registration_time = models.DateTimeField(blank=True, null=True)
    marathon = models.ForeignKey(Marathon, models.DO_NOTHING, blank=True, null=True)
    route = models.ForeignKey(MarathonRoute, models.DO_NOTHING, blank=True, null=True)
    cluster_run_letter = models.TextField(blank=True, null=True)
    number_runner = models.IntegerField(blank=True, null=True)

    is_active = models.BooleanField(verbose_name=_("Is active"))

