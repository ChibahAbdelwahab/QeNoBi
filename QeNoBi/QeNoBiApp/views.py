# pages/views.py
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from .models import *
from QeNoBi.settings import DEFAULT_DATASET, DEFAULT_PRODUCTS_MAX, DEFAULT_PRODUCTS_MIN, DEFAULT_DEMOGRAPHICS, \
    DEFAULT_GRANULARITY, DEFAULT_SUPPORT


@csrf_exempt
def handle_post(request):
    dataset = request.POST.get("dataset")
    demographics = request.POST.getlist('demographics')
    period = [request.POST.get("date_min"), request.POST.get("date_max")]
    products_properties = request.POST.get("products_properties")
    customers_properties = request.POST.get("customers_properties")
    time_granularity = request.POST.get("time_granularity")
    support = request.POST.get("support")
    products_min = request.POST.get("products_min")
    products_max = request.POST.get("product_max")
    # df = get(dataset)
    # lcm_handler = LcmHandler()
    # lcm_handler.linear_closed_itemset_miner(df, frequency, min_support, itemsets_size, properties)

    return HttpResponse(str("d"))
    context = {"datasets": DataSetDescription.objects.all()}
    return render(request, "test.html", context=context)


class SankeyView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dataset_name = DEFAULT_DATASET
        context.update({
            'MiningGroupsExperiments': MiningGroupsExperiment.objects.all(),
            "default_granularity": DEFAULT_GRANULARITY,
            "default_demographics": DEFAULT_DEMOGRAPHICS,
            "products_min": DEFAULT_PRODUCTS_MIN,
            "products_max": DEFAULT_PRODUCTS_MAX,
            "support": DEFAULT_SUPPORT,
            "time_granularities": TimeGranularity.objects.all(),
            "customers_properties": DataSetDescription.objects.get(name=dataset_name).customers_properties.all(),
            "items_properties": DataSetDescription.objects.get(name=dataset_name).items_properties.all(),
        })
        return context
