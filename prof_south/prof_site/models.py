from django.db import models

class Survey(models.Model):
    surname_name = models.CharField(max_length=200)
    question_date = models.DateTimeField('date published')
    e_mail = models.EmailField()
    phone_num = models.IntegerField()
    question_text = models.TextField()

    def __str__(self):
        return self.name

class Сhairman(models.Model):
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phones_num = models.IntegerField()
    e_mail = models.EmailField()
    chairman_photo = models.ImageField(default=1)

    def __str__(self):
        return self.name


class Document(models.Model):
    date_append = models.DateTimeField('date published')
    document = models.FileField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phones_num = models.IntegerField()
    e_mail = models.EmailField()
    employee_photo = models.ImageField(default=1)

    def __str__(self):
        return self.name


class News(models.Model):
    news_date = models.DateTimeField('date published')
    news_text = models.TextField()
    news_photo = models.ImageField()

    def __str__(self):
        return self.name


class ShortNewsOnMainPage(models.Model):
    short_news_text = models.TextField()
    short_news_photo = models.ImageField()

    def __str__(self):
        return self.name
