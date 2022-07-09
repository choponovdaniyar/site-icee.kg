from .models import Client

from django.template import loader
from django.conf import settings
from django.core.mail import EmailMessage
from django.forms import ModelForm, TextInput,  Select, Textarea, EmailInput, FileInput, CheckboxInput


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = [
            "first_name", "last_name",
            "academic_title", "academic_status",
            "subject", 
            "face_type", "format", "role",
            "company", "company_status",
            "email", "phonenumber",
            "city", "country",
            "paper",
            "hotel1", "hotel2", "hotel3", "hotel4",
            "discription", "files"
        ]

        TextInput_mytemp1 = TextInput(attrs={
            "type": "text",
            "placeholder": "fill in the fields"
        })

        EmailInput_mytemp1 = EmailInput(attrs={
            "type": "email",
            "placeholder": "fill in the fields"
        })

        Select_mytemp1 = Select(attrs={
                "default": "1"
            }
        )
        Textarea_mytemp1 = Textarea(attrs={
            "placeholder": "fill in the fields"
        })

        FileInput_mytemp1 = FileInput(attrs={
        })

        CheckBox_mytemp1 = CheckboxInput(
        )
        widgets = {
            "first_name": TextInput_mytemp1,
            "last_name": TextInput_mytemp1,
            "academic_title": TextInput_mytemp1,
            "academic_status": TextInput_mytemp1,
            "face_type": Select_mytemp1,
            "format": Select_mytemp1,
            "role": Select_mytemp1,
            "subject": TextInput_mytemp1,
            "company": TextInput_mytemp1,
            "company_status": TextInput_mytemp1,
            "paper": Select_mytemp1,
            "hotel1": CheckBox_mytemp1,
            "hotel2": CheckBox_mytemp1,
            "hotel3": CheckBox_mytemp1,
            "hotel4": CheckBox_mytemp1,
            "email": EmailInput_mytemp1,
            "phonenumber": TextInput_mytemp1,
            "city": TextInput_mytemp1,
            "country": TextInput_mytemp1,

            "discription": Textarea_mytemp1,
            "files": FileInput_mytemp1,
        }


    def send_message(self):
        cd = self.cleaned_data
        
        def for_user():
            body = loader.render_to_string("en/email/registration", {
                "firstname": cd.firstname,
                "lastname": cd.lastname
            })
            message = EmailMessage(
                "Thank you for registration on III IAEEE Conference",
                body,
                settings.DEFAULT_FROM_EMAIL,
                cd.email
            )
            message.send()
            
        def for_admin():            
            body = f'Новый пользователь: {cd.firstname} {cd.lastname}.\n' \
                    'Все данные в админке!'

            message = EmailMessage(
                "Зарегистрировался новый пользователь",
                body,
                settings.DEFAULT_FROM_EMAIL,
                cd.email
            )
            message.send()

        for_admin()
        for_user()
