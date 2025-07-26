from atria_registry import RegistryGroup
from atria_registry.module_builder import ModuleBuilder


class MetricBuilder(ModuleBuilder):
    pass


class MetricRegistryGroup(RegistryGroup):
    __registers_as_module_builder__ = True
    __module_builder_class__ = MetricBuilder
    __exclude_from_builder__ = {"num_classes", "device"}
