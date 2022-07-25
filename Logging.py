import logging

logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")

#logging.basicConfig(...) set config, check on the internet args and what they do

logger = logging.getLogger(__name__) #name of module ("Logging")
logger.info('hello form module') #if u import this model it would send info
logger.propagate = False # wont send info if u import this module

#Create log file

logger = logging.getLogger(__name__)

#handlers
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#levels and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)
#level tell that it would write only this level and above

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('warrning!')
logger.error('error!')
#on console both are written
#on file only error bcs level is Error or above

#U can create file logging.conf
#import logging
#import logging.conf
#logging.config.fileConfig('logging.conf)
#logger = logging.getLogger('example')

try:
    a = [1,2,3,4]
    x = a[4]
except IndexError as e:
    logging.error(e, exc_info= True) #Traceback is wrote on console too (it s tell more abot error)


#if we dont know Error type

import traceback
try:
    a = [1,2,3,4]
    x = a[4]
except:
    logging.error('Some error - %s', traceback.format_exc())

#for big aplication u can use rotating handler
#handle = RotatingFileHandler('app.log', maxBytes = 2000, backup=5)
#it would create 5 app.log.i with max 2kb

#handle = TimedRotatingFileHandler('timed.log',when = 's', interval = 5, backup=5)
#it create every 5s some timed.log.actualtime