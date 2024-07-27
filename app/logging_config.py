# app/logging_config.py
import logging

def setup_logging():
    logging.basicConfig(
        filename='app_logs.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
