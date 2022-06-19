from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),

    path('fort/', views.fort, name='fort'),
    path('fort-detail/<int:pk>', views.fortdetailview.as_view(), name='fort-detail'),

    path('food/', views.food, name='food'),
    path('food-detail/<int:pk>', views.fooddetailview.as_view(), name='food-detail'),

    path('prod/', views.ProductView.as_view(), name='prod'),
    path('product-detail/<int:pk>', views.productdetailview.as_view(), name='product-detail'),

    path('pa/', views.pa, name='pa'),
    path('pa-detail/<int:pk>', views.padetailview.as_view(), name='pa-detail'),

    path('fr/', views.freedom.as_view(), name='fr'),
    path('fr-detail/<int:pk>', views.frdetailview.as_view(), name='fr-detail'),

    path('mi/', views.music.as_view(), name='mi'),
    path('mi-detail/<int:pk>', views.mdetailview.as_view(), name='mi-detail'),
    
    path('ti/', views.textiles.as_view(), name='ti'),
    path('ti-detail/<int:pk>', views.textiledetailview.as_view(), name='ti-detail'),





    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)