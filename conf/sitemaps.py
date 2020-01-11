# learn about sitemaps here:https://docs.djangoproject.com/en/2.2/ref/contrib/sitemaps/

# from django.contrib import sitemaps
# from django.urls import reverse
# from apps.pages.models import *
#
# # Sample
# class ArticlesSitemap(sitemaps.Sitemap):
#     protocol = "https"
#
#     def items(self):
#         return  your_model.objects.all()
#
#     def location(self, item):
#         # change namespace:name as per yourneed or replace it with a complete url.
#         return reverse('namespace:name',kwargs={'slug':item.slug})
#
#     def lastmod(self,item):
#         return item.posted # posted is a datetime field
