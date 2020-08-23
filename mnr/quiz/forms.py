from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class MNRUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class MNRUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)
