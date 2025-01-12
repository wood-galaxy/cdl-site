from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from django.contrib import admin

import symposion.views


WIKI_SLUG = r"(([\w-]{2,})(/[\w-]{2,})*)"


urlpatterns = patterns(
    "",
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^robots\.txt$", TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    url(r"^account/signup/$", symposion.views.SignupView.as_view(), name="account_signup"),
    url(r"^account/login/$", symposion.views.LoginView.as_view(), name="account_login"),
    url(r"^account/", include("account.urls")),

    url(r"^conference/", include("symposion.conference.urls")),

    url(r"^dashboard/", symposion.views.dashboard, name="dashboard"),
    # url(r"^intervenant/", include("cdl.speakers.urls")),
    url(r"^intervenant/", include("symposion.speakers.urls")),
    # url(r"^speaker/", include("cdl.speakers.urls")),
    url(r"^speaker/", include("symposion.speakers.urls")),
    url(r"^proposals/", include("symposion.proposals.urls")),
    url(r"^sponsors/", include("symposion.sponsorship.urls")),
    url(r"^partenariat/", include("symposion.sponsorship.urls")),
    url(r"^boxes/", include("symposion.boxes.urls")),

    # url(r"^teams/", include("cdl.teams.urls")),
    url(r"^teams/", include("symposion.teams.urls")),

    url(r"^reviews/", include("symposion.reviews.urls")),
    # url(r"^coverage/", include("cdl.coverage.urls")),
    # url(r"^subscribe/", include("cdl.subscription.urls")),
    # url(r"^schedule/", include("cdl.schedule.urls")),
    # url(r"^programme/", include("cdl.schedule.urls")),

    url(r"^schedule/", include("symposion.schedule.urls")),
    url(r"^programme/", include("symposion.schedule.urls")),
    url(r"^conference/", include("symposion.conference.urls")),
    # url(r"^badges/", include("cdl.badges.urls")),
    url(r"^markitup/", include("markitup.urls")),

    url(r"^", include("symposion.cms.urls")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
