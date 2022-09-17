from django.db import models


class Status(models.Model):
    """ Stock Status of the game """

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    statuses = (
        ('1', 'In-Stock'),
        ('2', 'Back-Order'),
        ('3', 'Out-Of-Stock'),
    )

    status = models.CharField(max_length=1, choices=statuses, default='1')

    def __str__(self):
        if self.status == '1':
            return 'In-Stock'
        elif self.status == '2':
            return 'Back-Order'
        elif self.status == '3':
            return 'Out-Of-Stock'
        else:
            return 'Unknown'


class Game(models.Model):
    """ Video Game Model """

    status = models.ForeignKey('Status', on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year = models.IntegerField(max_length=4)
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
