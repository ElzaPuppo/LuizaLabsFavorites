from django.urls import path
from .import views
from rest_framework_simplejwt import views as jwt_views



urlpatterns=[
    path('', views.index, name="api-index"),

    path('api/brands/', views.brands, name='brands'),
    path('api/deletebrand/<int:idbrand>', views.deletebrand, name='brand'),

    path('api/client/<int:idclient>', views.client, name='client'),    
    path('api/clients/', views.clients, name='clients'),

    path('api/product/<int:idproduct>', views.product, name='product'),    
    path('api/products/', views.products, name='products'),

    
    path('api/favorite/<int:idclient>', views.favorite, name='favorite'),    
    path('api/deletefavorite/<int:idclient>/<int:idproduct>', views.deletefavorite, name='deletefavorite'),       
    path('api/favorites/', views.favorites, name='favorites'),

    path('api/review/<int:idproduct>', views.review, name='review'),    
    path('api/detailreview/<int:idclient>/<int:idproduct>', views.detailreview, name='detailreview'),       
    path('api/reviews/', views.reviews, name='reviews'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view()),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view()),

    
]