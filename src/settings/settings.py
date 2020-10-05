import os

NB_THREADS = 1

# Path
TMP_FOLDER = os.path.abspath("../output/tmp")
LCM_EXECUTABLE = os.path.abspath("../bin/lcm")
RESULTS_FOLDER = os.path.abspath("../output/results")
STATS_FOLDER = os.path.abspath('../output/plots/stats')
LINKS_FOLDER = os.path.abspath('../output/plots/links')
GROUPS_FOLDER = os.path.abspath('../output/plots/groups')

# Db requirements
TRANSACTIONS_REQUIRED_FIELDS = ['article_id', 'customer_id', 'station_id', 'transaction_date', 'transaction_id']

GROUPS_DEMOGRAPHICS = ["STATION_MGT_TYPE", "DEPARTEMENT"]
