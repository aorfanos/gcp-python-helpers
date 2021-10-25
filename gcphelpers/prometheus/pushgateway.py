from prometheus_client import CollectorRegistry, Gauge, push_to_gateway

def push_metrics_pushgateway(metric_name,
metric_desc,
pushgateway_url,
value,
labels,
label_values,
job="google-cloud-functions"):
  registry = CollectorRegistry()
  g = Gauge(metric_name, metric_desc, labels, registry=registry)
  g.labels(label_values).set(value)

  try:
      push_to_gateway(pushgateway_url, job=job, registry=registry)
  except Exception as e:
      print(f"Error: {e}")
      return e
