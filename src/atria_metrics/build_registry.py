"""
Build Registry Script

This script is responsible for building the registry of modules used in the Atria project. It imports various components from the Atria framework and writes the registry configuration to YAML files.

Usage:
    Run this script to generate the registry configuration files in the `conf` directory.

Modules Imported:
    - Core utilities for registry management.
    - Data batch samplers, pipelines, and storage managers.
    - Model definitions and pipelines.
    - Task pipelines for training and evaluation.
    - Training optimizers and schedulers.

Author: Saifullah
Date: April 14, 2025
"""

from pathlib import Path

from atria_registry.utilities import write_registry_to_yaml  # noqa

from atria_metrics.detection.cocoeval import *  # noqa
from atria_metrics.instance_classification.ext_modules import *  # noqa
from atria_metrics.instance_classification.f1_score import *  # noqa
from atria_metrics.layout.f1_score import *  # noqa
from atria_metrics.layout.precision import *  # noqa
from atria_metrics.layout.recall import *  # noqa
from atria_metrics.qa.anls import *  # noqa
from atria_metrics.qa.sequence_anls import *  # noqa

if __name__ == "__main__":
    write_registry_to_yaml(str(Path(__file__).parent / "conf"), types=["metric"])
