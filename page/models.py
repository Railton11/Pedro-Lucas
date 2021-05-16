from django.db import models
from django.urls import reverse




class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Indentificador', max_length=100, unique=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('page:categorias')

class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Indentificador', max_length=100, unique=True)
    category = models.ForeignKey('page.Category', verbose_name='Categoria', on_delete=models.CASCADE)
    description = models.TextField('Descrição', blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    image = models.ImageField('Imagem', upload_to='static/products', blank=True, null=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('page:product')



class Banner(models.Model):
    name = models.CharField('Nome', max_length=100)
    image  = models.ImageField('Imagem', upload_to='static/banners', blank=True, null=True)

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('page:banner')   