"""
FuncX Shell - `fxsh`

Use FuncX to open a virtual
    interactive session on a FuncX endpoint.

Any commands input will be forwarded to the
    endpoint using `subprocess.check_output`

Has only been tested with Linux-based endponits
"""

import argparse

from funcx_frontend.execution import fxsh


def cli_run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--endpoint-id",
                        "-ep",
                        type=str,
                        help="Endpoint to open interactive session on",
                        default="3c3f0b4f-4ae4-4241-8497-d7339972ff4a")
    parser.add_argument("--verbose",
                        "-v",
                        action="store_true",
                        help="Enable verbose output",
                        default=False)
    args = parser.parse_args()

    fxsh(endpoint_name=args.endpoint_name, print_wait=args.verbose)


if __name__ == '__main__':
    cli_run()
