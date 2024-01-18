from django.db import models
from django.contrib.auth import get_user_model

from varta.utils import upload_path

User = get_user_model()

class Group(models.Model):
    name    = models.CharField(max_length=255)
    
    photo   = models.ImageField(upload_to=upload_path,
                                null=True,
                                blank=True)
    
    users   = models.ManyToManyField(User,
                                     through='GroupMembership')

    def __str__(self) -> str:
        return self.name

class GroupMembership(models.Model):
    group               = models.ForeignKey(Group,
                              on_delete=models.CASCADE)
    
    member              = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name="groups")
    
    is_admin            = models.BooleanField(default=False)
    
    can_send_messages   = models.BooleanField(default=True)
    
    is_blocked          = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.group.name} : {self.member.get_username()}"

class GroupInvitation(models.Model):
    group       = models.ForeignKey(Group,
                                    on_delete=models.CASCADE)
    
    from_user   = models.ForeignKey(User,
                                    on_delete=models.CASCADE)
    
    to_user     = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name="group_invites")

    def __str__(self) -> str:
        from_ = self.from_user.get_username()
        to = self.to_user.get_username()
        group = self.group.name
        return f"{from_} invited {to} to join {group}"

class GroupMessages(models.Model):
    sender      = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name='sent_group_messages')
    
    group       = models.ForeignKey(Group,
                                    on_delete=models.CASCADE,
                                    null=True,
                                    blank=True,
                                    related_name="messages")
    
    text        = models.TextField()
    
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        sender = self.sender.get_username()
        group = self.group.name
        return f"Message from {sender} on Group {group}"

class UserMessages(models.Model):
    sender      = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name='sent_private_messages')
    
    receiver    = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name='received_private_messages',
                                    null=True,
                                    blank=True)
    
    text        = models.TextField()
    
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        sender = self.sender.get_username()
        receiver = self.receiver.get_username()
        return f"Message from {sender} to {receiver}"

class BlockedUser(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='blocked_users')
    
    blocked_user = models.ForeignKey(User,
                                     on_delete=models.CASCADE,
                                     related_name='blocking_users')

    def __str__(self) -> str:
        user = self.user.get_username()
        blocked_user = self.blocked_user.get_username()
        return f"{user} blocked {blocked_user}"
