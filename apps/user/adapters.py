from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        if commit:
            user.save()
        return user


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """Conecta contas sociais com usuários existentes pelo email"""
        if sociallogin.is_existing:
            return

        try:
            email = sociallogin.account.extra_data.get('email', '').lower()
            if email:
                from apps.user.models import User
                user = User.objects.get(email=email)
                sociallogin.connect(request, user)
        except User.DoesNotExist:
            pass
    
    def populate_user(self, request, sociallogin, data):
        """Popula dados do usuário a partir do provider social"""
        user = super().populate_user(request, sociallogin, data)
        
        if not user.avatar:
            if sociallogin.account.provider == 'google':
                user.avatar = data.get('picture', '')
            elif sociallogin.account.provider == 'facebook':
                picture_data = data.get('picture', {})
                if isinstance(picture_data, dict):
                    user.avatar = picture_data.get('data', {}).get('url', '')
        
        return user