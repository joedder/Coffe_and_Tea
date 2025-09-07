from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

# Create your models here.

class User(AbstractUser):
    username=models.CharField(max_length=150, unique=True)
    email=models.EmailField(unique=True)
    phone_number=models.CharField(max_length=15, blank=True, null=True)
    address=models.TextField(max_length=255, blank=True, null=True)
    city=models.CharField(max_length=100, blank=True, null=True)
    country=models.CharField(max_length=100, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    # REQUIRED_FIELDS=['email', 'phone_number'] #crecion de campos requeridos al crear el super usuario

    class Meta:
        db_table="users"
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
    
    def __str__(self):
        return f"{self.username} ({self.email})"

class CategoryProduct(models.Model):
    name=models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    description=models.TextField(blank=True, verbose_name='Descripción',null=True)

    class Meta:
        db_table="categories"
        verbose_name='Categoría'
        verbose_name_plural='Categorías'
    
    def __str__(self):
        return f"{self.name} - {self.description}"

class Product(models.Model):
    name=models.CharField(max_length=100, unique=True, verbose_name='Nombre')
    description=models.TextField(blank=True, verbose_name='Descripción',null=True)
    price=models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio', default=0.00)
    stock=models.IntegerField(default=0,verbose_name="Stock",null=False) #revisar
    image=models.ImageField(
        verbose_name='Imagen',
        upload_to='products/images/',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'webp'])],
        blank=True,
        null=True
    )
    category=models.ForeignKey('CategoryProduct', on_delete=models.CASCADE, related_name='products_category')

    class Meta:
        db_table="products"
        verbose_name='Producto'
        verbose_name_plural='Productos'

    def __str__(self):
        return f"{self.name}- {self.description}- ${self.price} - {self.category.name} - {self.image.url if self.image else 'Sin imagen'} - {self.stock}"

class Comment(models.Model):
    comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies', verbose_name='Comentario Padre')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='Comentario_del_Producto')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='Comentario_del_Usuario')
    body = models.TextField(verbose_name='Contenido', max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return f"Comentario de {self.user.username} en {self.product.name}: {self.body[:20]}..."