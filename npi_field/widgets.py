from django.forms.widgets import TextInput


class NPIWidget(TextInput):
    input_type = "text"

    def __init__(self, attrs=None):
        self.attrs = r"{'pattern':'\d{10}', 'maxlength':10, minlength':10, 'title':'A 10-digit NPI number'}"
        super().__init__(attrs)
