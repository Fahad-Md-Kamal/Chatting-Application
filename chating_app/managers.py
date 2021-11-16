from django.db import models
from django.db.models import Count
from django.contrib.auth import get_user_model

User = get_user_model()


class ThreadManager(models.Manager):
    '''Responsible for filtering or creating new threades'''

    def get_or_create_personal_thread(self, user1, user2):
        ''' Get or Create a thread with provided users '''
        threads = self.get_queryset().filter(thread_type='personal')
        threads = threads.filter(users__in=[user1, user2]).distinct()
        threads = threads.annotate(u_count=Count('users')).filter(u_count=2)
        if threads.exists():
            return threads.first()
        else:
            thread = self.create(thread_type='personal')
            thread.users.add(user1)
            thread.users.add(user2)
            return thread

    def by_user(self, user):
        ''' Get all threads for the given user '''
        return self.get_queryset().filter(users__in=[user])

    def get_thread_by_users(self, user1, user2):
        ''' Get all threads for given users '''
        threads = self.get_queryset().filter(thread_type='personal')
        threads = threads.filter(users__in=[user1, user2]).distinct()
        threads = threads.annotate(u_count=Count('users')).filter(u_count=2)
        if threads.exists():
            return threads.first()
            