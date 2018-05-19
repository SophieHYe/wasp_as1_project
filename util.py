from tabulate import tabulate, TableFormat, Line, DataRow
import logging
import colorlog
import pandas as pd
import ujson as json

format = '%(log_color)s%(asctime)15s %(name)15s %(levelname)10s - %(message)s'
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    format, datefmt="%y%m%d %H:%M:%S"))

logging.getLogger("cflib.crazyflie.log").addHandler(handler)

myfmt = TableFormat(lineabove=Line("", "-", "  ", ""),
                    linebelowheader=Line("| ", "-", " | ", " |"),
                    linebetweenrows=None,
                    linebelow=None,
                    headerrow=DataRow("| ", " | ", " |"),
                    datarow=DataRow("| ", " | ", " |"),
                    padding=0,
                    with_header_hide=["lineabove", "linebelow"])


def get_logger(name, level=logging.DEBUG):
    """
    This function returns a logger object
    """

    logger = colorlog.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    return logger


def ppjson(d):
    return json.dumps(d, sort_keys=True, indent=4)


def table(logger, table, message="", level=logging.DEBUG):

    if isinstance(table, pd.DataFrame):
        table.reset_index(inplace=True)

    tbl = tabulate(
        table,
        headers='keys',
        tablefmt=myfmt,
        showindex=False)

    logger.log(level, message + "\n" + tbl)
