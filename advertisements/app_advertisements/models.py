from django.contrib import admin
from django.db import models

# Create your models here.
from django.utils.html import format_html


class Advertisements(models.Model):
    title=models.CharField("Заголовок", max_length=128)
    description=models.TextField("Описание")
    price=models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction=models.BooleanField("Торг", help_text="Отметьте, если торг уместен")
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_time.date()== timezone.now().date():
            creat_time=self.created_time.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; '
                               'font-weight: bold">Сегодня в '
                               '{}</span>', creat_time)
        return self.created_time.strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"