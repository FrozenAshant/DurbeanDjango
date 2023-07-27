from django.urls import path
from account.views import UserRegistrationView, UserLoginView, UserLogoutView,CustomTokenObtainPairView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
