from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import product

@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'product_demo'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = product
         fields = [
             'name',
             'description',
             'image',
         ]