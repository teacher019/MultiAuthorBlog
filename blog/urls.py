from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "author/dashboard/",
        views.author_dashboard,
        name="author_dashboard"
    ),

    path(
        "signup/",
        views.signup,
        name="signup"
    ),

    path(
        "login/",
        views.user_login,
        name="login"
    ),

    path(
        "logout/",
        views.user_logout,
        name="logout"
    ),

    # Create Post URL must come before the slug URL
    path(
        "post/create/",
        views.create_post,
        name="create_post"
    ),

    path(
        "post/<slug:slug>/comment/",
        views.add_comment,
        name="add_comment"
    ),

    path(
        "post/<slug:slug>/like/",
        views.toggle_like,
        name="toggle_like"
    ),

    path(
        "post/<slug:slug>/",
        views.post_detail,
        name="post_detail"
    ),
    path(
        "dashboard/post/<int:post_id>/edit/",
        views.edit_post,
        name="edit_post"
    ),

    path(
        "dashboard/post/<int:post_id>/delete/",
        views.delete_post,
        name="delete_post"
    ),
]