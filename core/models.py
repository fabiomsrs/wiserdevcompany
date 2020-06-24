from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Post(models.Model):
    slug = models.SlugField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=50, verbose_name="título", unique=True)
    content = models.CharField(max_length=50, verbose_name="conteúdo")
    publicacao = models.TextField(max_length=140)
    data_publicacao = models.DateTimeField(auto_now=True, editable=False, verbose_name="data de publicação")
    categories = models.ManyToManyField("core.Category")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="nome", unique=True)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'