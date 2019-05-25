from rest_framework import routers
from backend.my_profile.api import \
    UserViewSet, \
    ProfileViewSet, \
    ProfilePicViewSet, \
    CVViewSet, \
    LinkViewSet, \
    AddressViewSet, \
    PhoneNumberViewSet, \
    EmailViewSet


router = routers.DefaultRouter()
router.register('user', UserViewSet, 'user')
router.register('profile', ProfileViewSet, 'profile')
router.register('profile_pic', ProfilePicViewSet, 'profile_pic')
router.register('cv', CVViewSet, 'cv')
router.register('address', AddressViewSet, 'address')
router.register('phone', PhoneNumberViewSet, 'phone')
router.register('email', EmailViewSet, 'email')

urlpatterns = router.urls
