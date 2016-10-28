from rest_framework import permissions

class BelongsTo(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.account.id == request.user.account.id:
            return True
