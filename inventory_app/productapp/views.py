# Create your views here.
from django.shortcuts import render,get_object_or_404,redirect
# from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from . models import Product
from . forms import ProductForm
# Create your views here.
# def home_view(request,*args, **kwargs):
#     return render(request,'home.html',{})

def product_list(request):
    p = Product.objects.all()
    return render(request, 'home.html', {'products': p})

# class ProductIndex(View):
#     def get(self,request):
#         p = Product.objects.all()
#         return render(request,'home.html',{'products':p})

def product_details(request,pk):
    p = get_object_or_404(Product,pk=pk)
    return render(request, 'product_details.html',{'product':p})
# class Product(View):
#     def get(self,request):
#         p=Product.object.all()
#         return render(request,'home.html',{'product':p})

class ProductAdd(CreateView):
    model=Product
    template_name = 'form.html'
    form_class = ProductForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductAdd, self).form_valid(form)

# class ClassProductView(View):
#     form_class = Product
#     def post(self,request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             p = form.save(commit=False)
#             p.save()
#             return redirect('product_details',pk=p.pk)
#         # return render(request,'')