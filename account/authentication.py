from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

User = get_user_model()


class EmailOrPhoneNumberModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the username is a valid email address
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                # If the username is not an email, check if it's a valid phone number
                user = User.objects.get(phone_number=username)
            except User.DoesNotExist:
                # Neither email nor phone number matched, return None
                return None

        if user.check_password(password):
            return user

        return None