from django.test import TestCase
from .factories import AlertFactory
from .models import Alert

class AlertTests(TestCase):
    def setUp(self):
        self.alert = AlertFactory.create()

    def test_alert_만들기(self):
        self.assertTrue(Alert.objects.exists())
        self.assertEqual(self.alert.title, self.alert.title)

    def test_alert_is_active_활성화(self):
        self.assertTrue(self.alert.is_active)

    def test_alert_user_비어있는지(self):
        self.assertIsNotNone(self.alert.user)

    def test_alert_select_related_검사(self):
        alert = Alert.objects.select_related('user').get(id=self.alert.id)
        self.assertEqual(alert.user.username, self.alert.user.username)
