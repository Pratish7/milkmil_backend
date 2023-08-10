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
