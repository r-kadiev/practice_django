from django.db import models

# Create your models here.

class Category(models.Model):
    """Модель категорий"""

    name = models.CharField(verbose_name="Имя", max_length=100)
    slug = models.SlugField(verbose_name="URL", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"




class Tag(models.Model):
    """Модель Тегов"""

    name = models.CharField(verbose_name="Имя", max_length=100)
    slug = models.SlugField(verbose_name="URL", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Post(models.Model):
    """Модель постов"""

    title = models.CharField(max_length=200)
    mini_text = models.TextField(max_length=450)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(models.Model):
    """Модель комментарии"""

    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    moderation = models.BooleanField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментария"
        verbose_name_plural = "Комментарии"
