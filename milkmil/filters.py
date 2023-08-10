from rest_framework import filters


class GuestsFilter(filters.BaseFilterBackend):
    """Filter that allows organizations to check for  company , facility floor or sector"""

    def filter_queryset(self, request, queryset, view):
            
        return queryset
    
