from django.db.models import CharField
from .validators import npi_validator
from django.utils.translation import gettext_lazy as _
import formfields


class NPIField(CharField):
    default_validators = [npi_validator]
    default_error_messages = {
        "invalid": _("Input must be a valid NPI number"),
    }

    description = _("National Provider Identifier(NPI) number")

    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 10
        kwargs["validators"] = [npi_validator]
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        """Checks if engine is postgres and, if so, returns name of custom domain."""
        if connection.vendor == "postgresql":
            return "NPI"
        else:
            return super().db_type(connection)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs

    def formfield(self, **kwargs):
        defaults = {
            "form_class": formfields.NPIField,
            "error_messages": "",
        }
        defaults.update(kwargs)
        return super(NPIField, self).formfield(**defaults)
