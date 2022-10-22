from rest_framework.response import Response
from rest_framework import viewsets
from api.models import Incident,Description,Cve_number,Target
from .serializers import IncidentSerializer,TargetSerializer,DescriptionSerializer,CVESerializer
from datetime import datetime




class IncidentViewset(viewsets.ModelViewSet):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        cve = self.request.query_params.get('cve')
        queryset = self.queryset
        if start_date:
             queryset = queryset.filter(time_creation__gte=datetime.strptime(start_date,"%Y-%m-%d %H:%M:%S"))
        if end_date:
             queryset = queryset.filter(time_creation__lte=datetime.strptime(end_date,"%Y-%m-%d %H:%M:%S"))
        
        if end_date:
             queryset = queryset.filter(time_creation__lte=datetime.strptime(end_date,"%Y-%m-%d %H:%M:%S"))

        if cve:
            queryset = queryset.filter(cve_number__cve=cve)
        return queryset

class TargeViewset(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer



class DescriptionViewset(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer


class CveViewset(viewsets.ModelViewSet):
    queryset = Cve_number.objects.all()
    serializer_class = CVESerializer
