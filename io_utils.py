"""File IO related utility functions"""

# standard library imports
import logging
import inspect
import os

# use module logger
logger = logging.getLogger(__name__)


# =============================================================================#
# public functions


def read_file(file_name: str, mode: str = 'r'):
    """
    @brief  Safely read a file, catching any potential exceptions.

    @param  file_name   The path to the file to read.
    @param  mode        The mode to open the file in.

    @return     The content of the given file if successful, otherwise False.
    """
    try:
        with open(file_name, mode) as file_pointer:
            logger.debug(
                'sucessfully opened file [path: "{path}"]'.format(
                    path=file_name))
            return file_pointer.read()
    except FileNotFoundError:
        logger.error(
            'unable to read file, path does not exist [path: "{path}"]'.format(
                path=file_name))
    except (IOError, OSError) as error:
        logger.error(
            'unable to read file [path: "{path}", error: "{error}"]'.format(
                path=file_name,
                error=error))

    return False


def read_binary_file(file_name):
    """
    @brief  Alias to read_file(file_name, 'rb').

    @param file_name   The path to the file to read.

    @return     The content of the given file if successful, otherwise False.
    """
    return read_file(file_name, 'rb')


def relative_path(*args):
    """
    @brief  Return the absolute path of a the provided filepath relative to the
            calling script.

    @param  *args   A list of path compoents that will be added to the calling
                    script's path.

    @return     The absolute path, or False on error.
    """
    calling_frame = inspect.currentframe().f_back
    if calling_frame is None:
        logger.error('unable to get calling frame')
        return False

    try:
        calling_script_path = inspect.getframeinfo(calling_frame)[0]
    except IndexError:
        logger.error('unable to get file path of calling frame')
        return False

    return os.path.abspath(os.path.join(
        os.path.dirname(calling_script_path),
        *args))
