import logging
logging.basicConfig( 
    level = logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Arthimetic App")

def add(a,b):
    result = a+b
    logger.debug(f"Adding: {a}+{b} = {result}")
    return result
def sub(a,b):
    result = a-b
    logger.debug(f"Adding: {a}-{b} = {result}")
    return result
def mult(a,b):
    result = a*b
    logger.debug(f"Adding: {a}*{b} = {result}")
    return result

def div(a,b):
    try:
        result = a/b
        logger.debug(f"Adding: {a}/{b} = {result}")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

add(10,15)
sub(10,20)
mult(134,169)
div(20,0)