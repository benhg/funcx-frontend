import sys
import os

from funcx_frontend.execution import run_console_cmd

def upload_file_to_blt(endpoint_id,
                       local_path=None,
                       remote_path="~",
                       username=None,
                       force=False):
    """
    Upload a file or directory to endpoint.

    Uses Croc as a transport layer

    :param local_path: Path where file should be saved
    :param remote_path: Path where file is currently
    :param username: Remote host username
    :param force: Do not ask user to overwrite existing files
    """
    pass


def download_file_from_blt(endpoint_id,
                           local_path=None,
                           remote_path="~",
                           username=None,
                           force=False):
    """
    Download a file or directory from endpoint.

    Uses Croc as a transport layer

    :param local_path: Path where file should be saved
    :param remote_path: Path where file is currently
    :param username: Remote host username
    :param force: Do not ask user to overwrite existing files
    """
    pass