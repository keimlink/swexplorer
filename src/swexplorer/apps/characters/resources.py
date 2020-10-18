import logging

import clients
from django.conf import settings

logger = logging.getLogger(__name__)


def get_all_results(url):
    resource = clients.Resource(settings.SWAPI_URL)
    results = []
    while url:
        logger.debug("Current SWAPI URL: %s", url)
        data = resource.get(url)
        logger.debug("Fetched %s items", len(data["results"]))
        results += data["results"]
        url = data["next"]
    return results


def get_planets():
    return {planet["url"]: planet["name"] for planet in get_all_results("planets")}
