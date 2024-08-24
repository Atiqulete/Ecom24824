from django.shortcuts import render,redirect
from website.forms import Contacfrom
from website.models import Banner,Category,Brand,Product

# Create your views here.,

def index(request):
    banner = Banner.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all()
    product = Product.objects.all()
    
    context = {
        'banner' : banner,
        'category' : category,
        'brand' : brand,
        'product' : product
    }

    return render(request,'website/index.html',context)

def contact(request):
    if request.method == 'POST':
        form = Contacfrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = Contacfrom()
    return render(request,'website/contact.html',{'form':form})


def pro_deta(request,pk):
    pro = Product.objects.get(pk=pk)
    context = {
        'pro':pro,
    }
    return render(request,'website/product.html',context)






