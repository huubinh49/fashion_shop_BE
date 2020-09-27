from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views
from .views import *
urlpatterns = [
    #user info
    path('user/', obtainUserInfo),
    #jwt auth
    path('signup/', signup),
    path('obtain/token/', obtainTokenForUser),
    path('api/token/refresh/', jwt_views.TokenRefreshSlidingView.as_view(), name='token_refresh'), #TokenRefreshView takes a refresh token and updates it
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'), # it receives user data(email/password) and updates a pair of tokens to authenticate these credentials.
    #social auth
    path('api/login/', include('rest_social_auth.urls_jwt_pair')),
    path('auth/convert-token/', SocialView.as_view()),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    path('',   include('social_django.urls')),
]

# case 1: new Login -> api/token/
# case 2: refresh_token => obtain/token/ => access_token
# case 3: refresh_token qúa hạn => api/token/