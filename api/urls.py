# django imports
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# REST API imports
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

# schema view
schema_view     = get_schema_view(title="FIBONACCI API")
# documentation view
document_view   = include_docs_urls(title='Fibonacci API', public=False)


urlpatterns = [
    # index
    path('', views.index, name='index'),

    # to see the schema
    path('schema/', schema_view),

    # REST API documentation
    path('api/', document_view),

    # POST customer_inputs to generate recommentations
    path('api/calculate/', views.FibonacciViewSet.as_view(), name='calculate'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
