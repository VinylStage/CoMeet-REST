from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "user"

urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path('log_in/', views.log_in_view, name='log_in'),
    # path('log_out/', views.log_out_view, name='log_out'),
    # path('sign_up/', views.sign_up_view, name='sign_up'),
    # path('my_page/<int:id>', views.my_page_view, name='my_page'),
    # path('user_page/<int:id>', views.user_my_view, name='user_page'),
]
