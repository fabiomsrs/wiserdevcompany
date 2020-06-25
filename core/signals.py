from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Post
from .utils import unique_slug_generator


@receiver(post_save, sender=Post)
def create_unique_slug(sender, instance, **kwargs):
    if not instance.slug:
       instance.slug = unique_slug_generator(instance)
       instance.save()