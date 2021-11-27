from django.db import models
from django.db.models.base import Model
from RestaurantApp.models import Restaurant

# Create your models here.

# BOT MODEL.................................................................................
class Bot(models.Model):
    rest = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    bot_no = models.IntegerField()
    bot_name = models.CharField(max_length = 300, unique = True)
    bot_color = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'bot_images')
    status = models.BooleanField(default=True, help_text="bot working(active or inactive)")   # active or inactive
    avialable = models.BooleanField(default=True, help_text="available or not avialabe for delivery")  # avialabe to serve or not avialable
    ip = models.CharField(max_length=15)
    port = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    battery = models.DecimalField(max_digits=5, decimal_places=2, default = 0)

    class Meta:
        verbose_name = 'Bot'
        verbose_name_plural = 'Bots'
        ordering = ('-id',)

    def __str__(self):
        return (self.bot_name)
#...........................................................................................