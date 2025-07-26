_initialized = False


def init_registry():
    from atria_registry.module_registry import ModuleRegistry

    from atria_metrics.registry.registry_groups import MetricRegistryGroup

    global _initialized
    if _initialized:
        return
    _initialized = True
    ModuleRegistry().add_registry_group(
        name="METRIC",
        registry_group=MetricRegistryGroup(
            name="metric", default_provider="atria_metrics"
        ),
    )
