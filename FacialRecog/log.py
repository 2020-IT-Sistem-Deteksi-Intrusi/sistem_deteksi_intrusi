import logging
import face_recognition_edit

def LOG_insert(file, format, text, level):
    infoLog = logging.FileHandler(file)
    infoLog.setFormatter(format)
    logger = logging.getLogger(file)
    logger.setLevel(level)
    
    if not logger.handlers:
        logger.addHandler(infoLog)
        if (level == logging.INFO):
            logger.info(text)
        if (level == logging.ERROR):
            logger.error(text)
        if (level == logging.WARNING):
            logger.warning(text)
    
    infoLog.close()
    logger.removeHandler(infoLog)
    
    return

formatLOG = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
LOG_insert("log/Access.log", formatLOG , str(names[id]) + "Detected", logging.INFO)