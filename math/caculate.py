from loguru import logger

def sum(a: int, b: int) -> int:
    logger.info(f"sum {a} + {b} = {a + b}")
    return a + b


def sub(a: int, b: int) -> int:
    logger.info(f"sub {a} - {b} = {a - b}")
    return a - b


def mul(a: int, b: int) -> int:
    logger.info(f"mul {a} * {b} = {a * b}")
    return a * b