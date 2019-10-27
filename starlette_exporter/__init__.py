import os
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, REGISTRY, multiprocess, CollectorRegistry
from starlette.responses import Response

from .middleware import PrometheusMiddleware

def handle_metrics(request):
    """ A handler to expose Prometheus metrics
        Example usage:

        ```
        app.add_middleware(PrometheusMiddleware)
        app.add_route("/metrics", handle_metrics)
        ```
    """
    registry = REGISTRY
    if 'prometheus_multiproc_dir' in os.environ:
        registry = CollectorRegistry()
        multiprocess.MultiProcessCollector(registry)
    
    headers = {'Content-Type': CONTENT_TYPE_LATEST}
    return Response(generate_latest(), status_code=200, headers=headers)
