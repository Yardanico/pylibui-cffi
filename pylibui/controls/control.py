"""
 Python wrapper for libui.

"""

from pylibui import libui


class Control:
    def __init__(self, control=None):
        """
        Creates a new Control.

        """
        self.control = control

    def pointer(self):
        """
        Returns this control as ui pointer.

        :return: uiControl ctype pointer
        """
        return libui.ffi.cast('uiControl *', self.control)

    def visible(self):
        """
        Returns whether the control is visible.

        :return: bool
        """
        return bool(libui.uiControlVisible(self.pointer()))

    def show(self):
        """
        Shows the control.

        :return: None
        """
        libui.uiControlShow(self.pointer())

    def hide(self):
        """
        Hides the control.

        :return: None
        """
        libui.uiControlHide(self.pointer())

    @property
    def enabled(self):
        """
        Returns whether the control is enabled.

        :return: bool
        """
        return bool(libui.uiControlEnabled(self.pointer()))

    @enabled.setter
    def enabled(self, enabled):
        """
        Enables or disables the control.

        :param enabled: bool
        :return: None
        """

        if enabled:
            libui.uiControlEnable(self.pointer())
        else:
            libui.uiControlDisable(self.pointer())

    def destroy(self):
        """
        Destroys the control.

        :return: None
        """
        libui.uiControlDestroy(self.pointer())
