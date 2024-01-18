from rest_framework.serializers import ValidationError

from rest_framework.generics import CreateAPIView
from .serializers import (
    GroupSerializer,
    GroupInvitationSerializer,
    GroupMembershipSerializer,
    GroupMessageSerializer,
    UserMessageSerializer)

from .models import (
    Group,
    GroupMembership,
    GroupInvitation,
    GroupMessages,
    UserMessages
    )

class CreateGroupAPIView(CreateAPIView):
    queryset            = Group.objects.all()
    serializer_class    = GroupSerializer

    def perform_create(self, serializer):
        group = serializer.save()
        GroupMembership.objects.create(
            group=group, member=self.request.user, is_admin=True)

class AcceptGroupInviteAPIView(CreateAPIView):
    queryset            = GroupMembership.objects.all()
    serializer_class    = GroupMembershipSerializer

    def perform_create(self, serializer):
        group = serializer.validated_data['group']
        invitions = GroupInvitation.objects.filter(
            to_user=self.request.user, group=group)
        
        if invitions.exists():
            invitions.first().delete()
            serializer.save(group=group, member=self.request.user)
        else:
            raise ValidationError(
                "There are no existing invites for you in this group.")

class SendGroupInvitationAPIView(CreateAPIView):
    queryset            = GroupInvitation.objects.all()
    serializer_class    = GroupInvitationSerializer

    def perform_create(self, serializer):
        group = serializer.validated_data['group']
        from_user = self.request.user
        to_user = serializer.validated_data['to_user']

        already_member = group.users.filter(id=to_user.id).exists()
        already_invited = GroupInvitation.objects.filter(
            group=group, to_user=to_user).exists()
        
        if not (already_member or already_invited):
            serializer.save(from_user=from_user)

class CreateGroupMessageAPIView(CreateAPIView):
    queryset            = GroupMessages
    serializer_class    = GroupMessageSerializer

    def perform_create(self, serializer):
        return serializer.save(sender = self.request.user)

class CreateUserMessageAPIView(CreateAPIView):
    queryset            = UserMessages
    serializer_class    = UserMessageSerializer

    def perform_create(self, serializer):
        return serializer.save(sender = self.request.user)
