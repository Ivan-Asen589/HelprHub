from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        User = get_user_model()
        
        # Try case-insensitive match for email or username
        try:
            user = User.objects.get(
                Q(email__iexact=email) | Q(username__iexact=email)
            )
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            pass
        except User.MultipleObjectsReturned:
            # If multiple matches, try exact first, then fallback
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    return user
            except User.DoesNotExist:
                try:
                    user = User.objects.get(username=email)
                    if user.check_password(password):
                        return user
                except User.DoesNotExist:
                    pass
        
        return None
