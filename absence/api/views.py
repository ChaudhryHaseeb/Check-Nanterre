

# Permet de récupérer l'utilisateur associé à un token
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from absence.api.serializers import PromotionSerializer
from absence.models import Promotion


@api_view(['GET', ])
@permission_classes([IsAuthenticated])
def get_all_promotions(request):
    try:
        promotions = Promotion.objects.all()
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = PromotionSerializer(promotions, many=True)
        return Response(serializer.data)

