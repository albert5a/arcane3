from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Documentos
from ia.tasks import ocr_and_markdown_file

@receiver(post_save, sender=Documentos)
def post_save_documentos(sender, instance, created, **kwargs):
    if created:
        markdown_text = ocr_and_markdown_file(instance.arquivo.path)
        print(f"Documento salvo: {instance.arquivo.name}, Tipo: {instance.tipo}, Data de Upload: {instance.data_upload}")
        print(f"Texto em Markdown: {markdown_text}")