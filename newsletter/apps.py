from django.apps import AppConfig
# from asgiref.sync import sync_to_async


class NewsletterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'newsletter'
    
    # def ready(self):
    #     from . import tasks
    #     sync_to_async(tasks.interval_schedule)()
