from django.urls import path
from .views import product_list, product_create, product_update, product_delete, yadom1, yadom2, yadom3, login_view, logout_view, signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', product_list, name='product_list'),  # หน้ารายการสินค้า
    path('new/', product_create, name='product_create'),  # เพิ่มสินค้าใหม่
    path('<int:pk>/edit/', product_update, name='product_update'),  # แก้ไขสินค้า
    path('<int:pk>/delete/', product_delete, name='product_delete'),  # ลบสินค้า
    path('yadom1/', yadom1, name='yadom1'),
    path('yadom2/', yadom2, name='yadom2'),
    path('yadom3/', yadom3, name='yadom3'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup, name='signup'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # เพิ่ม view ให้ถูกต้อง
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
