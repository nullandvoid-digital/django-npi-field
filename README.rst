################
django-npi-field
################

Description
===========
**Django-npi-field** is a Django library which validates and stores 10-digit U.S. `National Provider Identifier (NPI)`_
numbers.

.. _`National Provider Identifier (NPI)`: \
   https://www.cms.gov/Regulations-and-Guidance/Administrative-Simplification/NationalProvIdentStand

Installation
============
From PyPI
---------
Using pip:

.. code-block:: zsh

   pip install django-npi-field

Using poetry:

.. code-block:: zsh

   poetry add django-npi-field

From GitHub
-----------
Using poetry:

.. code-block:: zsh

   poetry add git+https://github.com/PhoenixStorm1015/django-npi-field.git

Usage
=====
Add the app to ``INSTALLED_APPS`` in your ``settings.py`` file.

.. code-block:: python

   INSTALLED_APPS = [
       # Other apps...
       "npi_field",
   ]

Add the field to your ``models.py``.

.. code-block:: python

   from django.db import models
   from npi_field.modelfields import NPIField

   class HealthcareProvider(models.Model):
       npi = NPIField()

If you prefer, you can also call the validator directly and bypass the model field. If you want the length restriction,
make sure to also set the ``max_length`` argument.

.. code-block:: python

   from django.db import models
   from npi_field.validators import npi_validator

   class HealthcareProvider(models.Model):
       npi = models.CharField(max_length=10, validators = [npi_validator])

Implementation
==============
A Luhn algorithm [1]_ implementation validates the NPI number and stores in a standard CharField. This
CharField is automatically restricted to a ``max_length`` of 10 characters to maintain consistency with the NPI
specification.

Currently, this validation is the only thing restricting the input. In the future, this library will have special
integration with PostgreSQL's Custom Domains to do validation in-database. Ideally, there will be checks to keep the
library database agnostic.

.. [1] **NOTE:** This is a Luhn algorithm specially implemented for NPI numbers due to it's shorter length. This \
   validator **WON'T WORK** for other numbers validated by a Luhn algorithm, such as credit/debit card \
   numbers, ISBN numbers, or IMEI numbers.