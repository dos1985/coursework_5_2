import logging

# Create a logger object
logger = logging.getLogger(__name__)

# Print out an info message
logger.info('Starting program...')

# Print out a debug message with variable information
x = 10
logger.debug(f'x = {x}')

# Print out an error message with exception information
try:
    y = x / 0
except Exception as e:
    logger.error('Error occurred: %s', e)
