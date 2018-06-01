import os
import json
from utils.log import setup_logging

logger = setup_logging()

filename = os.path.join(os.path.dirname(__file__), 'config.json')
with open(filename) as f:
    config = json.load(f)
