from django.forms.widgets import TextInput


class NPIWidget(TextInput):
    input_type = "text"

    def __init__(self, attrs=None, is_required=True):
        self.attrs = {
            "pattern": r"\d{10}",
            "maxlength": 10,
            "minlength": 10,
            "title": "A 10-digit NPI number",
            "required": self.is_required,
        }
        self.is_required = is_required
        super().__init__(attrs)
