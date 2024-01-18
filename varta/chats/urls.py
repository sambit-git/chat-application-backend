from django.urls import path
from .views import (
    CreateGroupAPIView,
    SendGroupInvitationAPIView,
    AcceptGroupInviteAPIView,
    CreateGroupMessageAPIView,
    CreateUserMessageAPIView)

app_name = 'chats'

urlpatterns = [
    path('groups/create', CreateGroupAPIView.as_view(), name='create-group'),
    path('groups/invite', SendGroupInvitationAPIView.as_view(), name='send-group-invite'),
    path('groups/accept', AcceptGroupInviteAPIView.as_view(), name='accept-group-invite'),
    path('groups/send_message', CreateGroupMessageAPIView.as_view(), name='send-group-message'),
    path('send_message', CreateUserMessageAPIView.as_view(), name='send-private-message'),
]
