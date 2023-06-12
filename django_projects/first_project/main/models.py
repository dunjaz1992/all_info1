from django.db import models


class Cars(models.Model):
    title = models.CharField(max_length=15)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='image')
    phone = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
    def __str__(self) -> str:
        return f'{self.title}'


