# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

from gi.repository import Gtk # pylint: disable=E0611
import logging
logger = logging.getLogger('vehiklo')

from vehiklo_lib import Window
from vehiklo.AboutVehikloDialog import AboutVehikloDialog
from vehiklo.PreferencesVehikloDialog import PreferencesVehikloDialog

# See vehiklo_lib.Window.py for more details about how this class works
class VehikloWindow(Window):
    __gtype_name__ = "VehikloWindow"

    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(VehikloWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutVehikloDialog
        self.PreferencesDialog = PreferencesVehikloDialog

        # Code for other initialization actions should be added here.
