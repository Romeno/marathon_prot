from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_only_one_instance(obj):
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.pk != model.objects.get().pk):
        raise ValidationError(_("Can only create 1 %(model_name)s instance") % {"model_name": model._meta.verbose_name})
