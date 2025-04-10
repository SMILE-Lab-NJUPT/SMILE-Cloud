import logging

def setup_logger(app): 
    level = logging.DEBUG if app.config.get("DEBUG") else logging.INFO 
    logging.basicConfig(level=level)
