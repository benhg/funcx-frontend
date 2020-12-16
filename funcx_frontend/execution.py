import os
import sys
import subprocess
import time

from funcx.sdk.client import FuncXClient

from funcx_frontend.config import FUNCX_SLEEP_TIME


def run_function_wait_result(py_fn,
                             py_fn_args,
                             py_fn_kwargs={},
                             endpoint_id="3c3f0b4f-4ae4-4241-8497-d7339972ff4a",
                             print_status=True):
    """
    Register and run a function with FuncX, wait for execution,
        and return results when they are available

    :param py_fn: Handle of Python function
    :param py_fn_args: List of positional args for py function
    :param py_fn_kwargs: Dict of keyword args for py function,
    :param endpoint_id: ID of endpoint to run command on
        - must be configured in config.py
    """
    fxc = FuncXClient()
    func_uuid = fxc.register_function(py_fn)
    res = fxc.run(*py_fn_args,
                  **py_fn_kwargs,
                  endpoint_id=endpoint_id,
                  function_id=func_uuid)
    while True:
        try:
            if print_status:
                print("Waiting for results...")
            time.sleep(FUNCX_SLEEP_TIME)
            return str(fxc.get_result(res), encoding="utf-8")
            break
        except Exception as e:
            if "waiting-for-" in str(e):
                continue
            else:
                raise e


def run_function_async(py_fn,
                       py_fn_args,
                       py_fn_kwargs={},
                       endpoint_id="3c3f0b4f-4ae4-4241-8497-d7339972ff4a"):
    """
    Asynchronously register and run a Python function on a FuncX endpoint

    :param py_fn: Handle of Python function
    :param py_fn_args: List of positional args for py function
    :param py_fn_kwargs: Dict of keyword args for py function,
    :param endpoint_id: ID of endpoint to run command on
        - must be configured in config.py
    """
    # Use return value for Funcx polling
    fxc = FuncXClient()
    func_uuid = fxc.register_function(py_fn)
    res = fxc.run(*py_fn_args,
                  **kwargs,
                  endpoint_id=endpoint_id,
                  function_id=func_uuid)
    return res


def _funcx_command_fn(cmd):
    """
    Helper method for calling console command
    """
    import subprocess
    return subprocess.check_output(cmd, shell=True)


def run_console_cmd(command,
                    endpoint_id="3c3f0b4f-4ae4-4241-8497-d7339972ff4a",
                    wait=True,
                    print_status=True):
    """
    Run a console command on the FuncX endpoint specified.

    Either waits for output and returns output or
        returns FuncX object which can be used to poll for results

    :param command: command to run
    :param endpoint_id: ID of endpoint to run command on
        - must be configured in config.py
    :param wait: Wait for output if True, otherwise run async.
    """
    if wait:
        return run_function_wait_result(_funcx_command_fn, [command],
                                        endpoint_id=endpoint_id,
                                        print_status=print_status)
    else:
        return run_function_async(_funcx_command_fn, [command],
                                  endpoint_id=endpoint_id)


def install_python_package(package_name):
    """
    Helper function to install a python package with `pip3`

    BLT Specific.

    :param package_name: Package to install.
    """
    return run_console_cmd(
        f"sudo /local/cluster/bin/pip3 install {package_name}")


def get_name(endpoint_id):
    """Return the name of an endpoint given its ID
    
       Not currently possible but Ryan promised it would be soon.
    """
    return endpoint_id

def fxsh(endpoint_id="3c3f0b4f-4ae4-4241-8497-d7339972ff4a", print_wait=True):
    """
    FuncX Shell - `fxsh`

    Use FuncX to open a virtual
        interactive session on a FuncX endpoint.

    Any commands input will be forwarded to the
        endpoint using `subprocess.check_output`

    Has only been tested with Linux-based endponits

    :param endpoint_id: Endpoint name. Must be present in config file
    :param print_wait: Print "waiting for results.." periodically while waiting.
    """
    ps1 = f"fxsh[{get_name(endpoint_id)}]$ "
    cwd = "~"
    try:
        cmd = input(ps1)
        while cmd.lower() != "exit":

            if cmd.startswith("cd "):
                cwd = cmd.split("cd ")[1].strip()
                cmd = input(ps1)
                continue
            try:
                print(
                    run_console_cmd(f"cd {cwd} ; {cmd}",
                                    endpoint_id=endpoint_id,
                                    wait=True,
                                    print_status=print_wait))
            except subprocess.CalledProcessError as e:
                print(f"Command {cmd} Failed:")
                print(str(e))
            cmd = input(ps1)
    except KeyboardInterrupt:
        # Make ctrl-c look like an `exit`
        print(ps1 + "exit")
        sys.exit(0)


if __name__ == '__main__':
    fxsh()
