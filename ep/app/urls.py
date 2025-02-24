from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('productDetails/<int:pk>',views.productDetails.as_view(), name='productDetails'),
    path("catagory/<slug:val>", views.catagory.as_view(), name='catagory'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)