from atria_registry.module_registry import ModuleRegistry
from atria_registry.registry_group import RegistryGroup

_initialized = False


def init_registry():
    global _initialized
    if _initialized:
        return
    _initialized = True
    ModuleRegistry().add_registry_group(
        name="METRIC",
        registry_group=RegistryGroup(
            name="metric", is_factory=True, default_provider="atria_metrics"
        ),
    )
