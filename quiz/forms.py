from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.widgets import RadioSelect
from django_countries.fields import CountryField

from quiz.models import User


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect)


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)


class SignUpForm(forms.Form):
    email = forms.EmailField(label='Your email')
    first_name = forms.CharField(label='Your first name')
    last_name = forms.CharField(label='Your last name')
    country = CountryField().formfield()
    city = forms.CharField(label='City')
    address = forms.CharField(label='Your address')
    zip_code = forms.CharField(label='Your postal code')
