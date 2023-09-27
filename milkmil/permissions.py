from rest_framework.permissions import BasePermission

from milk_mil_backend.users.models import UserTypes


class CanWriteGuest(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        user_permissions = []
        perms = UserTypes.objects.filter(user=request.user)
        for i in perms:
            user_permissions.append(i.id)
        if 14 in user_permissions or 1 in user_permissions or 10 in user_permissions:
            return True
        return False
    

class CanWriteMilk(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        user_permissions = []
        perms = UserTypes.objects.filter(user=request.user)
        for i in perms:
            user_permissions.append(i.id)
        if 14 in user_permissions  or 1 in user_permissions or 10 in user_permissions:
            return True
        return False
    

class CanWriteVehicle(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        user_permissions = []
        perms = UserTypes.objects.filter(user=request.user)
        for i in perms:
            user_permissions.append(i.id)
        if 14 in user_permissions or 11 in user_permissions or 1 in user_permissions or 10 in user_permissions:
            return True
        return False
    

class CanWriteVehicleVendor(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        user_permissions = []
        perms = UserTypes.objects.filter(user=request.user)
        for i in perms:
            user_permissions.append(i.id)
        if 14 in user_permissions or 1 in user_permissions or 10 in user_permissions or 17 in user_permissions:
            return True
        return False
    

class CanWriteKeys(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        user_permissions = []
        perms = UserTypes.objects.filter(user=request.user)
        for i in perms:
            user_permissions.append(i.id)
        if 14 in user_permissions or 1 in user_permissions or 10 in user_permissions:
            return True
        return False
    

class CanWriteReturnableMaterials(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        user_permissions = []
        perms = UserTypes.objects.filter(user=request.user)
        for i in perms:
            user_permissions.append(i.id)
        if 14 in user_permissions or 1 in user_permissions or 10 in user_permissions:
            return True
        return False
    

class CanWriteMasterData(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        user_permissions = []
        perms = UserTypes.objects.filter(user=request.user)
        for i in perms:
            user_permissions.append(i.id)
        if 1 in user_permissions or 1 in user_permissions or 10 in user_permissions:
            return True
        return False
    
class CanWriteMaterialOutward(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        user_permissions = []
        perms = UserTypes.objects.filter(user=request.user)
        for i in perms:
            user_permissions.append(i.id)
        if 14 in user_permissions or 1 in user_permissions or 10 in user_permissions:
            return True
        return False
    

class CanWriteMaterialInward(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        user_permissions = []
        perms = UserTypes.objects.filter(user=request.user)
        for i in perms:
            user_permissions.append(i.id)
        if 14 in user_permissions or 1 in user_permissions or 10 in user_permissions:
            return True
        return False
    

class CanViewReport(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        user_permissions = []
        perms = UserTypes.objects.filter(user=request.user)
        for i in perms:
            user_permissions.append(i.id)
        if 13 in user_permissions or 1 in user_permissions or 10 in user_permissions:
            return True
        return False


class CanGenerateBarCode(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        user_permissions = []
        perms = UserTypes.objects.filter(user=request.user)
        for i in perms:
            user_permissions.append(i.id)
        if 16 in user_permissions or 1 in user_permissions or 10 in user_permissions:
            return True
        return False