from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from core.models import *

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
    template_name= 'pagina/Login.html'
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        pass

class RegisterView(View):
    template_name= 'pagina/Register.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass

class ProductView(View):
    template_name = 'pagina/Producto.html'
    def get(self, request):
        return render(request, self.template_name)


class ProductDetailView(View):
    template_name = 'pagina/detail_product.html'
    def get (self, request, id, *args, **kwargs):
        product=get_object_or_404(Product, id=id)
        comments=Comment.objects.filter(product_id=id)
        return render(request, self.template_name, {'product':product, 'comments':comments})
    
    def post (self, request, id, *args, **kwargs):
        body= request.POST.get("body")
        product=Product.objects.filter(id=id).first() if id else None
        current_user= request.user
        print(body)
        new_comment= Comment.objects.create(
            body=body,
            product=product,
            user=current_user
        )


        return redirect('product_detail_view', id)
class CommentDetailView(View):
    template_name = 'pagina/detail_comment.html'
    def get (self, request, id, *args, **kwargs):
        comment=get_object_or_404(Comment, id=id)
        comments=Comment.objects.filter(comment_id=id)
        return render(request, self.template_name, {'comment':comment, 'comments':comments})
    
    def post (self, request, id, *args, **kwargs):
        body= request.POST.get("body")
        comment=Comment.objects.filter(id=id).first() if id else None
        product = comment.product if comment else None
        current_user= request.user
        print(body)
        new_comment= Comment.objects.create(
            body=body,
            comment=comment,
            product=product,
            user=current_user
        )


        return redirect('comment_detail_view', id)