from django.shortcuts import render
from django.views import View
from .models import Product

# def home(request):
#     cards = [
#         {"title": "Mens casual Shirt","price":"13", "description": "This is the first card.", "image": "app/images/product/p1.jpg"},
#         {"title": "Mens solid T-shirt","price":"15", "description": "This is the second card.", "image": "app/images/product/p2.jpg"},
#         {"title": "Mens Casual Shirt","price":"10", "description": "This is the third card.", "image": "app/images/product/p3.jpg"},
#         {"title": "Womens corporate wear","price":"60", "description": "This is the fourth card.", "image": "app/images/product/p4.jpg"},
#     ]
#     return render(request, "app/home.html", {"cards": cards})

def contact(request):
    # Your contact view logic
    return render(request, 'app/contact.html')

def about(request):
    # Your contact view logic
    return render(request, 'app/about.html')

class catagory(View):
    def get(self,request,val):
        product=Product.objects.filter(catagory=val)

        return render(request,"app/catagory.html",locals())
    
class productDetails(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,"app/productDetails.html",locals())
    
class home(View):
    def get(self,request):
        product=Product.objects.all()
        return render(request,"app/home.html",locals())

    