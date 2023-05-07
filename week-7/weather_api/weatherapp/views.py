from .models import Report
from .serializers import ReportSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAdminUser,
                                        IsAuthenticated,
                                        AllowAny)

# Create your views here.

class ReportView(APIView):

    permission_classes = (IsAdminUser,)

    def get(self, request, *arg, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            instance = Report.objects.get(id=pk)
            serializer = ReportSerializer(instance)
        else:
                
            queryset = Report.objects.all()
            serializer = ReportSerializer(queryset, many=True)
        return Response(serializer.data)
