import reviews.views
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book-search/', reviews.views.book_search),
    path('', include('reviews.urls')),
]
