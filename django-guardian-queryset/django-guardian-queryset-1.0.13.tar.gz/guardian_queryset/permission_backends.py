from guardian.backends import ObjectPermissionBackend


class ForeignKeyGuardianPermissionBackend(ObjectPermissionBackend):

    def has_perm(self, user_obj, perm, obj=None):
        if obj and getattr(obj, 'is_foreign_key_guardian', False):
            return user_obj == obj.user
        return False

