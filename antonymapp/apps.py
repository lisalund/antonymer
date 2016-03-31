from django.apps import AppConfig


class AntonymappConfig(AppConfig):
    name = 'antonymapp'

	def ready(self):
		from . import signals