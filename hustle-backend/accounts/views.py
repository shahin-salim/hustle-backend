from .import signals
from .models import CustomUser
from rest_framework import status
from rest_framework.views import APIView
from services.models import ScopeAndPrice
from .serializer import CustomUserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from seller.models import SellerProfile


class SignUp(APIView):

    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            token = {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            }

            return Response(token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            print(request.data["refresh"])
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_205_RESET_CONTENT)


#
class UserView(APIView):
    """
    get the user details
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        data = dict(request.GET)
        print(data["users"])
        queryset = CustomUser.objects.filter(id__in=data['users'])

        print(queryset)

        serialzer = CustomUserSerializer(queryset, many=True).data

        return Response(serialzer, status=status.HTTP_200_OK)


# class GetUsersUsingSellerId(APIView):
#     """
#     get the user details
#     """
#     permission_classes = (AllowAny,)

#     def get(self, request):

#         queryset = ScopeAndPrice.objects.filter(id=request.GET["id"]).values(
#             "service_id__seller_id__user_id__username",
#             "service_id__seller_id__user_id",
#         )

#         print(queryset)

#         return Response(serialzer, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_routes(request):
    routes = [
        '/accounts/signup/',
        '/accounts/token/',
        '/accounts/token/refresh/',
        'seller/',
        'category/',
        'subcategory',
        'services/',
        'scope_and_price/'
    ]
    return Response(routes)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        print(user, "========================== refresh token")
        seller = SellerProfile.objects.filter(user_id=user)
        print(seller)
        if seller:
            # seller.is_seller = False
            # seller.save()
            # print(seller.id)
            token['seller_id'] = seller[0].id
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
