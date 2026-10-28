#!/bin/bash
# Run once in an authorized cluster setup session, from this project folder.
# For substantial installations, use suitable compute resources.
set -e
module load python/3.11.11
python -m venv .venv
source .venv/bin/activate
python -m pip install pandas
python -c 'import pandas; print(pandas.__version__)'
