from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ComputerEngineering_1Request, ComputerEngineering_11Request,ComputerEngineering_2Request,ComputerEngineering_22Request
from .models import ComputerEngineering_3Request,ComputerEngineering_33Request,ComputerEngineering_32Request,ComputerEngineering_332Request
from .models import ComputerEngineering_4Request,ComputerEngineering_44Request,ComputerEngineering_42Request,ComputerEngineering_442Request
from .models import Cyber_security_1Request,Cyber_security_11Request


@receiver(post_save, sender=ComputerEngineering_1Request)
def create_computer_engineering_11_request(sender, instance, created, **kwargs):
    if created:
        ComputerEngineering_11Request.objects.create(name=instance)
        
        
@receiver(post_save, sender=ComputerEngineering_2Request)
def create_computer_engineering_22_request(sender, instance, created, **kwargs):
    if created:
        ComputerEngineering_22Request.objects.create(name=instance)
        
        
@receiver(post_save, sender=ComputerEngineering_3Request)
def create_computer_engineering_33_request(sender, instance, created, **kwargs):
    if created:
        ComputerEngineering_33Request.objects.create(name=instance)
        
@receiver(post_save, sender=ComputerEngineering_32Request)
def create_computer_engineering_332_request(sender, instance, created, **kwargs):
    if created:
        ComputerEngineering_332Request.objects.create(name=instance)


@receiver(post_save, sender=ComputerEngineering_4Request)
def create_computer_engineering_44_request(sender, instance, created, **kwargs):
    if created:
        ComputerEngineering_44Request.objects.create(name=instance)


@receiver(post_save, sender=ComputerEngineering_42Request)
def create_computer_engineering_442_request(sender, instance, created, **kwargs):
    if created:
        ComputerEngineering_442Request.objects.create(name=instance)
        

@receiver(post_save, sender=Cyber_security_1Request)
def create_security_11_request(sender, instance, created, **kwargs):
    if created:
        Cyber_security_11Request.objects.create(student=instance)