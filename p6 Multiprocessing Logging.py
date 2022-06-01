The multiprocessing module also provides logging module to ensure that, 
if the logging package doesn't use locks function, the messages between processes mixed up during execution.

Example
import multiprocessing, logging
logger = multiprocessing.log_to_stderr()
logger.setLevel(logging.INFO)
logger.warning('Error has occurred')

In this example at first we import the logging and multiprocessing module then we use multiprocessing.log_to_stderr() method. 
And it call get_logger() as well as adding to sys.stderr and finally we set the level of logger and convey the message.
