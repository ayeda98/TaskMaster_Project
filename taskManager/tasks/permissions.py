from rest_framework import permissions

class IsLeaderOrReadOnly(permissions.BasePermission):
    """
    Permission personnalisée pour que seul le leader du groupe puisse modifier.
    """
    def has_object_permission(self, request, view, obj):
        # Les permissions sont autorisées à toute requête en lecture
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # L'autorisation est accordée uniquement si l'utilisateur est le leader du groupe
        return obj.leader == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permission personnalisée pour que seuls les créateurs ou les utilisateurs assignés puissent modifier leurs tâches.
    """
    def has_object_permission(self, request, view, obj):
        # Les permissions sont autorisées à toute requête en lecture
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # L'autorisation est accordée uniquement si l'utilisateur est le créateur ou l'assigné de la tâche
        return obj.created_by == request.user or obj.assigned_to == request.user
