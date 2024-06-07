import logging

from django.http import HttpResponse

# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    # Log some messages
    logger.debug("Debug message - Index page is loaded.")
    logger.info("Info message - Index page is loaded.")
    logger.warning("Warning message - Index page is loaded.")
    logger.error("Error message - Index page is loaded.")
    logger.critical("Critical message - Index page is loaded.")

    return HttpResponse("Hello, world. You're at the index.")
