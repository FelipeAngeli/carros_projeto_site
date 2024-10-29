from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car

#instace = é o objeto que está sendo salvo
#sender = é nosso model, nosso objeto que está enviando esse evento para nosso signal


#receiver é uma funçao que esta ouvindo o sinal de pre_save

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    print('#### Car pre save signal ####')


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    print('#### Car post save signal ####')

@receiver(pre_delete, sender=Car)
def car_pre_delete(sender, instance, **kwargs):
    print('#### Car pre delete signal ####')

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    print('#### Car post delete signal ####')