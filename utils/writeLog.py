import logging
#todo 在不同环境下filename中的地址要改
def mainlog(msg,level='info'):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s  %(levelname)s :  %(message)s',
                        datefmt='%Y-%m-%d %A %H:%M:%S', filename='./logging/main.log', filemode='a')

    if level is 'debug':
        pass
        #logging.debug(msg)
    elif level is 'info':
        logging.info(msg)
    elif level is 'error':
        logging.error(msg)
    elif level is 'warning':
        logging.warning(msg)

if __name__ == '__main__':
    mainlog("a","info")