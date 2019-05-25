from rest_framework import serializers
from backend.my_profile.models import User, Profile, ProfilePic, CV, Link, Address, \
    PhoneNumber, Email


# Profile Serializer
class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'bio',
            'user',
        )


# UserSerializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'profile',
        )


# ProfilePicSerializer
class ProfilePicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProfilePic
        fields = (
            'id',
            'image',
            'current',
            'profile',
        )


# CVSerializer
class CVSerializer(serializers.ModelSerializer):

    class Meta:
        model = CV
        fields = (
            'id',
            'file',
            'current',
            'profile',
        )


# LinkSerializer
class LinkSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Link
        fields = (
            'id',
            'name',
            'link',
            'icon',
            'profile',
        )


# AddressSerializer
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Address
        fields = (
            'id',
            'city',
            'country',
            'address',
            'primary',
            'type',
            'profile',
        )


# PhoneNumberSerializer
class PhoneNumberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PhoneNumber
        fields = (
            'id',
            'phone',
            'type',
            'profile',
        )


# EmailSerializer
class EmailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Email
        fields = (
            'id',
            'email',
            'type',
            'profile',
        )



