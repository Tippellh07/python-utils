#!/usr/bin/evn python
# -*- coding: utf-8 -*-
"""Example script to show some usage of the utilities in this repository."""

# standard library imports
import logging

# project imports
import io_utils

# default logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    datefmt='%m/%d/%Y %H:%M:%S',
    format='[%(asctime)s] [%(levelname)8s] %(message)s')


# =============================================================================#
# entrypoint


if __name__ == '__main__':
    readme_content = io_utils.read_file(io_utils.relative_path('README.md'))
    if readme_content:
        print(readme_content)
