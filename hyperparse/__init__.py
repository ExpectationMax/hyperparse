# -*- coding: utf-8 -*-
"""Top-level package for HyperParse."""

__author__ = """Max Horn"""
__email__ = "maexlich@gmail.com"
__version__ = "0.1.0"

from argparse import (  # ArgumentParser,
    PARSER,
    SUPPRESS,
    Action,
    ArgumentDefaultsHelpFormatter,
    ArgumentError,
    ArgumentTypeError,
    FileType,
    HelpFormatter,
    MetavarTypeHelpFormatter,
    Namespace,
    RawDescriptionHelpFormatter,
    RawTextHelpFormatter,
)

from .hyperparse import ArgumentParser

__all__ = [
    "ArgumentParser",
    "Action",
    "Namespace",
    "FileType",
    "HelpFormatter",
    "RawDescriptionHelpFormatter",
    "RawTextHelpFormatter",
    "ArgumentDefaultsHelpFormatter",
    "MetavarTypeHelpFormatter",
    "SUPPRESS",
    "ArgumentError",
    "ArgumentTypeError",
    "PARSER",
]
