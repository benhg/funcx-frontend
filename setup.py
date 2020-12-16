import os
from setuptools import setup, find_packages

version_ns = {}
with open(os.path.join("funcx_frontend", "version.py")) as f:
    exec(f.read(), version_ns)
version = version_ns['VERSION']

with open('requirements.txt') as f:
    install_requires = f.readlines()

setup(
    name='funcx_frontend',
    version=version,
    packages=find_packages(),
    description='FuncX Frontend: For easily accessing FuncX endpoints',
    install_requires=install_requires,
    python_requires=">=3.6.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering"
    ],
    keywords=[
        "funcX",
        "FaaS",
        "Function Serving",
        "BLT"
    ],
    entry_points={'console_scripts':
                  ['fxsh=funcx_frontend.fxsh:cli_run']
    },
    author='Ben Glick',
    author_email='glick@glick.cloud',
    license="Apache License, Version 2.0",
    url="https://github.com/benhg/blt-funcx-toolkit"
)