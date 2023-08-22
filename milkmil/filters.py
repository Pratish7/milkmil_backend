from rest_framework import filters


class GuestsFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        req_date = request.query_params.get('date', None)
        if req_date:
            queryset = queryset.filter(in_date=req_date)

        return queryset


class MilkFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        req_date = request.query_params.get('date', None)
        if req_date:
            queryset = queryset.filter(date=req_date)
        
        return queryset


class VehicleFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        return queryset


class KeyFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        return queryset


class ReturnableMaterialsFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        req_date = request.query_params.get('date', None)
        if req_date:
            queryset = queryset.filter(in_date=req_date)

        return queryset


class MasterDataFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        request_key = request.query_params.get('key', None)
        if request_key:
            queryset = queryset.filter(key=request_key)
        return queryset


class MaterialOutwardFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        req_date = request.query_params.get('date', None)
        if req_date:
            queryset = queryset.filter(date=req_date)

        return queryset


class MaterialInwardFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        req_date = request.query_params.get('date', None)
        if req_date:
            queryset = queryset.filter(date=req_date)

        return queryset
    

class GuestsInFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        queryset = queryset.filter(out_date__isnull=True, out_time__isnull=True)
        if 'type' in request.query_params:
            if request.query_params['type'] in ['organization', 'relationship']:
                if request.query_params['type'] == 'organization':
                    queryset = queryset.filter(relationship__isnull=True)
                elif request.query_params['type'] == 'relationship':
                    queryset = queryset.filter(organization__isnull=True)
        return queryset
    

class KeysQueue(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        queryset = queryset.filter(returned_time__isnull=True)
        return queryset


class MaterialInwardQueueFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        queryset = queryset.filter(out_time__isnull=True)
        return queryset
    

class MaterialOutwardQueueFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        queryset = queryset.filter(status='QUEUE')
        return queryset


class ReturnableMaterialsQueueFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):

        queryset = queryset.filter(status='YET TO BE RETURNED')
        return queryset
