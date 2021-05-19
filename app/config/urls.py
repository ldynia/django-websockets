from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

from demo import views as demo_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
    path('ws/models/<str:model_name>', demo_views.index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
