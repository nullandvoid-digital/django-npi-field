from django.db.migrations.operations.base import Operation
from django.db.migrations.operations.models import CreateModel
from django.db.migrations.writer import MigrationWriter


class CreateNPIDomain(Operation):
    """Creates custom domain for NPI ONLY ON POSTGRES ENGINE."""

    def state_forwards(self, app_label, state):
        pass

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        if schema_editor.connection.vendor == "postgresql":
            schema_editor.execute("")

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        if schema_editor.connection.vendor == "postgresql":
            schema_editor.execute("")  # TODO: Drop Domain
            schema_editor.execute("")  # TODO: Drop Function

    def describe(self):
        return "Creates a custom NPI Domain with Luhn algorithm validation only on PostgreSQL Engine"


class CustomModelCreation(CreateModel):
    pass
