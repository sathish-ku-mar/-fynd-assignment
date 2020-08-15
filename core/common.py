from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _



mobile_regex = RegexValidator(regex=r'^\d{10,15}$',
                              message=_("Please Enter correct Contact no.")
                             )