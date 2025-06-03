# 🗣️ Speech-to-Text & Text-to-Speech API

Bu loyiha DRF (Django Rest Framework), OpenAI Whisper modeli va OpenAI TTS API yordamida yaratilgan STT va TTS funksiyalarini o‘z ichiga oladi. Foydalanuvchilar matnni nutqqa va nutqni matnga aylantirish imkoniyatiga ega.

---

## 📄 Swagger va Redoc

- Swagger: [`/swagger/`](http://localhost:8000/swagger/)
- Redoc: [`/redoc/`](http://localhost:8000/redoc/)

---

## 📦 Texnologiyalar

- Django & Django Rest Framework
- PostgreSQL
- Celery & Redis
- OpenAI Whisper (STT)
- OpenAI TTS (Text to Speech)
- drf-yasg (Swagger)
- Docker (optional)

---

## 🔐 Authentication

| Method | Endpoint                   | Tavsif                    |
|--------|----------------------------|---------------------------|
| POST   | `/api/auth/register/`      | 👤 Ro‘yxatdan o‘tish      |
| POST   | `/api/auth/login/`         | 🔐 Login qilish           |
| POST   | `/api/auth/token/refresh/` | 🔐 Tokenni refresh qilish |
---
## 🗣️ Speech-to-Text (STT)

| Method | Endpoint             | Tavsif                 |
|--------|----------------------|------------------------|
| POST   | `/api/stt/convert/`  | 📜 Barcha STT ro‘yxati |
| GET    | `/api/stt/{id}/`     | 🔍 Bitta STT olish     |
| GET    | `/api/stt/history/`  | 🔍 STT history olish   |
---
## 🔊 Text-to-Speech (TTS)

| Method | Endpoint               | Tavsif                                |
|--------|------------------------|---------------------------------------|
| POST   | `/api/tts/convert/`    | 📜 Barcha TTS ro‘yxati                |
| GET    | `/api/tts/{id}/`       | 🔍 Bitta TTS olish                    |
| GET    | `/api/tts/{id}/audio/` | 🎙️ Barcha sintezlangan audio fayllari |
| GET    | `/api/tts/history/`    | 🔍 TTS history olish                  |
---
## 👤 User Profil

| Method | Endpoint                  | Tavsif                        |
|--------|---------------------------|-------------------------------|
| GET    | `/api/auth/user/profile/` | 🙍 Foydalanuvchi profili      |
---
## 📦 OTP & SMS Integratsiya

Loyihada foydalanuvchini ro‘yxatdan o‘tkazishda telefon raqamiga OTP (bir martalik parol) yuboriladi. Bu quyidagi texnologiyalar yordamida amalga oshiriladi:

- 📲 SMS Service API
- 🧵 Celery (fon ishlar uchun)
- 📡 Redis (broker sifatida)
---

## ⚙️ O‘rnatish

```bash
# Virtual environment yaratish
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Kutubxonalarni o‘rnatish
pip install -r requirements/development.txt    

# Migratsiyalar
python manage.py migrate

# Serverni ishga tushurish
python manage.py runserver
```

---

## 🧠 Manbalar

- [OpenAI Whisper (STT)](https://github.com/openai/whisper)
- [OpenAI TTS API](https://platform.openai.com/docs/guides/text-to-speech)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [Redis](https://redis.io/)
- [drf-yasg - Swagger](https://github.com/axnsan12/drf-yasg)

---

## 📎 Loyiha havolasi

📂 `GitHub repo:` [your-repo-link](https://github.com/Bunyodjon-Mamadaliyev/Speech_API.git)

---

🚀 Dastur to‘liq testdan o‘tkazilgan va ishlab chiqarishga tayyor!
