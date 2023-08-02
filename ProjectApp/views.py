from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ProjectApp.serializers import UserRegistrationSerializer, UserLoginSerializer, ServiceCategorySerializer1, ServiceSerializer1, ServiceCategorySerializer2
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from ProjectApp.models import Service, ServiceCategory, ServiceImage, ServiceSubCategory
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# Create your views here.

@api_view(['POST'])
def user_registration(request):
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception= True):
            user= serializer.save()
            token= get_tokens_for_user(user)
            return Response({'token': token, 'msg':'Registration Successfull'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception= True):
            email= serializer.data.get('email')
            password = serializer.data.get ('password')
            user =  authenticate(email= email, password=password)
            if user is not None:
              token= get_tokens_for_user(user)
              return Response ({'token': token,'msg': 'Login Successful'}, status= status.HTTP_200_OK)
            else:
              return Response ({'msg': 'Error'}, status= status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

""" @api_view(['GET'])
def home_page(request):
    categories = ServiceCategory.objects.all()
    subcategories = ServiceSubCategory.objects.all()
    services = Service.objects.all()
    service_images = ServiceImage.objects.all()
    #service_pricings = ServicePricing.objects.all()

        # Serialize the data for each model using the respective serializers

    category_serializer = ServiceCategorySerializer(categories, many=True)
    subcategory_serializer = ServiceSubCategorySerializer(subcategories, many=True)
    service_serializer = ServiceSerializer(services, many=True)
    service_image_serializer = ServiceImageSerializer(service_images, many=True)
    #service_pricing_serializer = ServicePricingSerializer(service_pricings, many=True)

        # Return a dictionary containing the serialized data for each model

    data = {
            'categories': category_serializer.data,
            'subcategories': subcategory_serializer.data,
            'services': service_serializer.data,
            'service_images': service_image_serializer.data,
        }

    return Response(data, status=status.HTTP_200_OK) """


""" class HomePageView(ListAPIView):
    queryset = ServiceImage.objects.all()
    serializer_class = ServiceImageSerializer1 """


class HomePageView(APIView):
    def get(self, request):
        categories = ServiceCategory.objects.all()
        serializer = ServiceCategorySerializer1(categories, many=True)
        return Response(serializer.data)
    


@api_view(['GET'])
def HomePageViewTest(self):
        categories = ServiceCategory.objects.all()
        serializer = ServiceCategorySerializer1(categories, many=True)
        return Response(serializer.data)


class ServiceDetailView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer1


class ServiceCategoryDetailView(RetrieveAPIView):
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer2
    lookup_field = 'category_id'