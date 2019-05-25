def update_filename_with_username(instance, filename):
    return "{}/{}_{}_{}".format(instance._meta.model.__name__,
                             instance.profile.user.username,
                             instance._meta.model.__name__,
                            filename
                               )
