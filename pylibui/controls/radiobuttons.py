"""
Python wrapper for libui.

"""

from pylibui import libui
from .control import Control


class RadioButtons(Control):
    def __init__(self, items=None):
        """
        Creates a new radio buttons.

        """
        super().__init__()
        if items is None:
            items = []
        self.control = libui.uiNewRadioButtons()

        for item in items:
            self.append(item)

        def handlerOnSelected(radio_buttons, data):
            self.on_select(data)

        self.selectedHandler = libui.uiRadioButtonsOnSelected(
            self.control, handlerOnSelected, None)

    def append(self, text):
        """
        Appends a new item to the radio buttons.

        :param text: string
        :return: None
        """
        libui.uiRadioButtonsAppend(self.control, text)

    @property
    def selected(self):
        """
        Returns index of the selected item.

        :return: int
        """
        return libui.uiRadioButtonsSelected(self.control)

    @selected.setter
    def selected(self, n):
        """
        Sets selected item.

        :n: integer
        :return: None
        """
        libui.uiRadioButtonsSetSelected(self.control, n)

    def on_select(self, data):
        """
        Executes when an item in radio buttons is selected.

        :param data: data
        :return: None
        """
        pass
