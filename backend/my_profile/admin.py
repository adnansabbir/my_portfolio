from django.contrib import admin
from backend.my_profile.models import \
    ProfilePic, \
    CV,\
    Link, \
    Address, \
    PhoneNumber, \
    Email


@admin.register(ProfilePic)
class ProfilePicAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'current')


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'current')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'name', 'link')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'address', 'type')


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'phone', 'type')


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'email', 'type')

