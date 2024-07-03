from django.views.generic.base import TemplateView


class WelcomeView(TemplateView):
    template_name = 'welcome.html'