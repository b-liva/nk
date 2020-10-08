import django_filters
from commitment.models import Commitment


class CommitmentFilter(django_filters.FilterSet):

    class Meta:
        model = Commitment
        fields = [
            'supporter',
            'caseworkder',
            'case',
        ]
