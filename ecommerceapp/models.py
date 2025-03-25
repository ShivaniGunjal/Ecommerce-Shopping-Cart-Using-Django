from django.db import models

# Create your models here.
class Contact(models.Model):
    # contact_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    email=models.EmailField()
    desc= models.TextField(max_length=500)
    phonenumber= models.IntegerField()

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id= models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/images')

    def __str__(self):
        return self.product_name
    
class Order(models.Model):
    items_json = models.TextField()  # Stores cart items as JSON
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)  # Automatically sets date

    def __str__(self):
        return f"Order {self.id} by {self.name}"
    
class OrderUpdate(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    update_desc = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for Order {self.order.id}"
