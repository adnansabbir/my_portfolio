from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.common_helpers.update_filename import update_filename_with_username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=True, blank=True)
    sub_title = models.CharField(max_length=30, null=True, blank=True)
    bio = models.TextField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username


# All the models that need to have profile and user as foreign key will extend this model
class BaseUserProfile(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False)

    class Meta:
        abstract = True


class ProfilePic(BaseUserProfile):
    image = models.ImageField(upload_to=update_filename_with_username)
    current = models.BooleanField(default=True, blank=True)

    # Custom save method to set the current pic and unset current from previous pic if exist
    def save(self, *args, **kwargs):
        if self.current:
            try:
                current_pic = ProfilePic.objects.get(current=True, profile=self.profile)
                current_pic.current = False
                current_pic.save()
            except ProfilePic.DoesNotExist:
                pass
        super(ProfilePic, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.image)


class CV(BaseUserProfile):
    file = models.FileField(upload_to=update_filename_with_username)
    current = models.BooleanField(default=True, blank=True)

    # Custom save method to set the current cv and unset current from previous cv if exist
    def save(self, *args, **kwargs):
        if self.current:
            try:
                current_cv = CV.objects.get(current=True, profile=self.profile)
                current_cv.current = False
                current_cv.save()
            except CV.DoesNotExist:
                pass
        super(CV, self).save(*args, **kwargs)

    def __str__(self):
        return "{}".format(self.file)


class Link(BaseUserProfile):
    name = models.CharField(max_length=50, null=False, blank=False)
    link = models.CharField(max_length=100, null=True, blank=True)
    icon = models.ImageField(upload_to='links')

    def __str__(self):
        return "{}".format(self.name)


class Address(BaseUserProfile):
    city = models.CharField(null=True, blank=True, max_length=50)
    country = models.CharField(null=True, blank=True, max_length=50)
    address = models.CharField(null=True, blank=True, max_length=100)
    primary = models.BooleanField(null=True, blank=True, default=False)
    ADDRESS_TYPE = (
        ('T', 'Current Address'),
        ('P', 'Permanent Address'),
    )
    type = models.CharField(max_length=1, choices=ADDRESS_TYPE)

    def __str__(self):
        return "{},{},{}".format(self.address, self.city, self.country)


class PhoneNumber(BaseUserProfile):
    phone = models.CharField(max_length=20, null=False, blank=False)
    CONTACT_TYPE = (
        ('P', 'Primary'),
        ('T', 'Temporary'),
    )
    type = models.CharField(max_length=1, choices=CONTACT_TYPE)

    def __str__(self):
        return "{}".format(self.phone)


class Email(BaseUserProfile):
    email = models.CharField(max_length=50, null=False, blank=False)
    CONTACT_TYPE = (
        ('P', 'Primary'),
        ('T', 'Temporary'),
    )
    type = models.CharField(max_length=1, choices=CONTACT_TYPE)

    def __str__(self):
        return "{}".format(self.email)


# Adding a signal to create a profile instance on user creation
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()