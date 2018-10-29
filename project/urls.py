from django.conf import settings
from django.conf.urls.static import static

from project.admin import admin_modullux
from django.urls import path, include

urlpatterns = [
    path('',            include(('backend.urls', 'backend'),    namespace='backend')),
    path('client/',     include(('client.urls', 'client'),      namespace='client')),
    path('admin/',      admin_modullux.urls),
]

# handler404 = 'project.errors.handler404'
# handler500 = 'project.errors.handler500'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

