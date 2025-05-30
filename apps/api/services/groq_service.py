from groq import Groq
from django.conf import settings
from ..models import ChatMessage


class GroqService:
    """Service for interacting with Groq API"""

    def __init__(self):
        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def chat_completion(self, session_id, message, model_id="llama-3.1-70b-versatile"):
        """Generate chat completion using Groq API"""

        previous_messages = ChatMessage.objects.filter(
            session_id=session_id
        ).order_by('-created_at')[:10]

        previous_messages = list(reversed(previous_messages))

        user_message = ChatMessage.objects.create(
            session_id=session_id,
            role='user',
            content=message
        )

        messages = previous_messages + [user_message]

        formatted_messages = [
            {"role": msg.role, "content": msg.content}
            for msg in messages
        ]

        try:
            response = self.client.chat.completions.create(
                model=model_id,
                messages=formatted_messages,
                temperature=0.7,
            )

            response_content = response.choices[0].message.content

            assistant_message = ChatMessage.objects.create(
                session_id=session_id,
                role='assistant',
                content=response_content
            )

            return {
                'user_message': user_message,
                'assistant_message': assistant_message
            }

        except Exception as e:
            error_message = str(e)
            print(f"Error in chat completion: {error_message}")

            user_message.delete()

            raise e

    def get_available_models(self):
        """Get available models from Groq"""
        try:
            response = self.client.models.list()

            model_ids = [model.id for model in response.data]

            return model_ids
        except Exception as e:
            print(f"Error fetching Groq models: {e}")
            return [
                "llama-3.1-70b-versatile",
                "llama-3.1-8b-instant",
                "mixtral-8x7b-32768",
                "gemma-7b-it",
            ]