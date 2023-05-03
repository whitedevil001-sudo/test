
from .models import test
from .serializers import testserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['GET'])
def test_list(request):
    # Retrieve data from MyModel and serialize it
    data = test.objects.all()
    serializer = testserializer( data , many=True)
    return Response(serializer.data)
