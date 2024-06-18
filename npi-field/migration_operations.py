from django.db import migrations, models
from django.db.migrations.operations.base import Operation
from fields import NPIField


class CreateNPIDomain(Operation):
    """Creates custom domain for NPI ONLY ON POSTGRES ENGINE."""
    def state_forwards(self, app_label, state):
        pass

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        if schema_editor.connection.vendor == "postgresql":
            schema_editor.execute("")  # TODO: Create Function
            schema_editor.execute("")  # TODO: Create Domain

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        if schema_editor.connection.vendor == "postgresql":
            schema_editor.execute("")  # TODO: Drop Domain
            schema_editor.execute("")  # TODO: Drop Function

    def describe(self):
        return "Creates a custom NPI Domain with Luhn algorithm validation only on PostgreSQL Engine"

    def migration_name_fragment(self):
        return "create_npi_domain"
