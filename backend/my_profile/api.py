from backend.my_profile.models import \
    User, \
    Profile, \
    ProfilePic, \
    CV, \
    Link, \
    Address, \
    PhoneNumber, \
    Email
from rest_framework import viewsets, permissions
from backend.my_profile.serializers import UserSerializer, \
    ProfilePicSerializer, \
    CVSerializer, \
    ProfileSerializer, \
    LinkSerializer, \
    AddressSerializer, \
    PhoneNumberSerializer, \
    EmailSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().select_related('profile')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().select_related('user')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProfileSerializer


class ProfilePicViewSet(viewsets.ModelViewSet):
    queryset = ProfilePic.objects.all().select_related('profile')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProfilePicSerializer


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all().select_related('profile')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CVSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all().select_related('profile')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LinkSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().select_related('profile')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AddressSerializer


class PhoneNumberViewSet(viewsets.ModelViewSet):
    queryset = PhoneNumber.objects.all().select_related('profile')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PhoneNumberSerializer


class EmailViewSet(viewsets.ModelViewSet):
    queryset = Email.objects.all().select_related('profile')
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = EmailSerializer
