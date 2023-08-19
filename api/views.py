from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView
from .tests import *
from rest_framework.response import Response
from core.getSalesTaxData import searchTaxData, stateName
# Create your views here.


class SalesTaxDataView(APIView):
    def get(self, request, zipcode=None, state=None):
        if zipcode:
            zipCode = zipcode
            try:
                df = searchTaxData(zipcode=zipcode)
                state = df.state.values[0]
                combined_rate = df.combined_rate.values[0]
                local_rate = df.local_rate.values[0]
                state_rate = df.state_rate.values[0]
                population = df.population.values[0]
            except:
                return Response({"error": "Please enter a valid zipcode."}, status=400)
            data = SalesTaxDataTest(
                zipCode, state, combined_rate, local_rate, state_rate, population)
            serializer = SalesTaxDataSerializer(data)
            return Response({**serializer.data}, status=200)
        elif state:
            state = state.replace("+", " ")
            try:
                zipCode = ""
                df = searchTaxData(state=state)
                state = df.state.values[0]
                combined_rate = df.combined_rate.values[0]
                local_rate = df.local_rate.values[0]
                state_rate = df.state_rate.values[0]
                population = df.population.values[0]
            except:
                return Response({"error": "Please enter a valid state."}, status=400)
            data = SalesTaxDataTest(
                zipCode, state, combined_rate, local_rate, state_rate, population)
            serializer = SalesTaxDataSerializer(data)
            return Response({**serializer.data}, status=200)
        else:
            return Response({"error": "Please enter a zipcode or state."}, status=400)
