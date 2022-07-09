from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Сomitet, Program, Client, ParticipantCategories, Participant, Country, KeySpeakers, ComitetType


admin.site.register(Program)


@admin.register(Сomitet)
class СomitetAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'type', 'country']
    list_filter = ['country', 'type']


@admin.register(KeySpeakers)
class ParticipantCategoriesAdmin(admin.ModelAdmin):
    list_display = ["name", "get_photo"]

    def get_photo(self, object):
        return mark_safe("<img src='{}' height='100px'> ".format(object.image.url))

    get_photo.short_description = 'Фото'


@admin.register(Client)
class ParticipantCategoriesAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "city", "country"]
    list_filter = ["role", "format", "face_type", "paper", 'country']
    readonly_fields = [
        "first_name", "last_name",
        "academic_title", "academic_status",
        "subject", "discription",
        "face_type", "format", "role",
        "company", "company_status",
        "email", "phonenumber",
        "city", "country",
        "paper", 
        "hotel1", "hotel2", "hotel3", "hotel4", "files"
    ]


# @admin.register(ParticipantCategories)
# class ParticipantCategoriesAdmin(admin.ModelAdmin):
#     list_display = ["name"]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ["name", "company", "country", "category"]
    list_filter = ["category"]
    

