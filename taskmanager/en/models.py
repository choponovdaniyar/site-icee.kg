from tkinter import N
from django.db import models


class ComitetType(models.Model):
    name = models.CharField("Название",  max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Комитет"
        verbose_name_plural = "Комитеты"


class Сomitet(models.Model):
    name = models.CharField("ФИО",  max_length=100)
    position = models.TextField("Должности", blank=True)
    type = models.ForeignKey(verbose_name="Комитет", to='ComitetType', related_name="users", on_delete=models.CASCADE,
        null=True)
    country = models.ForeignKey(verbose_name="Страна", to='Country', on_delete=models.CASCADE,
        null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "Член комитет"
        verbose_name_plural = "Члены Комитета"


class Program(models.Model):
    date = models.DateField(verbose_name="Дата", blank=True, null=True)
    round = models.CharField("Этап", max_length=1)
    position = models.TextField("Описание")

    def __str__(self):
        return f"{self.date}"

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программа"


class Client(models.Model):
    FACE_TYPE_CHOICES = (
        ('face_1', 'Юридическое лицо'),
        ('face_2', 'Физическое лицо'),
    )
    FORMAT_CHOICES = (
        ('face_ofline', 'Очно',),
        ('face_online', 'Дистанционно')
    )
    PAPER_CHOICES = (
        ('paper_1', 'Без статьи и без доклада'),
        ('paper_2', 'Только публикация'),
        ('paper_3', 'Только устный доклад '),
        ('paper_4', 'Устный доклад + публикация статьи')
    )
    ROLE_CHOICES = (
        ('role_1', 'Слушатель'),
        ('role_2', 'Докладчик'),
    )


    first_name = models.CharField("Имя",  max_length=100)
    last_name = models.CharField("Фамилия", max_length=100)
    academic_title = models.CharField("Ученое звание", max_length=200, blank=True)
    academic_status = models.CharField("Ученая степень", max_length=200, blank=True)
    subject = models.CharField("Тема научного доклада", max_length=200, blank=True)
    face_type = models.CharField(verbose_name='Лицо', max_length=20, choices=FACE_TYPE_CHOICES,default = 1)
    format = models.CharField(verbose_name='Формат участия', max_length=20, choices=FORMAT_CHOICES, default=1)
    role = models.CharField(verbose_name='Роль', max_length=20, choices=ROLE_CHOICES, default=1)
    company = models.CharField("Организация",  max_length=50)
    company_status = models.CharField("Должность",  max_length=50)
    email = models.CharField("e-mail",  max_length=50)
    phonenumber = models.CharField("Телефон", max_length=50)
    city = models.CharField("Город",  max_length=50)
    country = country = models.ForeignKey(verbose_name="Страна", to='Country', on_delete=models.CASCADE,
        null=True)
    discription = models.TextField("Описание", blank=True)
    paper= models.CharField("Доклад / статья",  max_length=20, choices=PAPER_CHOICES, default=1)

    hotel1 = models.BooleanField("Самостоятельный выбор жилья в г. Бишкек", max_length=50, default=False)
    hotel2 = models.BooleanField("Отель “Jannat Regency”, г. Бишкек", max_length=50,  default=False)
    hotel3 = models.BooleanField("Отель “Золотой Дракон”, г. Бишкек", max_length=50, default=False)
    hotel4 = models.BooleanField("Отель “Talisman Village”, Иссык-Куль", max_length=50, default=False)
    
    files = models.FileField(verbose_name="Файлы", blank=True)


    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"



class ParticipantCategories(models.Model):
    name = models.CharField(verbose_name="Название", max_length=250)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория участника конференции"
        verbose_name_plural = "Категории участников конференции"


class Country(models.Model):
    name = models.CharField(verbose_name="Название", max_length=250,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Participant(models.Model):
    name = models.CharField(verbose_name="Ф.И.О.", max_length=250)
    company = models.CharField(verbose_name="Организация", max_length=250, default="")
    category = models.ForeignKey(verbose_name="Категория участника", to='ParticipantCategories',
                related_name="participant", on_delete=models.CASCADE)
    country = models.ForeignKey(verbose_name="Страна", to='Country', related_name="participant",
                on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"


class KeySpeakers(models.Model):
    name = models.CharField(verbose_name="Ф.И.О", max_length=200)
    text = models.TextField(verbose_name="Описание", blank=True)
    image = models.FileField(verbose_name="Фото", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ключевой спикер"
        verbose_name_plural = "Ключевые спикеры"