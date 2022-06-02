import datetime

from django.db import models


# Create your models here.

def expire():
    return datetime.date.today() + datetime.timedelta(days=365)


class Customer(models.Model):
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    customer_since = models.DateField(auto_now=True)
    prime_customer = models.CharField(max_length=1, default='N', null=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Address(models.Model):
    STATE_CHOICES = [
        ('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'),
        ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'),
        ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'),
        ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
        ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
        ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'),
        ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'),
        ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
        ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'),
        ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming')
    ]

    street = models.CharField(max_length=25, null=False)
    city = models.CharField(max_length=25, null=False)
    state = models.CharField(max_length=25, choices=STATE_CHOICES, null=False)
    zipCode = models.CharField(max_length=10, null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='address')

    def __str__(self):
        return self.street


class Order(models.Model):
    p_type = [
        ('C', 'Credit'),
        ('B', 'Bank Account'),
        ('O', 'Other')
    ]
    order_number = models.CharField(max_length=25, null=False, unique=True)
    order_date = models.DateField(auto_now=True)
    order_total = models.DecimalField(null=False, max_digits=12, decimal_places=2, default=0)
    payment_type = models.CharField(max_length=1, choices=p_type, null=False)
    account_number = models.CharField(max_length=20, null=False, unique=True)
    expiration_date = models.DateField(default=expire)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order')

    def __str__(self):
        return self.order_number


class OrderItems(models.Model):
    item_choices = [
        ('Java 101', 'Java 101'),
        ('Python 101', 'Python 101'),
        ('Biology 101', 'Biology 101'),
        ('English 101', 'English 101'),
        ('Cloud Computing 101', 'Cloud Computing 101')
    ]

    item_description = models.CharField(max_length=25, choices=item_choices, default='Java 101')
    item_quantity = models.IntegerField(null=False)
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')

