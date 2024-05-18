import private_storage.urls
from django.conf import settings
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView
from rest_framework.routers import DefaultRouter, SimpleRouter

from app.api import views
from app.api.swagger import SwaggerView


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()


router.register("event", views.EventViewSet)
router.register("user", views.UserViewSet)
router.register("team", views.TeamViewSet)
# router.register("team_document_collection", views.TeamDocumentCollectionViewSet)
# router.register("team_document", views.TeamDocumentViewSet)
# router.register("research_summary", views.ResearchSummaryViewSet)
# router.register("research_note", views.ResearchNoteViewSet)
router.register("feedback", views.FeedbackViewSet)


# API URLS
app_name = "api"
urlpatterns = [
    path("status/", views.Status.as_view(), name="status"),
    path("", SwaggerView.as_view(url_name="api-schema"), name="api-docs"),
    path("schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path("accounts/", include("allauth.urls")),
    path("users/", include("app.users.urls", namespace="users")),
    path("feedback/", include("app.feedback.urls", namespace="feedback")),
    path("private-media/", include(private_storage.urls)),
] + router.urls
