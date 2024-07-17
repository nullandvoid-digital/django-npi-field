from django.test import TestCase, SimpleTestCase
from npi_field.validators import npi_validator
from tests.test_models import TestPKModel, TestNPIModel
from tests.test_forms import TestPKForm, TestNPIForm
from django.core.exceptions import ValidationError

valid = {
    "1710291802": "Fred Astaire",
    "1013969922": "Velma Dinkley",
    "1659731826": "Monty Python",
    "1609389642": "Seymour Butts",
    "1922580133": "Jake Hyde",
}

invalid = {
    "0710291802": "Fred Astaire",
    "1013969923": "Velma Dinkley",
    "165973182634": "Monty Python",
    "16093896": "Seymour Butts",
    "": "Jake Hyde",
}


class TestNPIValidator(SimpleTestCase):

    def test_is_valid_npi(self):
        for npi in valid.keys():
            self.assertIsNone(npi_validator(npi))

    def test_is_invalid_npi(self):
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

    def test_invalid_primary_key_data_error(self):
        for npi, name in invalid.items():
            create = TestPKModel.objects.create(npi=npi, name=name)
            with self.assertRaises(ValidationError):
                create.full_clean()

    def test_invalid_not_primary_key_data_error(self):
        for npi, name in invalid.items():
            if not npi:
                pass
            else:
                create = TestNPIModel.objects.create(npi=npi, name=name)
                with self.assertRaises(ValidationError):
                    create.full_clean()

    def test_blank_allowed(self):
        TestNPIModel.objects.create(npi="", name="Ken Masters")
        row = TestNPIModel.objects.get(npi="")
        self.assertEqual(row.name, "Ken Masters")


class TestFormField(TestCase):
    def test_empty_pk_form(self):
        form = TestPKForm()
        self.assertInHTML(
            r'<input type="text" name="npi" pattern="\d{10}" title="A 10-digit NPI number" required maxlength="10" '
            r'id="id_npi">',
            str(form),
        )

    def test_empty_npi_form(self):
        form = TestNPIForm()
        self.assertInHTML(
            r'<input type="text" name="npi" pattern="\d{10}" title="A 10-digit NPI number" maxlength="10" id="id_npi">',
            str(form),
        )

    def test_pk_data_is_valid(self):
        for npi, name in valid.items():
            data = {"npi": npi, "name": name}
            form = TestPKForm(data)
            self.assertTrue(form.is_valid())

    def test_not_pk_data_is_valid(self):
        for npi, name in valid.items():
            data = {"npi": npi, "name": name}
            form = TestNPIForm(data)
            self.assertTrue(form.is_valid())

    def test_pk_data_is_not_valid(self):
        for npi, name in invalid.items():
            data = {"npi": npi, "name": name}
            form = TestPKForm(data)
            self.assertFalse(form.is_valid())

    def test_not_pk_data_is_not_valid(self):
        for npi, name in invalid.items():
            if not npi:
                pass
            else:
                data = {"npi": npi, "name": name}
                form = TestNPIForm(data)
                self.assertFalse(form.is_valid())
