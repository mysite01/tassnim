from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from OnlineShop import settings
from . import views
from django.urls import path

from .views import checkout

#from .views import view_cart, add_to_cart, remove_from_cart, housing_list, checkout

urlpatterns = [
    path('show/', views.housing_list, name='housing-list'),
    path('show/<int:pk>/', views.housing_detail, name='housing-detail'),
    path('add/', views.housing_create, name='housing-create'),
    path('delete/<int:pk>/', views.housing_delete, name='housing-delete'),
    path('comment/edit/<int:pk>/', views.edit_comment, name='edit-comment'),
    path('vote/<int:pk>/<str:vote_type>/', views.vote, name='vote'),
    path('comment-vote/<int:comment_id>/<str:vote_type>/', views.comment_vote, name='comment-vote'),
    path('search/', views.housing_search, name='housing-search'),
    path('add_to_cart/<int:housing_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),

    # Beispiel für die
    # path('PrList/', views.product_list, name='product_list'),
#    path('cart/', views.view_cart, name='view_cart'),
    #path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
#    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout')
  #  path('housings/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
