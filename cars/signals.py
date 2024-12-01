import logging
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import Car, CarInventory
from openai_api.client import get_car_ai_bio

logger = logging.getLogger(__name__)

def car_inventory_update():
    cars_count = Car.objects.count()
    
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value'] or 0.0
    
    logger.info(f"Atualizando inventário: cars_count={cars_count}, cars_value={cars_value}")
    
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        ai_bio = get_car_ai_bio(
            instance.model, 
            instance.brand.name, 
            instance.factory_year
        )
        instance.bio = ai_bio
        logger.info(f"Bio gerada pela AI para o carro {instance.model}: {instance.bio}")

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    logger.info(f"Carro salvo: {instance.model}. Atualizando inventário...")
    car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    logger.info(f"Carro excluído: {instance.model}. Atualizando inventário...")
    car_inventory_update()
