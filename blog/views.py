from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from blog.models import Spend
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import CreateView



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def add_spend(request):
    if request.method == "POST":
        s = Spend()
        s.category = request.POST.get("category")
        s.name = request.POST.get("name")
        s.created_date = timezone.now()
        s.amount = request.POST.get("amount")
        s.save()
    return render(request, 'blog/add_spend.html')


def spends_view_url(request):
    header = "Таблица затрат:"
    spend_category = Spend.category
    spend_name = Spend.name
    spend_amount = Spend.amount

    data = {"header": header,
            "category": spend_category,
            "name": spend_name,
            "amount": spend_amount}

    return render(request, 'blog/spend-view.html', context=data)


class ListSpendView(ListView):
    model = Spend
    template_name = 'blog/spends-list.html'


class CreateSpendView(CreateView):
    model = Spend
    template_name = 'add_spend.html'
    fields = ['category', 'name', 'amount']

    def get_success_url(self):
        return HttpResponseRedirect("/")

"""
# сохранение данных в бд
def add_spend(request):
    if request.method == "POST":
        s = Spend()
        s.category = request.POST.get("category")
        s.name = request.POST.get("name")
        s.created_date = '1 января'
        s.amount = request.POST.get("amount")
        s.save()
    return HttpResponseRedirect("/")
"""