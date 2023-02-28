import sys
from django.apps import AppConfig

started = False


class AppHooks(AppConfig):
    name = 'models'

    def ready(self) -> None:
        if 'runserver' not in sys.argv:
            return

        from endpoints.news.fetch_news_thread import start_background_thread
        start_background_thread()
