from rest_framework import viewsets

from . import permissions
from .models import Wishlistitem, Wishlist
from .serializers import WishlistitemSerializer
from django.views.generic.edit import CreateView
from django.shortcuts import redirect, render
from products.models import ProductModel
from django.core.exceptions import ObjectDoesNotExist


class WishlistitemViewSet(viewsets.ModelViewSet):
    queryset = Wishlistitem.objects.all()
    serializer_class = WishlistitemSerializer
    permission_classes = (permissions.WishlistitemPermission,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CreateWishList(CreateView):
    model=Wishlist
    template_name=''
    fields=['wishlist_id', 'products', 'date_added']



def _wishlist_id(request):
    wishlist=request.user
    if not wishlist:
        wishlist=request.user
    print("Wishlist ID:",wishlist)
    return wishlist



def wishlist_detail(request):
    try:
        wishlist = Wishlist.objects.get(wishlist_id=_wishlist_id(request))
        wishlist_items = Wishlistitem.objects.filter(wishlist=wishlist)
    except ObjectDoesNotExist:
        wishlist_items = []  # Sets wishlist_items to empty list if wishlist doesn't exist
    
    print("WishlistItems:", wishlist_items) #DEBUGGING
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})
 # I have spent 2 hours trying to get this to work. The items are going up to the database no bothers, but for some reason they aren't displaying on the website (api/v1/wishlist).




def add_wishlist(request, pk):
    product = ProductModel.objects.get(pk=pk)

    try:
        user = request.user
        wishlistObject = Wishlistitem(user=user, product=product)
        wishlistObject.save()
        return redirect('wishlist:wishlist_detail')
    except Wishlist.DoesNotExist:
        wishlist = Wishlist.objects.create(wishlist_id = _wishlist_id(request))
        wishlist.save()
        return redirect('wishlist:wishlist_detail')
