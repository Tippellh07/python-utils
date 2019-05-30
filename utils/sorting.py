"""Sorting related utility functions"""

# standard library imports
import collections
import inspect
import logging
import typing

# use module logger
logger = logging.getLogger(__name__)


# =============================================================================#
# public functions


def sort_dict(unsorted: dict, key: typing.Callable, reverse: bool = False):
    """
    @brief  Sorts a dictionary using the provided key. Uses OrderedDict to
            allow compatibility with older python versions.

    @param  unsorted    The unsorted dictionary object.
    @param  key         The function to use for comparison, using index 1 on
                        the function arg equates to using the dict value. E.g.
                        lambda x: x[1]
    @param  reverse     Whether to return the dictionary in reverse order

    @return The sorted dictionary, or False on error.
    """
    if len(inspect.signature(key).parameters) > 1:
        logger.error(
            'invalid sorting key provided, key must take no more than 1 '
            'argument')
        return False

    return collections.OrderedDict(
        [(k, v) for k, v in sorted(
            unsorted.items(),
            key=key,
            reverse=reverse)])
