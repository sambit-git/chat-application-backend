from django.contrib import admin

from .models import (Group,
                    GroupMembership,
                    GroupInvitation,
                    GroupMessages,
                    UserMessages,
                    BlockedUser)

admin.site.register(Group)
admin.site.register(GroupMembership)
admin.site.register(GroupInvitation)
admin.site.register(GroupMessages)
admin.site.register(UserMessages)
admin.site.register(BlockedUser)
