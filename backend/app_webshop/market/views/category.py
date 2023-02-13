from rest_framework import serializers, viewsets, permissions

from market.models import Category

class CategorySerizalizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CategoryViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows users to read and modify categories
    """
    queryset = Category.objects.all().order_by('-id')
    serializer_class = CategorySerizalizer
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get', 'post', ]
