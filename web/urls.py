## web/urls/py
## pkibuka@milky-way.space


from django.urls import path

from web import views

urlpatterns = [
    path("", views.index_view, name="home"),
    path("report_incident/", views.report_incident_view, name="report_incident"),
    path("incidents/", views.incidents_view, name="incidents"),
    path("neighborhood_watch", views.neighborhood_watch_view, name="neighborhood_watch"),
    path("safety_tips/", views.safety_tips_view, name="safety_tips"),
    path("emergency_services/", views.emergency_services_view, name="emergency_services"),
    path("how_it_works/", views.how_it_works_view, name="how_it_works"),
    path("about_us/", views.about_us_view, name="about_us"),
    path("FAQs/", views.faqs_view, name="faqs"),
    path("accounts/profile/", views.profile_view, name="profile"),
    # path("log-out/", views.signout_view, name="signout"),
]
