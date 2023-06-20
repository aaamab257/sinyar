from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import CartSerializer
from .models import Cart, CartItem
from shop.models import Product
# Create your views here.


class AddToCartAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        user = request.user
        product = Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    

class RemoveFromCartAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))
        user = request.user
        try:
            cart = Cart.objects.get(user=user)
            cart_item = cart.items.get(product_id=product_id)
            if cart_item.quantity > quantity:
                cart_item.quantity -= quantity
                cart_item.save()
            else:
                cart_item.delete()
        except (Cart.DoesNotExist, CartItem.DoesNotExist):
            pass
        cart = Cart.objects.get(user=user)
        serializer = CartSerializer(cart)
        return Response({'removed' : True})