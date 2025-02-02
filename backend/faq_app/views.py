from rest_framework import viewsets
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from django.views.generic import TemplateView

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        return FAQ.objects.all().order_by('-created_at')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        # Get language from query parameter, default to 'en'
        context['lang'] = self.request.query_params.get('lang', 'en')
        return context

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        # Get language from query parameter
        lang = request.query_params.get('lang', 'en')
        # Pass language in context
        serializer = self.get_serializer(queryset, many=True, context={'lang': lang})
        return Response(serializer.data)

class FAQListView(TemplateView):
    template_name = 'faq_app/faq_list.html'
