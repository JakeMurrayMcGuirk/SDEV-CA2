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
    #wishlist = request.session.session_key
    wishlist="wishlist/"
    #wishlist = "self.request.user/wishlist/"
    if not wishlist:
        wishlist="wishlist/"
        #wishlist = request.user.create()
    return wishlist



def add_wishlist(request, pk):
    product = ProductModel.objects.get(pk=pk)
    try:
        wishlist = Wishlist.objects.get(wishlist_id = _wishlist_id(request))
    except Wishlist.DoesNotExist:
        wishlist = Wishlist.objects.create(wishlist_id = _wishlist_id(request))
        wishlist.save()
    return redirect('wishlist:wishlist_detail')



def wishlist_detail(request, total=0, counter=0, wishlist_items = None):
    try:
        wishlist = Wishlist.objects.get(wishlist_id=_wishlist_id(request))
        wishlist_items=Wishlistitem.objects.filter(wishlist=wishlist)
        for wishlist_item in wishlist_items:
            counter+=wishlist_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'wishlist.html', {'wishlist_items':wishlist_items,'total':total,'counter':counter})