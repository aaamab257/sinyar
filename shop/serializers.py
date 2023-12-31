from rest_framework import serializers
from accounts.models import User
from .models import *
from installment.models import InstallMentsPlans
from accounts.serializers import UserSerializer


class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallMentsPlans
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    plans = PlansSerializer(many=True)
    is_fav = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "image" , 'plans' , 'is_fav')

    def get_is_fav(self,obj):
        user = self.context.get("user")
        return True if user in obj.favorits.all() else False


class SubCategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = SubCategory
        fields = ("id", "name", "products" , 'image')


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "image", "subcategories")


class UserSerializer(serializers.ModelSerializer):
    favorites = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "phone", "email", "favorites")


class MarkedCategorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    category = CategorySerializer(many=True)

    class Meta:
        model = IntrestedCategory
        fields = ("id", "user", "category")


class CreateInterestedCategoriesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = IntrestedCategory
        fields = "__all__"

    def create(self, validated_data):
        user = self.context.get("user")
        return IntrestedCategory.objects.create(user=user, **validated_data)


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ("plan", "product", "status", 'deposit','id_image_front' , 'id_image_back' , 'another_files')

    def create(self, validated_data):
        user = self.context.get("user")
        return Request.objects.create(user=user, **validated_data)


class UserFavoraitesSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    product = ProductSerializer()
    class Meta:
        model = UserFavoriets
        fields= ('user' , 'product')
        
    def get_is_fav(self,obj):
        user = self.context.get("user")
        return True if user in obj.product.favorits.all() else False
    

class GetRequestSerializer(serializers.ModelSerializer):
    plan = PlansSerializer()
    product = ProductSerializer()
    user = UserSerializer()
    class Meta:
        model = Request
        fields = ('plan' ,'deposit' , 'user' , 'product')