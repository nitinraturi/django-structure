from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Learn about sitemaps here: https://docs.djangoproject.com/en/2.2/ref/contrib/sitemaps/
# from django.contrib.sitemaps.views import sitemap
# from .sitemaps import ArticlesSitemap
# sitemaps = {
#     'first_sitemap': ArticlesSitemap,
# }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls',namespace="users")),

    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
    #      name='django.contrib.sitemaps.views.sitemap'),

    path('',include('apps.pages.urls', namespace="pages")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
