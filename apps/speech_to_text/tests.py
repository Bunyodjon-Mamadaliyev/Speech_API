from io import BytesIO
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.speech_to_text.models import STT
from apps.users.models import User


class STTTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='user@example.com',
            username='user1',
            password='password123'
        )
        self.client.force_authenticate(user=self.user)
        self.convert_url = reverse('stt-convert')

    def test_stt_convert_success(self):
        audio_content = BytesIO(b"fake audio content here")
        audio_content.name = "stt_test.wav"

        data = {
            "audio": audio_content,
            "language": "uz"
        }
        response = self.client.post(self.convert_url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertIn("status", response.data)
        self.assertIn("text", response.data)
        self.assertIn("language", response.data)
        self.assertIn("duration", response.data)
        self.assertIn("file_name", response.data)
        self.assertIn("file_size", response.data)
        self.assertIn("created_at", response.data)
        self.assertIn("updated_at", response.data)
        self.assertIn("error", response.data)

    def test_stt_retrieve(self):
        stt = STT.objects.create(
            status="completed",
            text="hello world",
            language="uz",
            duration=2.0,
            file_name="stt_1.wav",
            file_size=12000,
            error=""
        )
        url = reverse('stt-retrieve', args=[stt.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], stt.id)

    def test_stt_history(self):
        STT.objects.create(
            status="completed",
            text="hello world",
            language="uz",
            duration=2.0,
            file_name="stt_1.wav",
            file_size=12000,
            error=""
        )
        url = reverse('stt-history')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertIsInstance(response.data['results'], list)
