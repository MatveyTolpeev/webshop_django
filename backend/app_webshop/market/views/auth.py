from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view

class CommonResponseSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class AuthView(APIView):
    """
        User login.
    """
    @swagger_auto_schema(
        request_body= LoginRequestSerializer,
        responses={200: CommonResponseSerializer}
    )
    def post(self, request):
        return Response(CommonResponseSerializer({
            'status': 0,
            'message': 'ok'
        }).data)

@api_view()
def hello(request):
    return Response({'status': 0, 'message': 'hello!'})
