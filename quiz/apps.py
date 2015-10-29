from django.apps import AppConfig
from actstream import registry

class QuizConfig(AppConfig):
    name = 'quiz'
    verbose_name = "Quiz"

    def ready(self):
        registry.register(
        	self.get_model('Quiz'))