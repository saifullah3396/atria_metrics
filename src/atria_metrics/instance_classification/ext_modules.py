from atria_metrics.instance_classification.output_transforms import _output_transform
from atria_metrics.registry import METRIC

METRIC.register_modules(
    module_paths=[f"ignite.metrics.{x}" for x in ["Accuracy"]],
    module_names=["accuracy"],
    output_transform=_output_transform,
    is_multilabel=False,
    device="cpu",
)

METRIC.register_modules(
    module_paths=[f"ignite.metrics.{x}" for x in ["Precision", "Recall"]],
    module_names=["precision", "recall"],
    output_transform=_output_transform,
    is_multilabel=False,
    average=True,
    device="cpu",
)
METRIC.register_modules(
    module_paths=[f"ignite.metrics.{x}" for x in ["ConfusionMatrix"]],
    module_names=["confusion_matrix"],
    output_transform=_output_transform,
    average="recall",
    device="cpu",
)
