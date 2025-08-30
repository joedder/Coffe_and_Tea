from django.shortcuts import render
from django.views import View

# Create your views here.

def index(request):
    return render(request, 'pagina\Coffee_and_Tea.html')

def login(request):
    return render(request, 'pagina\Login.html')

def register(request):
    return render(request, 'pagina\Register.html')

def products(request):
    return render(request, 'pagina\Producto.html')

def detail_product(request):
    return render(request, 'pagina\detail_product.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'pagina\Login.html')
    
    def post(self, request):
        pass

class RegisterView(View):
    def get(self, request):
        return render(request, 'pagina\Register.html')

    def post(self, request):
        pass

class ProductView(View):
    def get(self, request):
        return render(request, 'pagina\Producto.html')

    def post(self, request):
        pass