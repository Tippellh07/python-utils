#!/usr/bin/evn python
# -*- coding: utf-8 -*-
"""Example script to show some usage of the utilities in this repository."""

# standard library imports
import logging

# project imports
import utils.io
import utils.sorting

# default logging configuration
logging.basicConfig(
    level=logging.DEBUG,
    datefmt='%m/%d/%Y %H:%M:%S',
    format='[%(asctime)s] [%(levelname)8s] %(message)s')


# =============================================================================#
# entrypoint


if __name__ == '__main__':
    readme_content = utils.io.read_file(utils.io.relative_path('README.md'))
    if readme_content:
        print(readme_content)

    unsorted_dict = {1: '-', 3: '---', 2: '--'}
    print(utils.sorting.sort_dict(
        unsorted_dict,
        key=lambda item: len(item[1]),  # sort by length of value
        reverse=True))
    print(utils.sorting.sort_dict(unsorted_dict, key=lambda k: k))
