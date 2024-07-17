from django_filters import rest_framework as filters
from .models import Topic


class TopicFilter(filters.FilterSet):
    id = filters.NumberFilter(lookup_expr='exact')
    title = filters.CharFilter(lookup_expr='icontains')
    is_active = filters.BooleanFilter(lookup_expr='exact')

    class Meta:
        model = Topic
        fields = ['id', 'title', 'is_active']
