import sys
from django.apps import AppConfig

started = False


class AppHooks(AppConfig):
    name = 'models'

    def ready(self):
        if 'runserver' not in sys.argv:
            return True

        from endpoints.news.fetch_news_thread import start_background_thread
        start_background_thread()
