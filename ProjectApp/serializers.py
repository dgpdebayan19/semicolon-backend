from rest_framework import serializers
from ProjectApp.models import Customer, Service, ServiceCategory, ServiceSubCategory, ServiceImage, ServicePricing

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password2', None)
        return Customer.objects.create_user(**validated_data)
    


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = Customer
        fields = ['email', 'password']


 

""" class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['category_id', 'category_name', 'category_image', 'category_heading', 'category_subheading','status']

class ServiceSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSubCategory
        fields = ['subcategory_id', 'category','subcategory_image',  'subcategory_heading', 'subcategory_subheading','is_popular_service','subcategory_status']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_id', 'subcategory', 'service_title', 'service_description', 'service_rating', 'no_of_ratings','service_status']

class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ['service_image_id', 'service', 'image_title', 'image_alt_text', 'image_path','image_status'] """




""" class ServiceCategorySerializer1(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['category_id', 'category_name', 'category_image', 'category_heading', 'category_subheading','status']

class ServiceSubCategorySerializer1(serializers.ModelSerializer):
    category= ServiceCategorySerializer1()
    class Meta:
        model= ServiceSubCategory
        fields = ['subcategory_id', 'category','subcategory_image',  'subcategory_heading', 'subcategory_subheading','is_popular_service','subcategory_status']

class ServiceSerializer1(serializers.ModelSerializer):
    subcategory = ServiceSubCategorySerializer1()
    class Meta:
        model = Service
        fields =['service_id', 'subcategory', 'service_title', 'service_description', 'service_rating', 'no_of_ratings','service_status']

class ServiceImageSerializer1(serializers.ModelSerializer):
    service = ServiceSerializer1()
    class Meta:
        model=  ServiceImage
        fields = ['service_image_id', 'service', 'image_title', 'image_alt_text', 'image_path','image_status'] """


class ServiceImageSerializer1(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ('image_title', 'image_alt_text', 'image_path')



class ServicePricingSerializer1(serializers.ModelSerializer):
    class Meta:
        model = ServicePricing
        fields = ('package_name', 'package_title', 'package_description', 'package_price', 'delivery_time', 'no_of_revisions')




class ServiceSerializer1(serializers.ModelSerializer):
    images = ServiceImageSerializer1(many=True)
    pricing = ServicePricingSerializer1(many=True)

    class Meta:
        model = Service
        fields = ('service_id', 'service_title', 'service_description', 'service_status', 'service_rating', 'no_of_ratings', 'images', 'pricing')




class ServiceSubCategorySerializer1(serializers.ModelSerializer):
    services = ServiceSerializer1(many=True)

    class Meta:
        model = ServiceSubCategory
        fields = ('subcategory_id', 'subcategory_heading', 'is_popular_service', 'subcategory_subheading', 'services')




class ServiceCategorySerializer1(serializers.ModelSerializer):
    subcategories = ServiceSubCategorySerializer1(many=True)

    class Meta:
        model = ServiceCategory
        fields = ('category_id', 'category_name', 'category_image', 'category_heading', 'category_subheading', 'subcategories')





#duplicate serializers


class ServiceSubCategorySerializer2(serializers.ModelSerializer):
    #services = ServiceSerializer1(many=True)

    class Meta:
        model = ServiceSubCategory
        fields = ('subcategory_id', 'subcategory_heading', 'is_popular_service', 'subcategory_subheading', 'services')




class ServiceCategorySerializer2(serializers.ModelSerializer):
    subcategories = ServiceSubCategorySerializer2(many=True)

    class Meta:
        model = ServiceCategory
        fields = ('category_id', 'category_name', 'category_image', 'category_heading', 'category_subheading', 'subcategories')
