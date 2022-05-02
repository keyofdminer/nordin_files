import os
import sys
import signal
import logging
from pathlib import Path
from time import sleep

from async_file_handler import AsyncFileHandler
from loadcell import LoadCell


def exit_prog(signal, frame):
    loadcell.stop()
    loadcell.set_log_file(None)
    async_file_hander.finish()
    print("Program finished!")
    sys.exit(0)


signal.signal(signal.SIGINT, exit_prog)

async_file_hander = AsyncFileHandler()
loadcell = LoadCell(async_file_hander, log_level=logging.INFO)

APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory

loadcell_log = str(Path(APP_DIR) / "loadcell_data.csv")
loadcell.connect()

async_file_hander.write(loadcell_log, "timestamp,index,raw_data,newtons\n")
async_file_hander.start()
loadcell.set_log_file(loadcell_log)
loadcell.start()

sleep(30)
