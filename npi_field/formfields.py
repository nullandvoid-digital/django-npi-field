from django.forms.fields import CharField
from validators import npi_validator
from widgets import NPIWidget
from django.utils.translation import gettext_lazy as _


class NPIField(CharField):
    validators = [npi_validator]
    widget = NPIWidget
    label = _("NPI number")
    help_text = _(
        "Please enter the provider's or facility's National Provider Identifier number"
    )

    def __init__(
        self, widget, validators, help_text, label, required=True, *args, **kwargs
    ):
        self.widget, self.validators, self.help_text, self.label, self.is_required = (
            widget,
            validators,
            help_text,
            label,
            required,
        )
        self.max_length = 10
        self.min_length = 10
        widget.is_required = self.required
        super().__init__(*args, **kwargs)
