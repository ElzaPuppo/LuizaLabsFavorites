from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.name

    def to_dict(self):
        return{
            "name": self.name,
            "email": self.email,
            "id": self.id
        }



class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id
        }


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name='Nome')
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Preço')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.CharField(max_length=200, verbose_name='URL da imagem')
    reviewScore = models.FloatField(verbose_name='Nota', null=True)

    def __str__(self) -> str:
        return self.title

    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "brand": self.brand.to_dict(),
            "id": self.id,
            "image": self.image,            
            "reviewScore": self.reviewScore
        }

class Review(models.Model):
    text = models.CharField(max_length=400, verbose_name='Opinião')
    score =  models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Nota')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'client'], name = 'reviewed')
        ]

    def __str__(self) -> str:
        return f"{self.client.name} - {self.product.title}"

    def to_dict(self):
        return{
           "product": self.product.to_dict(),
           "client": self.client.to_dict(),
           "score": self.score,
           "text": self.text,
           "id": self.id
        }

class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'client'], name = 'favoritado')
        ]

    def __str__(self) -> str:
        return f"{self.client.name} - {self.product.title}"

    def to_dict(self):
        return{
           "product": self.product.to_dict(),
           "client": self.client.to_dict(),
           "id": self.id
        }
