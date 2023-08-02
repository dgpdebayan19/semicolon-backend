from django.urls import path
from ProjectApp.views import user_registration, user_login,  HomePageView, HomePageViewTest, ServiceDetailView, ServiceCategoryDetailView

urlpatterns = [
    path('register', user_registration, name= 'register' ),
    path('login', user_login, name= 'login' ),
    #path('login', UserLoginView.as_view(), name= 'login' ),
    #path('profile', UserProfileView.as_view(), name= 'profile' ),



    #path('', HomePageView.as_view(), name= 'home_page' ),
    #path('', home_page, name= 'home_page' ),

    path('', HomePageViewTest, name= 'home_page' ),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('service-category/<int:category_id>/', ServiceCategoryDetailView.as_view(), name='service-category-detail'),
]