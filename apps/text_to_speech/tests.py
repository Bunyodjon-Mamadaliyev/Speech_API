from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.text_to_speech.models import TTS
from apps.users.models import User

class TTSTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='user@example.com',
            username='user1',
            password='password123'
        )
        self.client.force_authenticate(user=self.user)
        self.convert_url = reverse('tts-convert')

    def test_tts_convert_success(self):
        data = {
            "text": "Hello world",
            "voice": "nova",
            "language": "en",
            "speed": 1.0
        }
        response = self.client.post(self.convert_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", response.data)
        self.assertIn("status", response.data)
        self.assertIn("text", response.data)
        self.assertIn("language", response.data)
        self.assertIn("duration", response.data)
        self.assertIn("file_size", response.data)
        self.assertIn("created_at", response.data)
        self.assertIn("updated_at", response.data)
        self.assertIn("error", response.data)
        self.assertIn("audio_url", response.data)

    def test_tts_detail(self):
        tts = TTS.objects.create(
            status="completed",
            text="hello world",
            voice="nova",
            language="en",
            speed=1.0,
            duration=2.0,
            file_name="tts_1.mp3",
            file_size=204800,
            error=""
        )
        url = reverse('tts-detail', args=[tts.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], tts.id)

    def test_tts_history(self):
        TTS.objects.create(
            status="completed",
            text="hello world",
            voice="nova",
            language="en",
            speed=1.0,
            duration=2.0,
            file_name="tts_1.mp3",
            file_size=204800,
            error=""
        )
        url = reverse('tts-history')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)


    def test_tts_audio_endpoint(self):
        tts = TTS.objects.create(
            status="completed",
            text="hello world",
            voice="nova",
            language="en",
            speed=1.0,
            duration=2.0,
            file_name="tts_1.mp3",
            file_size=204800,
            error=""
        )
        url = reverse('tts-audio', args=[tts.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("audio/mpeg", response.get("Content-Type"))
