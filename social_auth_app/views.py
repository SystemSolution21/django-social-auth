from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "social_auth_app/home.html"
