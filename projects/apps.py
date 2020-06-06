from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    name = 'projects'

    def ready(self):
        """
        method import creatd signals
        """
        import projects.signals
