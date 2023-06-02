from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path('login/' , views.login_page, name="login_page"),
    path('register/' , views.register, name="register"),
    path('logout/', views.logout_page, name="logout_page"),
    path('predict/', views.predict, name='predict'),
    path('register/' , views.register, name="register"),
    path('test/' , views.test, name="test"),
    path('result/' , views.result, name="result"),
    path("home/", views.home, name="home"),
    path('medicines/' , views.medicines, name="medicines"),
    path('delete-medicine/<id>/' , views.delete_medicine ,name="delete_medicine"),
    path("shop/", views.shop, name="shop"),
    path("buy-medicine/<id>/", views.buy_medicine, name="buy_medicine"),

]