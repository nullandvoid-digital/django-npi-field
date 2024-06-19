from django.test import TestCase, SimpleTestCase, override_settings
from ..npi_field.validators import npi_validator
from .test_models import TestPKModel, TestNPIModel
from django.core.exceptions import ValidationError

valid = {
        "1710291802": "Fred Astaire",
        "1013969922": "Velma dinkley",
        "1659731826": "Monty Python",
        "1609389642": "Seymour Butts",
        "1922580133": "Jake Hyde",
}


class TestNPIValidator(SimpleTestCase):

    def test_is_valid_npi(self):
        for npi, name in valid:
            self.assertTrue(npi_validator(npi))

    def test_is_invalid_npi(self):
        invalid = {
            "0710291802": "Fred Astaire",
            "1013969923": "Velma dinkley",
            "165973182634": "Monty Python",
            "16093896": "Seymour Butts",
            "": "Jake Hyde",
        }

        for num, name in invalid:
            self.assertRaises(ValidationError, npi_validator, num)


class TestNPIField(TestCase):

    def setUpTestData(self):
        for npi, name in valid:
            TestPKModel.objects.create(npi="", name=name)
            TestNPIModel.objects.create(npi=npi)

    def test_primary_key_data_saved(self):
        for npi, name in valid:
            row = TestPKModel.objects.get(npi=npi)
            self.assertEqual(row.name, name)

    def test_not_primary_key_data_saved(self):
        for npi, name in valid:
            row = TestNPIModel.objects.create(npi=npi)
            self.assertEqual(row.name, name)
            self.assertEqual(row.npi, npi)

    def test_blank_allowed(self):
        TestNPIModel.objects.create(npi="", name="Ken Masters")
        row = TestNPIModel.objects.get(npi="")
        self.assertEqual(row.name, "Ken Masters")
