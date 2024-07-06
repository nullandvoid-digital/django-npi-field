from django.forms.widgets import TextInput


class NPIWidget(TextInput):
    input_type = "text"

    def __init__(self, is_required, attrs=None):
        self.is_required = is_required
        self.attrs = {
            "pattern": r"\d{10}",
            "title": "A 10-digit NPI number",
            "required": self.is_required,
        }
        super().__init__(attrs)
