# -*- encoding: utf-8 -*-
from rest_framework import permissions

class hasPermission(permissions.BasePermission):
    """
    Customized Permission
    """
    def has_permission(self, request, view):
        """check if user make request can modified Quiz"""
        return request.user.has_perm('quiz.add_quiz')
