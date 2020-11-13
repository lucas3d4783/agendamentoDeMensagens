from django.db import models
from django.utils import timezone


class SocialNetwork(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Scheduling(models.Model):
    subject = models.CharField(max_length=45, null=False)
    receiver = models.CharField(max_length=45, null=False)
    message = models.TextField(max_length=500, null=False)
    date_time = models.DateTimeField(null=False, default='2020-01-01 12:00')
    status = models.BooleanField(default=0)

    social_network = models.ForeignKey(SocialNetwork, null=False,
                                        on_delete=models.CASCADE) #rede social para onde será enviado

    """def get_status(self):
        if self.status == 0:
            return 'A mensagem ainda não foi enviada para o destinatário! Porém ela está agendada para ' + self.data_hora 
        else:
            return 'A mensagem já foi enviada para o destinatário!'
    """

    def __str__(self):
        return self.subject
