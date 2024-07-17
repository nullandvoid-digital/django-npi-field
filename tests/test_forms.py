from django import forms
from tests.test_models import TestPKModel, TestNPIModel


class TestPKForm(forms.ModelForm):
    class Meta:
        model = TestPKModel
        fields = "__all__"


class TestNPIForm(forms.ModelForm):
    class Meta:
        model = TestNPIModel
        fields = "__all__"
