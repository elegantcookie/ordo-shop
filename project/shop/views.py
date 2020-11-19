from django.shortcuts import render, get_object_or_404
from .models import Product, Promotion, ProductImages
from django.views.generic import View, DetailView, ListView
from os.path import join
from project.settings import BASE_DIR
from .forms import SortForm
from django.db.models import *
from django.shortcuts import redirect
from .models import Category


class Index(ListView):
    template_name = 'index.html'
    context_object_name = 'promos'

    def get_queryset(self):
        self.request.session['q'] = ''
        promos = Promotion.objects.all()
        return promos


# def index(request):
#     promos = Promotion.objects.all()
#     context = {
#         'promos': promos,
#     }
#     request.session['q'] = ''
#
#     return render(request, 'index.html', context=context)


def sort_price(request, got_items=None):  # Говнокод | разобрать
    i = request.session['i']
    lte = request.session['lte']
    gte = request.session['gte']

    if got_items is not None:  # Если получает query
        obj = got_items
        if gte and lte:
            request.session['lte'] = lte
            request.session['gte'] = gte
            got_items = obj.filter(price__gte=gte, price__lte=lte)
        elif gte:
            request.session['gte'] = gte
            got_items = obj.filter(price__gte=gte)
        elif lte:
            request.session['lte'] = lte
            got_items = obj.filter(price__lte=lte)
        else:
            got_items = obj

        if i == '1':
            products = got_items.order_by('price')
        elif i == '2':
            products = got_items.order_by('-price')
        elif i == '3':
            products = got_items.order_by('name')
        elif i == '4':
            products = got_items.order_by('-name')
        else:
            products = got_items
    else:
        if request.session['id']:
            id = request.session['id']
            if gte and lte:
                request.session['lte'] = lte
                request.session['gte'] = gte
                got_items = Product.objects.filter(tags=id, price__gte=gte, price__lte=lte)
            elif gte:
                request.session['gte'] = gte
                got_items = Product.objects.filter(tags=id, price__gte=gte)
            elif lte:
                request.session['lte'] = lte
                got_items = Product.objects.filter(tags=id, price__lte=lte)
            else:
                got_items = Product.objects.filter(tags=id)
        else:
            if gte and lte:
                request.session['lte'] = lte
                request.session['gte'] = gte
                got_items = Product.objects.filter(price__gte=gte, price__lte=lte)
            elif gte:
                request.session['gte'] = gte
                got_items = Product.objects.filter(price__gte=gte)
            elif lte:
                request.session['lte'] = lte
                got_items = Product.objects.filter(price__lte=lte)
            else:
                got_items = Product.objects.all()

        if i == '1':
            products = got_items.order_by('price')
        elif i == '2':
            products = got_items.order_by('-price')
        elif i == '3':
            products = got_items.order_by('name')
        elif i == '4':
            products = got_items.order_by('-name')
        else:
            products = got_items

    return products


def get_category(request, id):
    if request.method == 'GET':
        request.session['i'] = request.GET.get('sort')
        request.session['gte'] = request.GET.get('gte')
        request.session['lte'] = request.GET.get('lte')
        request.session['id'] = id
        sort_form = SortForm(request.GET)
        if not sort_form.is_valid():
            return redirect('shop:get_category', id=id)
        else:  # Чтобы значение оставалось после отправки формы
            sort_form.cleaned_data['gte'] = request.session['gte']
            sort_form.cleaned_data['lte'] = request.session['lte']

        products = sort_price(request)

        sort_form = SortForm(request.GET)
        context = {
            'products': products,
            'sort_form': sort_form,
        }
        return render(request, 'product/category.html', context)


class ProductDetail(View):  # Можно использовать, когда def func(request, data):
    # return render(request, 'tmplt.path', context) 
    def get(self, request, id):
        product = Product.objects.filter(id=id, available=True)[0]
        product_images = ProductImages.objects.filter(iproduct=product)
        return render(request, 'product/detail.html', context={'product': product, 'product_images': product_images})


# def product_detail(request, id):
#     product = get_object_or_404(Product, id=id, available=True)
#     context = {
#         'product': product,
#     }
#
#     return render(request, 'product/detail.html', context=context)


class SearchView(ListView):
    template_name = join(BASE_DIR, 'shop/templates/product/category.html')

    # context_object_name = 'products'

    def get_queryset(self):  # поиск, квери кидает в сессию['q']
        if not self.request.session['q']:
            self.request.session['i'] = self.request.GET.get('sort')

            sort_form = SortForm(self.request.GET)

            query = self.request.GET.get('q')  # Поиск

            if query is None:
                got_items = ProductImages.iproduct.objects.filter(available=True)
                products = sort_price(self.request, got_items)

                context = {
                    'products': products,
                    'sort_form': sort_form,
                }

                return context
            else:
                got_items = Product.objects.filter(
                    Q(name__icontains=query) | Q(id__icontains=query)
                )

                products = got_items

                agg_max = products.aggregate(Max('price'))['price__max']
                agg_min = products.aggregate(Min('price'))['price__min']

                context = {
                    'products': products,
                    'sort_form': sort_form,
                }
                self.request.session['q'] = query
                return context
        else:
            new_query = self.request.GET.get('q')

            if self.request.session['q'] != new_query and new_query is not None:
                if self.request.method == 'GET':
                    self.request.session['i'] = self.request.GET.get('sort')
                    price_form = SortForm(self.request.GET)
                    if not price_form.is_valid():
                        return redirect('/')
                    else:  # Чтобы значение оставалось после отправки формы
                        price_form.cleaned_data['gte'] = self.request.session['gte']
                        price_form.cleaned_data['lte'] = self.request.session['lte']

                    sort_form = SortForm(self.request.GET)

                # Поиск

                query = new_query
                got_items = Product.objects.filter(
                    Q(name__icontains=query) | Q(id__icontains=query)
                )

                products = sort_price(self.request, got_items)
                context = {
                    'products': products,
                    'sort_form': sort_form,
                    'price_form': price_form
                }
                self.request.session['q'] = query
                return context
            else:
                if self.request.method == 'GET':
                    self.request.session['i'] = self.request.GET.get('sort')
                    self.request.session['gte'] = self.request.GET.get('gte')
                    self.request.session['lte'] = self.request.GET.get('lte')

                    sort_form = SortForm(self.request.GET)

                    if not sort_form.is_valid():
                        return redirect('/')
                    else:  # Чтобы значение оставалось после отправки формы
                        sort_form.cleaned_data['gte'] = self.request.session['gte']
                        sort_form.cleaned_data['lte'] = self.request.session['lte']

                # Поиск

                query = self.request.session['q']
                got_items = Product.objects.filter(
                    Q(name__icontains=query) | Q(id__icontains=query)
                )

                products = sort_price(self.request, got_items)

                self.request.session['gte'] = self.request.GET.get('gte')
                self.request.session['lte'] = self.request.GET.get('lte')

                context = {
                    'products': products,
                    'sort_form': sort_form,
                }
                return context
