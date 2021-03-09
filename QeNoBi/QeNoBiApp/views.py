# pages/views.py
import os
from ast import literal_eval

from QeNoBi.settings import DEFAULT_DATASET, DEFAULT_PRODUCTS_MAX, DEFAULT_PRODUCTS_MIN, DEFAULT_DEMOGRAPHICS, \
    DEFAULT_GRANULARITY, DEFAULT_SUPPORT
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from mining_groups_behavior.handler import run_mining, experiment_name
from psycopg2._psycopg import IntegrityError
from sqlalchemy import create_engine

from .models import *
from .sankey_experiments_handler import get_sankey_data


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
    exp_params = {
        "dataset": "Retail",
        "time_granularity": time_granularity,
        "support": support,
        "properties": str(customers_properties),
        "itemsets_size": str([products_min, products_max]),
    }
    try:
        print(exp_params)
        sankey_experiment_id = run_mining(DEFAULT_DATASET, time_granularity, support, customers_properties,
                                          [products_min, products_max])
    except Exception:
        sankey_experiment_id = experiment_name(exp_params)
    sankey_groups, sankey_links = get_sankey_data(sankey_experiment_id)

    # df = get(dataset)
    # lcm_handler = LcmHandler()
    # lcm_handler.linear_closed_itemset_miner(df, frequency, min_support, itemsets_size, properties)
    context = {
        "default_time_granularities": DEFAULT_GRANULARITY,
        "default_customers_properties": DEFAULT_DEMOGRAPHICS,
        'MiningGroupsExperiments': MiningGroupsExperiment.objects.all(),
        "products_min": products_min,
        "products_max": products_min,
        "support": support,
        "sankey_groups": sankey_groups,
        "sankey_links": sankey_links,
        "customers_properties": customers_properties,
        "time_granularity": TimeGranularity.objects.all(),
    }

    return render(request, "index.html", context=context)


class SankeyView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dataset_name = DEFAULT_DATASET

        sankey_experiment_id = 'Retail_4M_100_[sex]_[1, None]'
        sankey_groups, sankey_links = get_sankey_data(sankey_experiment_id)
        context.update({
            'MiningGroupsExperiments': MiningGroupsExperiment.objects.all(),
            "default_time_granularities": DEFAULT_GRANULARITY,
            "default_customers_properties": DEFAULT_DEMOGRAPHICS,
            "products_min": DEFAULT_PRODUCTS_MIN,
            "products_max": DEFAULT_PRODUCTS_MAX,
            "support": DEFAULT_SUPPORT,
            "sankey_groups": sankey_groups,
            "sankey_links": sankey_links,
            "customers_properties": ["Gender"],
            "time_granularity": TimeGranularity.objects.all(),

            # "items_properties": DataSetDescription.objects.get(name=dataset_name).items_properties.all(),
        })
        return context
