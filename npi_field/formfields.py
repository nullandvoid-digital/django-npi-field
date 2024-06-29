from django.forms.fields import CharField
from npi_field.validators import npi_validator
from npi_field.widgets import NPIWidget
from django.utils.translation import gettext_lazy as _


class NPIField(CharField):
    default_validators = [npi_validator]
    widget = NPIWidget
    label = _("NPI number")
    default_error_messages = {
        "invalid": _("Input must be a valid NPI number"),
    }
    help_text = _(
        "Please enter the provider's or facility's National Provider Identifier number"
    )
    initial = "1710291802"
    required = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators = (*self.default_validators,)
        self.default_error_messages = self.error_messages
        self.widget.is_required = self.required
        self.max_length = 10
        self.min_length = 10

    def clean(self, *args, **kwargs):
        pass
