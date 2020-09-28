import os
import pathlib

NB_THREADS = 1

# Path
TMP_FOLDER = os.path.abspath("../output/tmp")
LCM_EXECUTABLE = os.path.abspath("../bin/lcm")
RESULTS_FOLDER = os.path.abspath("../output/results")

# Db requirements
TRANSACTIONS_REQUIRED_FIELDS = ['article_id', 'customer_id', 'station_id', 'transaction_date', 'transaction_id']
