from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from core.models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, get_user_model,logout
from .forms import LoginForm,RegisterForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    return render(request, 'pagina\Coffee_and_Tea.html')

# def login(request):
#     return render(request, 'pagina\Login.html')

# def register(request):
#     return render(request, 'pagina\Register.html')

# def products(request):
#     return render(request, 'pagina\Producto.html')

# def detail_product(request):
#     return render(request, 'pagina\detail_product.html')


class LoginView(View):
    template_name= 'pagina\Login.html'
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product_view')
        form=LoginForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product_view')
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('product_view')
            else:
                return render(request, self.template_name, {
                    'form':form,
                    'error_message': 'Nombre de usuario o contraseña incorrectos.'
                })
        return render(request, self.template_name, {'form': form})

class RegisterView(View):
    template_name= 'pagina/Register.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product_view')
        form=RegisterForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('product_view')
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password= form.cleaned_data['password']

            User=get_user_model()
            user=User.objects.create_user(username=username,email=email,password=password)

            login(request, user)

            return redirect('product_view')
        return render(request, self.template_name, {'form':form})

class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login_view')

class ProductView(LoginRequiredMixin, View):
    template_name = 'pagina/Producto.html'
    paginated_by = 2

    def get(self, request):
        query = request.GET.get('q')
        products = Product.objects.all()

        if query:
            products = products.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
                ).distinct()
        
        paginator=Paginator(products, self.paginated_by)
        page_number= request.GET.get('page')
        page_obj= paginator.get_page(page_number)
        
        context={
            'page_obj': page_obj,
            'products': page_obj.object_list,
            'query': query
        }
        return render(request, self.template_name, context)


class ProductDetailView(LoginRequiredMixin, View):
    template_name = 'pagina/detail_product.html'
    def get (self, request, id, *args, **kwargs):
        product = get_object_or_404(Product, id=id)
        # Comentarios principales (no son respuesta)
        comments = Comment.objects.filter(product_id=id, comment__isnull=True)
        # Respuestas (opcional, si quieres pasarlas aparte)
        replies = Comment.objects.filter(product_id=id, comment__isnull=False)
        return render(request, self.template_name, {'product': product, 'comments': comments, 'replies':replies})
    
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
class CommentDetailView(LoginRequiredMixin, View):
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

class CommentUpdateView(LoginRequiredMixin, View):
    template_name= 'pagina\partials\comment_update.html'

    def get(self, request, id, *args, **kwargs):
        comment=get_object_or_404(Comment, id=id)
        return render(request, self.template_name, {'comment':comment})

    def post(self, request, id, *args, **kwargs):
        comment=get_object_or_404(Comment, id=id)
        body= request.POST.get("body")
        comment.body= body
        comment.save()
        return redirect('comment_detail_view', id)

class CommentDeleteView(View):
    template_name= 'pagina\partials\comment_delete.html'

    def get(self, request, id, *args, **kwargs):
        comment=get_object_or_404(Comment, id=id)
        return render(request, self.template_name, {'comment':comment})

    def post(self, request, id, *args, **kwargs):
        comment=get_object_or_404(Comment, id=id)
        comment.delete()
        return redirect('product_detail_view', comment.product.id)