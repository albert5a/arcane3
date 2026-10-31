from usuarios.models import Documentos
from django.shortcuts import get_object_or_404

def ocr_and_markdown_file(instance_id):
    from docling.document_converter import DocumentConverter

    documentos = get_object_or_404(Documentos, id=instance_id)

    converter = DocumentConverter()
    result = converter.convert(documentos.arquivo.path)
    doc = result.document
    texto = doc.export_to_markdown()
    
    documentos.content = texto
    documentos.save()