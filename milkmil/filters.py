from rest_framework import filters


class GuestsFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        return queryset


class MilkFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        return queryset


class VehicleFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        return queryset


class KeyFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        return queryset


class ReturnableMaterialsFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        return queryset


class MasterDataFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        request_key = request.query_params.get('key', None)
        if request_key:
            queryset = queryset.filter(key=request_key)
        return queryset


class MaterialOutwardFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        return queryset


class MaterialInwardFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        return queryset
    

class GuestsInFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        queryset = queryset.filter(out_date__isnull=True, out_time__isnull=True)
        return queryset


class MaterialInwardQueueFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        queryset = queryset.filter(out_time__isnull=True)
        return queryset
    

class MaterialOutwardQueueFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        queryset = queryset.filter(status='QUEUE')
        return queryset
    