from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

#Lead Viewset

class LeadViewSet(viewsets.ModelViewSet):

    #simple CRUD API for leads
    # queryset = Lead.objects.all()
    # permission_classes = [
    #     permissions.AllowAny
    # ]
    # serializer_class = LeadSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    serializer_class = LeadSerializer

    #get only the leads of that user
    def get_queryset(self):
        return self.request.user.leads.all()

    #only save the lead for the owner
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    