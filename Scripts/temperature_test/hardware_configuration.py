import json
import logging
from pathlib import Path
from printer_server.settings import Config
from printer_server.drivers.screen import ScreenThread
from printer_server.drivers.galil import Galil, Galil_dummy
from printer_server.drivers.visitech import Visitech, Visitech_dummy
from printer_server.drivers.wintech import Wintech
from printer_server.drivers.tiptilt import TipTilt, TipTilt_dummy
from printer_server.drivers.loadcell import LoadCell, Loadcell_dummy

default_log_level = logging.INFO
dummy = False


configuration_path = Path(Config.PRINT_SERVER_FOLDER).rglob("hardware_configuration.json")
with open(next(configuration_path), "r") as file_handle:
    config_dict = json.load(file_handle)
config_dict = config_dict[Config.HOSTNAME]


class Printer3D:
    """Provides hardware handles to the Flask print control."""

    def __init__(self):
        self.screen = ScreenThread(
            resolutions=((2560, 1600), (1920, 1080)), log_level=default_log_level
        )
        # self.screen = ScreenThread(log_level=default_log_level)
        if dummy:
            self.galil = Galil_dummy()
            self.visitech = Visitech_dummy()
            self.tiptilt = TipTilt_dummy(verbose=True)
            self.loadcell = Loadcell_dummy()
        else:
            self.galil = Galil(
                config_dict=config_dict["galil_settings"], log_level=default_log_level
            )
            self.visitech = Visitech(log_level=default_log_level)
            self.wintech = Wintech(log_level=default_log_level)
            self.tiptilt = TipTilt_dummy(verbose=True)
            # self.tiptilt = TipTilt(
            #     config_dict=config_dict["tiptilt_settings"], log_level=default_log_level
            # )
            self.loadcell = LoadCell(
                config_dict=config_dict["loadcell_settings"], log_level=default_log_level
            )


driver_handles = Printer3D()
