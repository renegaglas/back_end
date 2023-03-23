from django.urls import path

from . import views

app_name = "our_memo"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('block/create/', views.BlockCreateView.as_view(), name='create_block'),
    path('block/<int:pk>/', views.BlockView.as_view(), name='block'),
    path('block/<int:pk>/update', views.BlockUpdate.as_view(), name='update_block'),
    path('block/<int:pk>/delete', views.DeleteBlock.as_view(), name='delete_block'),


    path('memo/create/', views.MemoCreateView.as_view(), name='create_memo'),
    path('memo/<int:pk>', views.MemoView.as_view(), name='memo'),
    path('memo/<int:pk>/update', views.MemoUpdate.as_view(), name='update_memo'),
    path('memo/<int:pk>/delete', views.DeleteMemo.as_view(), name='delete_memo'),
]
