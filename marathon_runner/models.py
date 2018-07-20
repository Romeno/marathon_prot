from django.db import models
from marathon_common.models import Marathon, MarathonRoute
from django.utils.translation import gettext_lazy as _


class MarathonRunner(models.Model):
    class Meta:
        db_table = 'marathon_runner'

    MALE = 'M'
    FEMALE = 'F'
    GENDER = (
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    )

    id = models.BigAutoField(primary_key=True)

    id_external = models.BigIntegerField(verbose_name=_("Id of runner got from client"))
    first_name = models.CharField(max_length=50, verbose_name=_("First name"))
    last_name = models.TextField(max_length=100, verbose_name=_("Last name"))
    age = models.PositiveIntegerField(verbose_name=_("Age"))
    birthday = models.DateField(verbose_name=_("Birthday"))
    gender = models.CharField(choices=GENDER, max_length=1, verbose_name=_("Gender"))
    email = models.EmailField(max_length=256, verbose_name=_("Email"))
    citizenship = models.CharField(max_length=200, verbose_name=_("Citizenship"))
    phone = models.CharField(max_length=50, verbose_name=_("Phone number"))
    user_register_date = models.DateField(verbose_name=_("Registration date"))
    second_phone = models.CharField(max_length=50, verbose_name=_("Second phone"))
    city = models.CharField(max_length=100, verbose_name=_("City"))
    emergency_contact = models.CharField(max_length=150, verbose_name=_("Emergency contact name"))
    emergency_phone = models.CharField(max_length=50, verbose_name=_("Emergency contact phone"))
    t_shirt_size = models.CharField(max_length=20, verbose_name=_("T-shirt size"))
    running_club = models.CharField(max_length=200, verbose_name=_("Running club"))
    is_disabled = models.NullBooleanField(blank=True, verbose_name=_("Is runner a disabled person"))
    is_prof = models.BooleanField(verbose_name=_("Is runner a professional sportsman"))
    is_child = models.BooleanField(verbose_name=_("Is runner a child"))
    is_elite = models.BooleanField(verbose_name=_("Is runner an elite sportsman"))
    marathon_registration_datetime = models.DateTimeField(verbose_name=_("Registration time"))
    marathon = models.ForeignKey(Marathon, models.DO_NOTHING, verbose_name=_("Marathon in which runner participates"))
    route = models.ForeignKey(MarathonRoute, models.DO_NOTHING, verbose_name=_("Route which runner will run on"))
    cluster_run_letter = models.CharField(max_length=10, verbose_name=_("Run cluster letter"))
    runner_number = models.IntegerField(verbose_name=_("Runner number"))

    is_active = models.BooleanField(verbose_name=_("Is active"))

