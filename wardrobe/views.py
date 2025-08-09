from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import ClothingItem

# Create your views here.
def shop(request):
    query = request.GET.get('q')
    if query:
        items = ClothingItem.objects.filter(name__icontains=query)
    else:
        items = ClothingItem.objects.all()
    items = ClothingItem.objects.all()
    return render(request, 'wardrobe/shop.html', {'items': items})

def clothing_detail(request, item_id):
    item = get_object_or_404(ClothingItem, id=item_id)
    return render(request, 'wardrobe/detail.html', {'item': item})

def mannequin(request):
    return render(request, 'wardrobe/mannequin.html')