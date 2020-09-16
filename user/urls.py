from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import *
urlpatterns = [
    # Your URLs...
    path('signup/', signup),
    # path('register/', userRegistration),
    path('obtain/token/', obtainTokenForUser),
    path('api/token/refresh/', jwt_views.TokenRefreshSlidingView.as_view(), name='token_refresh'), #TokenRefreshView takes a refresh token and updates it
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'), # it receives user data(email/password) and updates a pair of tokens to authenticate these credentials.
]

# case 1: new Login -> api/token/
# case 2: refresh_token => obtain/token/ => access_token
# case 3: refresh_token qúa hạn => api/token/