from django.urls import path

from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.index, name="index"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('index/', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('store/modelo1', views.modelo1, name="modelo1"),
    path('store/modelo2', views.modelo2, name="modelo2"),
    path('store/modelo3', views.modelo3, name="modelo3"),
    path('store/modelo4', views.modelo4, name="modelo4"),
    path('store/modelo5', views.modelo5, name="modelo5"),
    path('store/modelo6', views.modelo6, name="modelo6"),
    path('store/modelo7', views.modelo7, name="modelo7"),
    path('store/modelo8', views.modelo8, name="modelo8"),
    path('store/modelo9', views.modelo9, name="modelo9"),
    path('store/modelo10', views.modelo10, name="modelo10"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]   
