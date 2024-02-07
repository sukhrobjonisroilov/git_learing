# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.generics import GenericAPIView
# from rest_framework.permissions import AllowAny, IsAuthenticated,IsAdminUser
# from rest_framework.response import Response
# from rest_framework.authtoken.models import Token
#
# from base.helper import MethodNot
# from core.models import User
# from core.serializer import UserSerializer
#

# class LoginView(GenericAPIView, MethodNot):
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         if 'email' not in data or 'password' not in data:
#             return Response({
#                 "error": "data to'liq emas"
#             })
#         user = User.objects.filter(email=data['email']).first()
#         if not user:
#             return Response({
#                 "error": "User mavjud emas"
#             })
#         if not user.check_password(data['password']):
#             return Response({
#                 "error": "parol xato "
#             })
#         token = Token.objects.get_or_create(user=user)[0]
#         return Response({
#             "result": token.key
#         })
#
#
# class RegisView(GenericAPIView):
#     serializer_class = UserSerializer
#     permission_classes = (AllowAny,)
#
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         password = data.get('password')
#         email = data.get('email')
#
#         serializer = self.serializer_class(data=data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         user.set_password(str(password))
#         user.save()
#         token = Token.objects.create(user=user)
#         return Response({
#             "result": token.key
#         })
#
#
# class LogoutView(GenericAPIView):
#     permission_classes = (IsAuthenticated,)
#     # authentication_classes = (TokenAuthentication,)
#
#     def post(self, request):
#         token = Token.objects.get(user=request.user)
#         token.delete()
#         return Response({
#             "succes": " Foydalanuvchi chiqarilib yuborildi"
#         })
