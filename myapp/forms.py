from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


from .models import ContactUs

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']

    # اعتبارسنجی برای فیلد name
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise ValidationError("نام نمی‌تواند خالی باشد.")
        if len(name) < 3:
            raise ValidationError("نام باید حداقل 3 کاراکتر داشته باشد.")
        return name

    # اعتبارسنجی برای فیلد email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise ValidationError("ایمیل نمی‌تواند خالی باشد.")
        if len(email) < 5:
            raise ValidationError("ایمیل وارد شده معتبر نیست.")
        # استفاده از EmailValidator برای بررسی فرمت ایمیل
        validator = EmailValidator()
        try:
            validator(email)  # بررسی فرمت ایمیل
        except ValidationError:
            raise ValidationError("آدرس ایمیل وارد شده معتبر نیست.")
        return email

    # اعتبارسنجی برای فیلد message
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if not message:
            raise ValidationError("پیام نمی‌تواند خالی باشد.")
        if len(message) < 10:
            raise ValidationError("پیام باید حداقل 10 کاراکتر داشته باشد.")
        return message






User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "example@email.com",
                "autocomplete": "email",
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )
