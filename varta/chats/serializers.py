from rest_framework import serializers
from .models import (Group,
                     GroupMembership,
                     GroupInvitation,
                     GroupMessages,
                     UserMessages,
                     BlockedUser)

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class GroupMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMembership
        fields = '__all__'
        extra_kwargs = { 'member' : { 'required': False } }

class GroupInvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupInvitation
        fields = ['group', 'to_user']

class GroupMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMessages
        fields = '__all__'
        extra_kwargs = { 'sender' : { 'required': False } }

class UserMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMessages
        fields = '__all__'
        extra_kwargs = { 'sender' : { 'required': False } }

class BlockedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockedUser
        fields = '__all__'
        extra_kwargs = { 'user' : { 'required': False } }
