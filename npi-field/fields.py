from django.db.models import CharField
from validators import npi_validator
from django.utils.translation import gettext_lazy as _


class NPIField(CharField):

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
