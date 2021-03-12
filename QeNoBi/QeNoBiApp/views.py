# pages/views.py

from QeNoBi.settings import DEFAULT_DATASET, DEFAULT_DEMOGRAPHICS, DEFAULT_SANKEY_PARAMS, DEFAULT_GRANULARITY
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from mining_groups_behavior.handler import run_mining, experiment_name

from .models import *
from .sankey_experiments_handler import get_sankey_data


class SankeyView(TemplateView):
    template_name = 'index.html'

    @csrf_exempt
    def post(self, request):
        dataset = request.POST.get("dataset")
        products_properties = request.POST.getlist("products_properties")
        customers_properties = request.POST.getlist("customers_properties")
        time_granularity = request.POST.get("time_granularity")
        support = request.POST.get("support")
        products_min = request.POST.get("products_min")
        products_max = request.POST.get("products_max")
        exp_params = {
            "dataset": dataset,
            "time_granularity": time_granularity,
            "support": support,
            "properties": str(customers_properties),
            "itemsets_size": str([products_min, products_max]),
        }
        try:
            print(exp_params)
            sankey_experiment_id = run_mining(DEFAULT_DATASET, time_granularity, support, customers_properties,
                                              [products_min, products_max], overwrite=True)
        except Exception:
            sankey_experiment_id = experiment_name(exp_params)
        sankey_groups, sankey_links, periods = get_sankey_data(sankey_experiment_id)

        context = {
            "default_time_granularities": DEFAULT_GRANULARITY,
            "default_customers_properties": DEFAULT_DEMOGRAPHICS,
            'MiningGroupsExperiments': MiningGroupsExperiment.objects.all(),
            "products_min": products_min,
            "products_max": products_max,
            "support": support,
            "sankey_groups": sankey_groups,
            "sankey_links": sankey_links,
            "customers_properties": customers_properties,
            "time_granularity": exp_params["time_granularity"],
            "periods": periods,

        }
        return render(request, "index.html", context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exp_params = DEFAULT_SANKEY_PARAMS
        sankey_experiment_id = 'Retail_Y_100_[sex]_[1, None]'
        sankey_groups, sankey_links, periods = get_sankey_data(sankey_experiment_id)
        context.update({
            'MiningGroupsExperiments': MiningGroupsExperiment.objects.all(),
            "default_time_granularities": DEFAULT_GRANULARITY,
            "default_customers_properties": DEFAULT_DEMOGRAPHICS,
            "products_min": exp_params["itemsets_size"][0],
            "products_max": exp_params["itemsets_size"][1],
            "support": exp_params["support"],
            "sankey_groups": sankey_groups,
            "sankey_links": sankey_links,
            "customers_properties": exp_params["customers_properties"],
            "time_granularity": exp_params["time_granularity"],
            "periods": periods
        })
        return context
