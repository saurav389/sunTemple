from django.apps import AppConfig


class SetupprofileConfig(AppConfig):
    name = 'setupprofile'
    def ready(self):
        import users.signals
