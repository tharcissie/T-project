from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from .views import dashboard, article_create, my_articles, edit_article, delete_article, article_detail, change_password, update_profile



urlpatterns = [
  path('', accounts_views.signup, name='signup'),
  path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),


  path('reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html',email_template_name='accounts/password_reset_email.html',subject_template_name='accounts/password_reset_subject.txt'),name='password_reset'),
  path('reset/done',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
  path('reset/<int:pk>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
  path('reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
  

   path('mydashboard/', dashboard, name='my_dashboard'),
   path('create-article/', article_create, name='create_article'),
   path('my-articles/', my_articles, name='my_articles'),
   path('edit-article/<int:pk>', edit_article, name='edit_article'),
   path('delete-article/<int:pk>', delete_article, name='delete_article'),
   path('article-details/<int:pk>/', article_detail, name='article_details'),


   path('settings/password/', change_password, name='change_password'),
   path('update_profile/', update_profile, name='update_profile'),
 
 ]

