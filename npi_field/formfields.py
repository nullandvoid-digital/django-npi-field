from django.forms.fields import CharField
from validators import npi_validator
from widgets import NPIWidget


class NPIField(CharField):
    default_validators = [npi_validator]
    widget = NPIWidget

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
