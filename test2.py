from logger_ex.logger import logger


def var_test():
    global zmie

    zmie = "test"

    try:
        zmie = "test2"
        logger.info("my test")
        logger.info(zmie)
    except Exception as err:
        logger.error(err)

    logger.info("po")
    logger.info(zmie)


if __name__ == "__main__":
    var_test()