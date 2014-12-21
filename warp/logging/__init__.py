import logging

class KwargsLoggingAdapter(logging.LoggerAdapter):

    """
    This example adapter expects the passed in dict-like object to have a
    'connid' key, whose value in brackets is prepended to the log message.
    """

    def process(self, msg, kwargs):
        system = kwargs.pop("system", "NONE")
        kwargs["extra"] = {}
        kwargs["extra"]["system"] = system
        return msg, kwargs

def get_logger(name):
    dummy_dict = {}
    logging.basicConfig(
        level=logging.DEBUG, format="%(asctime)s %(name)s:%(system)s:%(levelname)s:%(message)s")
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    log = KwargsLoggingAdapter(logger, dummy_dict)
    return log
