# This Python file uses the following encoding: utf-8
#
# Copyright 2020 NotNypical, <https://notnypical.github.io>.
#
# This file is part of pyTabulator.
#
# pyTabulator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyTabulator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyTabulator.  If not, see <https://www.gnu.org/licenses/>.
#

from PySide2.QtCore import QByteArray, QRect, QSettings, Qt
from PySide2.QtGui import QIcon, QKeySequence
from PySide2.QtWidgets import QAction, QApplication, QMainWindow

from about_dialog import AboutDialog
from colophon_dialog import ColophonDialog
from keyboard_shortcuts_dialog import KeyboardShortcutsDialog
from preferences_dialog import PreferencesDialog
from settings import Settings

import resources


class MainWindow(QMainWindow):

    m_settings = Settings()


    def __init__(self):
        """
        Initializes the MainWindow class.
        """
        QMainWindow.__init__(self)

        self.setupUI()

        self.readSettings()


    def setupUI(self):
        """
        Sets up the user interface.
        """
        self.setWindowIcon(QIcon(':/icons/apps/22/tabulator.svg'))

        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.createStatusBar()


    def createActions(self):
        """
        Creates user interface actions.
        """

        # Actions: Application
        self.actionAbout = QAction(f'About {QApplication.applicationName()}', self)
        self.actionAbout.setIcon(QIcon(':/icons/apps/16/tabulator.svg'))
        self.actionAbout.setStatusTip('Brief description of the application')
        self.actionAbout.setToolTip('Brief description of the application')
        self.actionAbout.triggered.connect(self.onActionAboutTriggered)

        self.actionColophon = QAction('Colophon', self)
        self.actionColophon.setStatusTip('Lengthy description of the application')
        self.actionColophon.setToolTip('Lengthy description of the application')
        self.actionColophon.triggered.connect(self.onActionColophonTriggered)

        self.actionPreferences = QAction('Preferences…', self)
        self.actionPreferences.setIcon(QIcon.fromTheme('configure', QIcon(':/icons/actions/16/configure.svg')))
        self.actionPreferences.setStatusTip('Customize the appearance and behavior of the application')
        self.actionPreferences.setToolTip('Customize the appearance and behavior of the application')
        self.actionPreferences.triggered.connect(self.onActionPreferencesTriggered)

        self.actionQuit = QAction('Quit', self)
        self.actionQuit.setIcon(QIcon.fromTheme('application-exit', QIcon(':/icons/actions/16/application-exit.svg')))
        self.actionQuit.setShortcut(QKeySequence.Quit)
        self.actionQuit.setStatusTip('Quit the application')
        self.actionQuit.setToolTip('Quit the application')
        self.actionQuit.triggered.connect(self.onActionQuitTriggered)

        # Actions: View
        self.actionFullScreen = QAction(self)
        self.actionFullScreen.setCheckable(True)
        self.actionFullScreen.setShortcuts([QKeySequence(Qt.Key_F11), QKeySequence.FullScreen])
        self.actionFullScreen.triggered.connect(self.onActionFullScreenTriggered)

        self.updateActionFullScreen()

        # Actions: Help
        self.actionKeyboardShortcuts = QAction('Keyboard Shortcuts', self)
        self.actionKeyboardShortcuts.setIcon(QIcon.fromTheme('help-keyboard-shortcuts', QIcon(':/icons/actions/16/help-keyboard-shortcuts.svg')))
        self.actionKeyboardShortcuts.setStatusTip('List of all keyboard shortcuts')
        self.actionKeyboardShortcuts.setToolTip('List of all keyboard shortcuts')
        self.actionKeyboardShortcuts.triggered.connect(self.onActionKeyboardShortcutsTriggered)


    def updateActionFullScreen(self):
        """
        Updates the full screen action, depending on the current screen-occupation state.
        """
        if not self.isFullScreen():
            self.actionFullScreen.setText('Full Screen Mode')
            self.actionFullScreen.setIcon(QIcon.fromTheme('view-fullscreen', QIcon(':/icons/actions/16/view-fullscreen.svg')))
            self.actionFullScreen.setChecked(False)
            self.actionFullScreen.setStatusTip('Display the window in full screen')
            self.actionFullScreen.setToolTip('Display the window in full screen')
        else:
            self.actionFullScreen.setText('Exit Full Screen Mode')
            self.actionFullScreen.setIcon(QIcon.fromTheme('view-restore', QIcon(':/icons/actions/16/view-restore.svg')))
            self.actionFullScreen.setChecked(True)
            self.actionFullScreen.setStatusTip('Exit the full screen mode')
            self.actionFullScreen.setToolTip('Exit the full screen mode')


    def createMenus(self):
        """
        Creates groups of menu items.
        """

        # Menu: Application
        menuApplication = self.menuBar().addMenu('Application')
        menuApplication.addAction(self.actionAbout)
        menuApplication.addAction(self.actionColophon)
        menuApplication.addSeparator()
        menuApplication.addAction(self.actionPreferences)
        menuApplication.addSeparator()
        menuApplication.addAction(self.actionQuit)

        # Menu: Document
        menuDocument = self.menuBar().addMenu('Document')

        # Menu: Edit
        menuEdit = self.menuBar().addMenu('Edit')

        # Menu: Tools
        menuTools = self.menuBar().addMenu('Tools')

        # Menu: View
        menuView = self.menuBar().addMenu('View')
        menuView.addAction(self.actionFullScreen)

        # Menu: Help
        menuHelp = self.menuBar().addMenu('Help')
        menuHelp.addAction(self.actionKeyboardShortcuts)


    def createToolBars(self):
        """
        Creates groups of toolbar buttons.
        """

        # Toolbar: Document
        toolbarDocument = self.addToolBar('Document')
        toolbarDocument.setObjectName('toolbarDocument')

        # Toolbar: Edit
        toolbarEdit = self.addToolBar('Edit')
        toolbarEdit.setObjectName('toolbarEdit')

        # Toolbar: Tools
        toolbarTools = self.addToolBar('Tools')
        toolbarTools.setObjectName('toolbarTools')

        # Toolbar: View
        toolbarView = self.addToolBar('View')
        toolbarView.setObjectName('toolbarView')
        toolbarView.addAction(self.actionFullScreen)


    def createStatusBar(self):
        """
        Creates the status bar.
        """
        self.statusBar().showMessage(f'Welcome to {QApplication.applicationName()}', 3000)


    def readSettings(self):
        """
        Restores user preferences and other application properties.
        """
        settings = QSettings()

        # Application: Appearance
        self.m_settings.restoreWindowGeometry = self.valueToBool(settings.value('Settings/restoreWindowGeometry', True))
        self.m_settings.restoreDialogGeometry = self.valueToBool(settings.value('Settings/restoreDialogGeometry', True))

        # Window and dialog properties
        mainWindowGeometry = settings.value('MainWindow/geometry', QByteArray())
        mainWindowState = settings.value('MainWindow/state', QByteArray())
        self.aboutDialogGeometry = settings.value('AboutDialog/geometry', QByteArray())
        self.colophonDialogGeometry = settings.value('ColophonDialog/geometry', QByteArray())
        self.keyboardShortcutsDialogGeometry = settings.value('KeyboardShortcutsDialog/geometry', QByteArray())
        self.preferencesDialogGeometry = settings.value('PreferencesDialog/geometry', QByteArray())

        # Set window properties
        if self.m_settings.restoreWindowGeometry and mainWindowGeometry:
            self.restoreGeometry(mainWindowGeometry)
        else:
            availableGeometry = QRect(QApplication.desktop().availableGeometry(self))
            self.resize(availableGeometry.width() / 2, availableGeometry.height() / 2)
            self.move((availableGeometry.width() - self.width()) / 2, (availableGeometry.height() - self.height()) / 2)
        self.restoreState(mainWindowState)


    def writeSettings(self):
        """
        Saves user preferences and other application properties.
        """
        settings = QSettings()

        # Application: Appearance
        settings.setValue('Settings/restoreWindowGeometry', self.m_settings.restoreWindowGeometry)
        settings.setValue('Settings/restoreDialogGeometry', self.m_settings.restoreDialogGeometry)

        # Window and dialog properties
        settings.setValue('MainWindow/geometry', self.saveGeometry())
        settings.setValue('MainWindow/state', self.saveState())
        settings.setValue('AboutDialog/geometry', self.aboutDialogGeometry)
        settings.setValue('ColophonDialog/geometry', self.colophonDialogGeometry)
        settings.setValue('KeyboardShortcutsDialog/geometry', self.keyboardShortcutsDialogGeometry)
        settings.setValue('PreferencesDialog/geometry', self.preferencesDialogGeometry)


    @staticmethod
    def valueToBool(value):
        """
        Converts a specified value to an equivalent Boolean value.

        Args:
            value (bool): The specified value.

        Returns:
            bool: The equivalent Boolean value.
        """
        return value.lower() == 'true' if isinstance(value, str) else bool(value)


    def closeEvent(self, event):
        """
        Processes the Close event.

        Args:
            event (QCloseEvent): The Close event.
        """

        if True:
            self.writeSettings()
            event.accept()
        else:
            event.ignore()


    def onActionAboutTriggered(self):
        """
        Displays the About dialog.
        """
        geometry = self.aboutDialogGeometry if self.m_settings.restoreDialogGeometry else QByteArray()

        aboutDialog = AboutDialog(self)
        aboutDialog.setWindowTitle(f'About {QApplication.applicationName()}')
        aboutDialog.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        aboutDialog.setWindowGeometry(geometry)
        aboutDialog.exec_()

        self.aboutDialogGeometry = aboutDialog.windowGeometry()


    def onActionColophonTriggered(self):
        """
        Displays the Colophon dialog.
        """
        geometry = self.colophonDialogGeometry if self.m_settings.restoreDialogGeometry else QByteArray()

        colophonDialog = ColophonDialog(self)
        colophonDialog.setWindowTitle('Colophon')
        colophonDialog.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        colophonDialog.setWindowGeometry(geometry)
        colophonDialog.exec_()

        self.colophonDialogGeometry = colophonDialog.windowGeometry()


    def onActionPreferencesTriggered(self):
        """
        Displays the Preferences dialog.
        """
        geometry = self.preferencesDialogGeometry if self.m_settings.restoreDialogGeometry else QByteArray()

        preferencesDialog = PreferencesDialog(self)
        preferencesDialog.setWindowTitle('Preferences')
        preferencesDialog.setWindowGeometry(geometry)
        preferencesDialog.setSettings(self.m_settings)
        preferencesDialog.exec_()

        self.preferencesDialogGeometry = preferencesDialog.windowGeometry()
        self.m_settings = preferencesDialog.settings()


    def onActionQuitTriggered(self):
        """
        Fires the Close event to terminate the application.
        """
        self.close()


    def onActionFullScreenTriggered(self):
        """
        Sets the screen-occupation state of the window.
        """
        if not self.isFullScreen():
            self.setWindowState(self.windowState() | Qt.WindowFullScreen)
        else:
            self.setWindowState(self.windowState() & ~Qt.WindowFullScreen)

        self.updateActionFullScreen()


    def onActionKeyboardShortcutsTriggered(self):
        """
        Displays the Keyboard Shortcuts dialog.
        """
        geometry = self.keyboardShortcutsDialogGeometry if self.m_settings.restoreDialogGeometry else QByteArray()

        self.keyboardShortcutsDialog = KeyboardShortcutsDialog(self)
        self.keyboardShortcutsDialog.setWindowTitle('Keyboard Shortcuts')
        self.keyboardShortcutsDialog.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        self.keyboardShortcutsDialog.setWindowGeometry(geometry)
        self.keyboardShortcutsDialog.finished.connect(self.onDialogKeyboardShortcutsFinished)
        self.keyboardShortcutsDialog.show()


    def onDialogKeyboardShortcutsFinished(self):
        """
        Keyboard Shortcuts dialog was closed.
        """
        self.keyboardShortcutsDialogGeometry = self.keyboardShortcutsDialog.windowGeometry()
