from django.test import TestCase, SimpleTestCase
from npi_field.validators import npi_validator
from .test_models import TestPKModel, TestNPIModel
from django.core.exceptions import ValidationError

valid = {
    "1710291802": "Fred Astaire",
    "1013969922": "Velma Dinkley",
    "1659731826": "Monty Python",
    "1609389642": "Seymour Butts",
    "1922580133": "Jake Hyde",
}


class TestNPIValidator(SimpleTestCase):

    def test_is_valid_npi(self):
        for npi in valid.keys():
            self.assertIsNone(npi_validator(npi))

    def test_is_invalid_npi(self):
        invalid = {
            "0710291802": "Fred Astaire",
            "1013969923": "Velma Dinkley",
            "165973182634": "Monty Python",
            "16093896": "Seymour Butts",
            "": "Jake Hyde",
        }

        for num in invalid:
            self.assertRaises(ValidationError, npi_validator, num)


class TestModelField(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        for npi, name in valid.items():
            TestPKModel.objects.create(npi=npi, name=name)
            TestNPIModel.objects.create(npi=npi, name=name)

    def test_primary_key_data_saved(self):
        for npi, name in valid.items():
            row = TestPKModel.objects.get(npi=npi)
            self.assertEqual(row.name, name)

    def test_not_primary_key_data_saved(self):
        for npi, name in valid.items():
            row = TestNPIModel.objects.get(npi=npi)
            self.assertEqual(row.name, name)
            self.assertEqual(row.npi, npi)

    def test_blank_allowed(self):
        TestNPIModel.objects.create(npi="", name="Ken Masters")
        row = TestNPIModel.objects.get(npi="")
        self.assertEqual(row.name, "Ken Masters")


class TestFormField(TestCase):
    pass
