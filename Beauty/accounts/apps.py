from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Beauty.accounts'

    def ready(self):
        import Beauty.accounts.signals
        result = super().ready()
        return result