from pyrestorm.models import RestModel
from pyrestorm.paginators import DjangoRestFrameworkLimitOffsetPaginator


class Post(RestModel):
    class Meta:
        url = 'http://jsonplaceholder.typicode.com/posts'


class Gene(RestModel):
    class Meta:
        paginator_class = DjangoRestFrameworkLimitOffsetPaginator
        slug_field = 'ens_gene'
        url = 'https://api.genepeeks.com/genes/'


class Subject(RestModel):
    class Meta:
        paginator_class = DjangoRestFrameworkLimitOffsetPaginator
        slug_field = 'key'
        token = 'INVALIDTOKEN'
        url = 'https://api.genepeeks.com/subjects/'
