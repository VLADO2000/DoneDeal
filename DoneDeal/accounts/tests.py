from django.test import TestCase
from django.contrib.auth import get_user_model

class AccountsTest(TestCase):
    def test_create_account(self):
        Account_model = get_user_model()
        test_account = Account_model.objects.create_user(
                    email='test@example.com', label='TestSRO',
                    password='test', description='TestSRO description'
        )

        self.assertEqual(test_account.email, 'test@example.com')
        self.assertEqual(test_account.label, 'TestSRO')
        self.assertEqual(test_account.description, 'TestSRO description')
        self.assertEqual(test_account.role, 0)
        self.assertTrue(test_account.is_active)
