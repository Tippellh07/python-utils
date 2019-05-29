#!/usr/bin/evn python
# -*- coding: utf-8 -*-

# standard library imports
import argparse
import logging
import unittest

# project imports
from test_cases.example_test_case import ExampleTestCase

# default logging configuration
logging.basicConfig(
    level=logging.CRITICAL,
    datefmt='%m/%d/%Y %H:%M:%S',
    format='[%(asctime)s] [%(levelname)8s] %(message)s')
logger = logging.getLogger(__name__)


# =============================================================================#
# public functions

def log_info(message: str):
    """
    @brief  Convenience function for logging info level messages when the
            module logger is set to a higher level.

    @param  message The message to log.
    """
    default_level = logger.level
    logger.setLevel(logging.INFO)
    logger.info(message)
    logger.setLevel(default_level)


def run_test_case(
        test_class: unittest.TestCase,
        verbose: bool = False,
        **kwargs):
    """
    @brief  Convenience function for running test cases with arguments.

    @param  test_class  The test class to run, should inherit from
                        unittest.TestCase.
    @param  verbose     Whether to run the test case in verbose mode.
    @param  kwargs      Keyword arguments to pass through to the test class.
    """
    test_loader = unittest.TestLoader()

    if verbose:
        test_suite = unittest.TestSuite()

    for test_name in test_loader.getTestCaseNames(test_class):
        if verbose:
            test_suite.addTest(test_class(test_name, *kwargs))
        else:
            result = test_class(test_name, **kwargs).run()
            if result.errors:
                logger.fatal(
                    'test failed with an error [test: "{test}", error:'
                    ' "{error}"]'.format(
                        test=test_name,
                        error=result.errors[0][1]))
                exit(1)
            elif result.failures:
                logger.fatal(
                    'test failed [test: "{test}", error: "{error}"]'.format(
                        test=test_name,
                        error=result.failures[0][1]))
                exit(1)

    if verbose:
        unittest.TextTestRunner().run(test_suite)


def parse_args():
    """
    @brief  Parse command line arguments.

    @return The parsed args object.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v',
        '--verbose',
        help='Whether to run in verbose mode.',
        action='store_true',
        default=False)
    parser.add_argument(
        '--example_arg',
        help='Example argument to pass to test case(s)',
        type=str,
        default='Example Arg')

    return parser.parse_args()

# =============================================================================#
# entrypoint


if __name__ == '__main__':
    """
    Using without verbose is designed to work well with continuous integration
    as it exits with an error causing CI pipelines to fail.

    Running without verbose also prevents all test cases being instantiated at
    once (which happens as a result of unittest's behaviour when running in
    verbose) which can cause issues when running tests on low powered CI agents.
    """
    args = parse_args()
    log_info('running example test case')
    run_test_case(
        ExampleTestCase,
        verbose=args.verbose,
        example_arg=args.example_arg)

    log_info('finished test cases')
