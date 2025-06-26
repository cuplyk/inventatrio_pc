from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class InventoryPageView(TemplateView):
    template_name = "pages/pc_inventory/workstation_inventory.html"
