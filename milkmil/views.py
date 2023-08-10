from rest_framework import viewsets, mixins
from milkmil.models import Guests
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from milkmil.serializers import GuestsSerializer
from rest_framework.filters import SearchFilter
from milkmil.filters import GuestsFilter


class GuestsView(viewsets.GenericViewSet,  mixins.ListModelMixin, mixins.CreateModelMixin):
    """Manage Facilities in the Database"""
    authentication_classes = (TokenAuthentication, SessionAuthentication, JWTAuthentication)
    permission_classes = ()
    queryset = Guests.objects.all()
    serializer_class = GuestsSerializer
    filter_backends = [GuestsFilter, SearchFilter]
    search_fields = ['id', 'visitor_name', 'employee_name', 'relationship', 'in_time', 'out_time']

