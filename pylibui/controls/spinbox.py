"""
 Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class Spinbox(Control):
    def __init__(self, min_value, max_value):
        """
        Creates a new spinbox.

        :param min_value: int
        :param max_value: int
        """
        super().__init__()
        self.control = libui.uiNewSpinbox(min_value, max_value)

        def handler(window, data):
            self.on_changed(data)

        self.changedHandler = libui.uiSpinboxOnChanged(self.control, handler,
                                                       None)

    @property
    def value(self):
        """
        Returns the value of the spinbox.

        :return: int
        """
        return libui.uiSpinboxValue(self.control)

    @value.setter
    def value(self, value):
        """
        Sets the value of the spinbox.

        :param value: int
        :return: None
        """
        libui.uiSpinboxSetValue(self.control, value)

    def on_changed(self, data):
        """
        Executes when spinbox's value change.

        :param data: data
        :return: None
        """
        pass
