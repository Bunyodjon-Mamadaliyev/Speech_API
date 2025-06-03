from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            email="test@example.com",
            username="testuser",
            password="securepassword123",
            first_name="Test",
            last_name="User"
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("securepassword123"))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(str(user), "test@example.com")

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(
            email="admin@example.com",
            username="adminuser",
            password="adminpass123"
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)
        self.assertEqual(superuser.email, "admin@example.com")
        self.assertEqual(str(superuser), "admin@example.com")

    def test_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="",
                username="nousername",
                password="somepass"
            )

    def test_user_without_username_raises_error(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email="no_username@example.com",
                username="",
                password="somepass"
            )
