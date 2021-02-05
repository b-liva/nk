from django.test import TestCase
from recipient.models import Recipient
from core.models import Gender


class PTest(TestCase):
    def setUp(self):
        self.male = Gender.objects.create(gender_type='male', title='male')
        self.recip = Recipient.objects.create(
            gender=self.male,
            first_name='first',
            last_name='last_name',
            is_active=True
        )

    def test_fist_name(self):
        rec = Recipient.objects.last()
        self.assertTrue(rec.first_name, 'first')

    def test_last_name(self):
        rec = Recipient.objects.last()
        self.assertTrue(rec.last_name, 'last_name')
