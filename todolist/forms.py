from django import forms
from .models import Todo, Info, Team


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'completed']


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = "__all__"

        widgets = {
            'username': forms.TextInput(attrs={'class': 'username_form', 'placeholder': 'Введите имя'}),
            'password': forms.PasswordInput(attrs={'class': 'password_form', 'placeholder': 'Введите пароль'}),
            'email': forms.TextInput(attrs={'class': 'email_form', 'placeholder': 'Введите свой емейл не обязательно'})
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'team_name', 'placeholder': 'Введите имя'}),
            'surname': forms.TextInput(attrs={'class': 'team_surname', 'placeholder': 'Введите фамилию'}),
            'email': forms.TextInput(attrs={'class': 'team_email', 'placeholder': 'Введите емейл'})
        }

        