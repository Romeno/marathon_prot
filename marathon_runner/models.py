from django.db import models
from marathon_common.models import Marathon, MarathonRoute
from django.utils.translation import gettext_lazy as _
import copy


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
    first_name = models.CharField(max_length=1024, verbose_name=_("First name"))
    last_name = models.TextField(max_length=1024, verbose_name=_("Last name"))
    age = models.PositiveIntegerField(verbose_name=_("Age"))
    birthday = models.DateField(verbose_name=_("Birthday"))
    gender = models.CharField(choices=GENDER, max_length=1, verbose_name=_("Gender"))
    email = models.EmailField(max_length=1024, verbose_name=_("Email"))
    citizenship = models.CharField(max_length=1024, verbose_name=_("Citizenship"))
    phone = models.CharField(max_length=32, verbose_name=_("Phone number"))
    user_register_date = models.DateField(verbose_name=_("Registration date"))
    second_phone = models.CharField(blank=True, max_length=50, verbose_name=_("Second phone"))
    city = models.CharField(max_length=1024, verbose_name=_("City"))
    emergency_contact = models.CharField(max_length=1024, verbose_name=_("Emergency contact name"))
    emergency_phone = models.CharField(max_length=32, verbose_name=_("Emergency contact phone"))
    t_shirt_size = models.CharField(blank=True, max_length=8, verbose_name=_("T-shirt size"))
    running_club = models.CharField(max_length=1024, verbose_name=_("Running club"))
    is_disabled = models.NullBooleanField(blank=True, verbose_name=_("Is runner a disabled person"))
    is_prof = models.NullBooleanField(blank=True, verbose_name=_("Is runner a professional sportsman"))
    is_child = models.BooleanField(verbose_name=_("Is runner a child"))
    is_elite = models.BooleanField(verbose_name=_("Is runner an elite sportsman"))
    marathon_registration_datetime = models.DateTimeField(verbose_name=_("Registration time"))
    marathon = models.ForeignKey(Marathon, models.DO_NOTHING, verbose_name=_("Marathon in which runner participates"))
    route = models.ForeignKey(MarathonRoute, models.DO_NOTHING, verbose_name=_("Route which runner will run on"))
    cluster_run_letter = models.CharField(max_length=10, verbose_name=_("Run cluster letter"))
    runner_number = models.IntegerField(verbose_name=_("Runner number"))

    is_active = models.BooleanField(verbose_name=_("Is active"))

    @classmethod
    def from_list(cls, runner):
        runner_copy = copy.copy(runner)
        runner_copy[21] = Marathon.objects.get(is_active=True, name=runner_copy[21])
        runner_copy[22] = MarathonRoute.objects.get(is_active=True, name=runner_copy[22])
        # return cls(None, *runner_copy, is_active=True)
        return cls(id_external=runner_copy[0],
                    first_name=runner_copy[1],
                    last_name=runner_copy[2],
                    age=runner_copy[3],
                    birthday=runner_copy[4],
                    gender=runner_copy[5],
                    email=runner_copy[6],
                    citizenship=runner_copy[7],
                    phone=runner_copy[8],
                    user_register_date=runner_copy[9],
                    second_phone=runner_copy[10],
                    city=runner_copy[11],
                    emergency_contact=runner_copy[12],
                    emergency_phone=runner_copy[13],
                    t_shirt_size=runner_copy[14],
                    running_club=runner_copy[15],
                    is_disabled=runner_copy[16],
                    is_prof=runner_copy[17],
                    is_child=runner_copy[18],
                    is_elite=runner_copy[19],
                    marathon_registration_datetime=runner_copy[20],
                    marathon=runner_copy[21],
                    route=runner_copy[22],
                    cluster_run_letter=runner_copy[23],
                    runner_number=runner_copy[24],
                    is_active=True)
