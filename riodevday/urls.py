from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('website.urls', namespace='website')),
    url(r'^colaboradores/', include('colaborators.urls', namespace='colaborators')),
    url(r'^patrocinadores/', include('sponsors.urls', namespace='sponsors')),
    url(r'^apoiadores/', include('supports.urls', namespace='supports')),
    url(r'^comunidades/', include('communities.urls', namespace='communities')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
