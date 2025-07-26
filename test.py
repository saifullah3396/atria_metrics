from atria_metrics import METRIC

x = METRIC.load_from_registry("f1_score")
print(x)
print(x())
