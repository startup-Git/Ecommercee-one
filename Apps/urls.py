from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm, PasswordResetForm

urlpatterns = [
    path('', views.Home, name="Home"),
    path('about-us/', views.about, name="about-us"),
    path('contact-us/', views.contact, name="contact-us"),
    path('category/<slug:val>', views.category.as_view(), name="category"),
    path('category-title/<val>', views.categoryTitle.as_view(), name="category-title"),
    path('product-details/<int:pk>', views.productView.as_view(), name="product-details"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('update-address/<int:pk>', views.UpdateAddressView.as_view(), name='update-address'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('checkout/', views.show_cart, name='checkout'),

    path('pluscart/', views.plus_cart, name="pluscart"),
    path('minuscart/', views.minus_cart, name="minuscart"),
    path('removecart/', views.remove_cart, name="removecart"),
    # login Authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name="registration"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='Apps/login.html', authentication_form=LoginForm), name='login'),
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name='Apps/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/password-change-done'), name='password-change'),
    path('password-change-done/', auth_view.PasswordChangeDoneView.as_view(template_name='Apps/passwordchangedone.html'), name='password-change-done'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    # update password
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='Apps/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='Apps/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='Apps/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='Apps/password_reset_complete.html'), name='password_reset_complete'),




]
