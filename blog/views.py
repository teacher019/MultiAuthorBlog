from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import Post, Category, Tag, AuthorProfile, Comment, Like
from .forms import PostForm

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "blog/signup.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "blog/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home")

def home(request):
    query = request.GET.get("q", "").strip()

    posts = (
        Post.objects
        .filter(status=Post.Status.PUBLISHED)
        .select_related("author", "category")
        .prefetch_related("tags")
        .annotate(
            comment_count=Count("comments", distinct=True),
            like_count=Count("likes", distinct=True),
        )
    )

    if query:
        posts = posts.filter(
            Q(title__icontains=query)
            | Q(content__icontains=query)
            | Q(category__name__icontains=query)
            | Q(tags__name__icontains=query)
            | Q(author__username__icontains=query)
        ).distinct()

    posts = posts.order_by("-created_at")

    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "categories": Category.objects.all(),
        "tags": Tag.objects.all(),
        "query": query,
    }

    return render(request, "blog/home.html", context)


def post_detail(request, slug):
    post = get_object_or_404(
        Post.objects
        .filter(status=Post.Status.PUBLISHED)
        .select_related("author", "category")
        .prefetch_related("tags"),
        slug=slug
    )

    post.view_count += 1
    post.save(update_fields=["view_count"])

    comments = post.comments.select_related("user").all()

    liked = False

    if request.user.is_authenticated:
        liked = Like.objects.filter(
            post=post,
            user=request.user
        ).exists()

    context = {
        "post": post,
        "comments": comments,
        "liked": liked,
    }

    return render(request, "blog/post_detail.html", context)


@login_required
def add_comment(request, slug):
    if request.method == "POST":
        post = get_object_or_404(
            Post,
            slug=slug,
            status=Post.Status.PUBLISHED
        )

        text = request.POST.get("text", "").strip()

        if text:
            Comment.objects.create(
                post=post,
                user=request.user,
                text=text
            )

    return redirect("post_detail", slug=slug)


@login_required
def toggle_like(request, slug):
    
    post = get_object_or_404(
        Post,
        slug=slug,
        status=Post.Status.PUBLISHED
    )

    like = Like.objects.filter(
        post=post,
        user=request.user
    ).first()

    if like:
        like.delete()
    else:
        Like.objects.create(
            post=post,
            user=request.user
        )

    return redirect("post_detail", slug=slug)

@login_required
def author_dashboard(request):
    profile = get_object_or_404(
        AuthorProfile,
        user=request.user,
        is_author=True
    )

    posts = (
        Post.objects
        .filter(author=request.user)
        .select_related("category")
        .prefetch_related("tags")
        .order_by("-created_at")
    )

    total_posts = posts.count()
    published_posts = posts.filter(
        status=Post.Status.PUBLISHED
    ).count()
    draft_posts = posts.filter(
        status=Post.Status.DRAFT
    ).count()

    total_views = sum(post.view_count for post in posts)

    context = {
        "profile": profile,
        "posts": posts,
        "total_posts": total_posts,
        "published_posts": published_posts,
        "draft_posts": draft_posts,
        "total_views": total_views,
    }

    return render(
        request,
        "blog/author_dashboard.html",
        context
    )
@login_required
def create_post(request):

    profile = get_object_or_404(
        AuthorProfile,
        user=request.user,
        is_author=True
    )

    if request.method == "POST":
        form = PostForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()

            return redirect("author_dashboard")

    else:
        form = PostForm()

    context = {
        "form": form,
        "profile": profile,
    }

    return render(
        request,
        "blog/post_form.html",
        context
    )
@login_required
def edit_post(request, post_id):

    profile = get_object_or_404(
        AuthorProfile,
        user=request.user,
        is_author=True
    )

    post = get_object_or_404(
        Post,
        id=post_id,
        author=request.user
    )

    if request.method == "POST":
        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():
            form.save()
            return redirect("author_dashboard")

    else:
        form = PostForm(instance=post)

    context = {
        "form": form,
        "profile": profile,
        "post": post,
        "edit_mode": True,
    }

    return render(
        request,
        "blog/post_form.html",
        context
    )


@login_required
def delete_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id,
        author=request.user
    )

    if request.method == "POST":
        post.delete()
        return redirect("author_dashboard")

    context = {
        "post": post,
    }

    return render(
        request,
        "blog/post_confirm_delete.html",
        context
    )