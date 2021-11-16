from django.db import models
from django.db import models

from django.contrib.auth import get_user_model

from .managers import ThreadManager

User = get_user_model()


class Thread(models.Model):
    '''Responsible for storing Message Treades'''
    THREAD_TYPE = (
        ('personal', 'Personal'),
        ('group', 'Group')
    )

    name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    thread_type = models.CharField(
        max_length=15,
        choices=THREAD_TYPE,
        default='group'
    )
    users = models.ManyToManyField(
        User,
        related_name='thread_users'
    )

    objects = ThreadManager()

    def __str__(self) -> str:
        if self.thread_type == 'personal' and self.users.count() == 2:
            return f'{self.users.first()} and {self.users.last()}'
        return f'{self.name}'


class Message(models.Model):
    ''' Responsible for storing Chat Messages '''
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return f'From <Thread - {self.thread}>'
