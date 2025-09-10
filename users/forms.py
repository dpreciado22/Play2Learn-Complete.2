from datetime import datetime
from PIL import Image

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm


MAX_W, MAX_H = 1536, 1536          
MAX_FILE_SIZE_MB = 2              

BIRTH_YEAR_CHOICES = range(1915, datetime.now().year + 1)

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'dob', 'avatar')
        widgets = {
            'dob': forms.SelectDateWidget(
                attrs={'style': 'width: 31%; display: inline-block; margin: 0 1%'},
                years=BIRTH_YEAR_CHOICES,
            ),
            'avatar': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }

    def clean_avatar(self):
        avatar = self.cleaned_data.get('avatar')
        if not avatar:
            return avatar 

        try:
            avatar.file.seek(0)
            with Image.open(avatar.file) as img:
                width, height = img.size
        except Exception:
            raise forms.ValidationError("Please upload a valid image file.")
        finally:
            try:
                avatar.file.seek(0)
            except Exception:
                pass

        if width > MAX_W or height > MAX_H:
            raise forms.ValidationError(
                f"Avatar is {width}×{height}px; max allowed is {MAX_W}×{MAX_H}px."
            )

        return avatar


