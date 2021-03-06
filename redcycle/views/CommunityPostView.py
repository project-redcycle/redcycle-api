from rest_framework import viewsets
from ..serializers.CommunityPostSerializer import *
from ..serializers.CommunityPostSerializer import *

class CommunityPostView(viewsets.ModelViewSet):
    queryset = CommunityPost.objects.all().order_by('creationDate')
    serializer_class = CommunityPostSerializer
    filterset_fields = ['authorId']
