"""
Models Module

This module provides model-related utilities and components for the Atria framework. It includes model definitions, training interfaces, and utilities for managing neural network modules.

Submodules:
    - core: Core model implementations and utilities.
    - pipelines: Pipelines for specific model tasks.
    - utilities: Helper functions and classes for neural network modules.

Author: Saifullah
Date: April 14, 2025
"""

from atria_metrics.registry import METRIC, MetricBuilder

__all__ = ["METRIC", "MetricBuilder"]
