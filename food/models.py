from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length = 100, null = False)
    price = models.IntegerField(null = False)
    image = models.ImageField(upload_to = "menu")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

STATUS_CHOICES = (
    ('none', 'none'),
    ('in_progress','in_progress'),
    ('done','done')
)
class Order(models.Model):
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default = 'none')
    created_at = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey("account.User", on_delete=models.CASCADE)

    def total_price(self):
        sum = 0
        menu_orders = self.menu_order_set.all()
        for item in menu_orders:
            sum+= item.get_price()
        return sum

class Menu_Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(null = False)

    def get_price(self):
        return self.menu.price * self.quantity

