from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.
from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(pk=list_id)
    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {
        'list': list_
    })

def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'],
        list=list_)
    try:
        item.save()
        item.full_clean()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {"error": error})
    return redirect('/lists/%d/' % list_.pk)


def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/%d/' % (list_.id,))