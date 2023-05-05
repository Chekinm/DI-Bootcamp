from django.contrib import admin
from django.urls import path, include
from polls.views import PostCreateView, PostListView, PostView, PostUpdateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include('accounts.urls')),
    path("polls/", include('polls.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
