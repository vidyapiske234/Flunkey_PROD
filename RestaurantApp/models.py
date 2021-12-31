from django.db import models


# RESTAURANT MODEL.........................................................
class Restaurant(models.Model):
    rest_name = models.CharField(max_length = 300, unique = True)
    rest_location = models.CharField(max_length = 300)
    rest_logo = models.ImageField(upload_to = 'logos')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Restaurant'
        verbose_name_plural = 'Restaurants'

    def __str__(self):
        return str(self.rest_name)
#..........................................................................

    
# TABLE MODEL..............................................................
class Table(models.Model):
    rest = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_no = models.CharField(max_length =20)
    avialable = models.BooleanField(default = True)
    image = models.ImageField(upload_to = 'tables', blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('table_no',)
        verbose_name = 'Table'
        verbose_name = 'Tables'

    def __str__(self):
        return str(self.table_no)
#..........................................................................


# TempDeliveryModel.......................................................................
class TempDelivery(models.Model):
    food_type_choices = (
        ('solid', 'solid'),
        ('liquid', 'liquid'),
    )
    speed_choices = (
        (120, 120),
        (90,90),
    )
    username = models.CharField(max_length= 20, null = True)
    restaurant = models.CharField(max_length = 300)
    bot_name = models.CharField(max_length = 300)
    bot_id = models.IntegerField(null = True)
    bot_color = models.CharField(max_length =100, null = True)
    table_no = models.CharField(max_length = 100, null = True)
    ip = models.CharField(max_length = 100, null = True)
    port = models.IntegerField(null=True)
    food_delivered = models.BooleanField(default = False)
    food_type = models.CharField(max_length = 100, choices = food_type_choices, default = 'solid')
    speed = models.IntegerField(choices = speed_choices, default = 120)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Temporary Delivery'
        verbose_name_plural = 'Temporary Delliveries'

    def __str__(self):
        return (str(self.id))
#.........................................................................................


# Delivery Model...........................................................
class Delivery(models.Model):
    username =  models.CharField(max_length= 100, null = True)
    restaurant = models.CharField(max_length = 300)
    bot_id = models.IntegerField()
    bot_name = models.CharField(max_length = 100)
    bot_color = models.CharField(max_length =100, null = True)
    table_no = models.IntegerField()
    ip = models.CharField(max_length = 30, null = True)
    port = models.IntegerField(null = True)
    food_type = models.CharField(max_length=30, null = True)
    speed_of_the_bot = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    food_delivered = models.BooleanField(default = False)
    time = models.DecimalField(max_digits=50, decimal_places=6, default = 0)

    class Meta:
        verbose_name = 'Final Delivery'
        verbose_name_plural = 'Final Deliveries'

    def __str__(self):
        return str(self.id)
#............................................................................
