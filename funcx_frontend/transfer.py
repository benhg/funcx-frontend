import sys
import os

from funcx_frontend.execution import run_console_cmd

def upload_file(endpoint_id,
                       local_path=None,
                       remote_path="~",
                       force=False):
    """
    Upload a file or directory to endpoint.

    Uses Croc as a transport layer

    :param local_path: Path where file is currently saved
    :param remote_path: Path where file should be saved
    :param force: Do not ask user to overwrite existing files
    """
    passphrase = f"croc-upload-{random.randint(0, 100000)}"
    output = subprocess.Popen(
        ["croc", "send", "--code", passphrase, local_path])
    print(passphrase)
    run_console_cmd(f"croc --yes {passphrase} --out {remote_path}")
    print(f"{local_path} has been uploaded to {remote_path} on remote endpoint")


def download_file(endpoint_id,
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
    passphrase = f"croc-upload-{random.randint(0, 100000)}"
    f"croc --yes {passphrase} --out {remote_path}"
    output = subprocess.Popen(
        ["croc", "--yes", passphrase, "--out", local_path])
    run_console_cmd(f"croc send --code {passprhase} {remote_path}")
    print(f"{remote_path} has been downloaded to {local_path} on current computer")
