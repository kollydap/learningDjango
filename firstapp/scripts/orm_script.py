from firstapp.models import Restaurant,Rating,Sale
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import connection


def run():
    # resturant = Restaurant()
    # resturant.name = "kola Resturant"
    # resturant.latitude = 50.3
    # resturant.longitude = 50.2
    # resturant.date_opened = timezone.now()
    # resturant.restaurant_type = Restaurant.TypeChoices.ITALIAN
    
    # resturant.save()
    
    # Restaurant.objects.create(
    #     name = "pixxa shop",
    #     latitude = 50.2,
    #     longitude = 50.5,
    #     restaurant_type = Restaurant.TypeChoices.INDIAN,
    #     date_opened = timezone.now()
    # )
    
    # restaurant = Restaurant.objects.first()
    # user = User.objects.first()
    # rating = Rating.objects.create(user=user,restaurant=restaurant, rating = 5)
    # print(restaurant)
    # print(connection.queries)
    
# manage.py shell_plus --print-sql 
    restaurant = Restaurant.objects.first()
    print(restaurant)
    # print(Rating.objects.filter(rating = 3))
    # print(restaurant.ratings.all())
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.first(),
    #     income = 2.33,
    #     datetime = timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.first(),
    #     income = 2.56,
    #     datetime = timezone.now()
    # )
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.first(),
    #     income = 5.33,
    #     datetime = timezone.now()
    # )
    print(restaurant.sales.all())