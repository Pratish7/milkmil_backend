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
