import json
import uuid

import petl as etl
from django.conf import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import Dataset
from .resources import get_all_results, get_planets


def index(request):
    context = {"datasets": Dataset.objects.all()}
    return render(request, "characters/index.html", context)


def dataset(request, pk):
    dataset = get_object_or_404(Dataset, pk=pk)
    table = etl.fromcsv(dataset.path)
    explore = request.GET.get("explore", [])
    fields = etl.header(table)
    limit = int(request.GET.get("limit", "10"))
    if explore:
        explore = explore.split(",")
        if len(explore) > 1:
            table = etl.aggregate(table, key=explore, aggregation=len, value=explore).rename(
                "value", "count"
            )
        show_load_more = False
    else:
        table = etl.head(table, limit)
        show_load_more = limit < len(table)
    html = etl.MemorySource()
    table.addrownumbers().tohtml(html)
    html = html.getvalue().decode().replace("class='petl'", "class='table table-striped'")
    context = {
        "dataset": dataset,
        "dataset_html": html,
        "explore": explore,
        "fields": fields,
        "limit": limit + 10,
        "show_load_more": show_load_more,
    }
    return render(request, "characters/dataset.html", context)


def download(request):
    planets = get_planets()
    source = etl.MemorySource(json.dumps(get_all_results("people")).encode())
    path = settings.MEDIA_ROOT / "characters" / f"{uuid.uuid4()}.csv"
    etl.fromjson(source).cutout(
        "films", "vehicles", "starships", "species", "created", "url"
    ).convert("homeworld", lambda v: planets[v]).convert(
        "edited", lambda v: etl.datetimeparser("%Y-%m-%dT%H:%M:%S.%fZ")(v).date()
    ).rename(
        "edited", "date"
    ).tocsv(
        path
    )
    dataset = Dataset.objects.create(path=path)
    messages.success(request, f"Added new dataset fetched on {dataset.created_at:%c}.")
    return redirect("characters:index")
