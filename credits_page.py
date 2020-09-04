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

from PySide2.QtWidgets import QFrame, QTextBrowser


class CreditsPage(QTextBrowser):

    def __init__(self, parent=None):
        """
        Initializes the CreditsPage class.
        """
        super(CreditsPage, self).__init__(parent)

        self.setFrameStyle(QFrame.NoFrame)
        self.setStyleSheet('background-color:transparent;')
        self.setOpenExternalLinks(True)
        self.setHtml('''<html><body><dl>
            <dt><strong>BreezeIcons project</strong></dt>
            <dd>Application logo and icons made by <a href="https://api.kde.org/frameworks/breeze-icons/html/" title="Visit project's homepage">BreezeIcons project</a>
                from <a href="https://kde.org" title="Visit organization's homepage">KDE</a>
                are licensed under <a href="https://www.gnu.org/licenses/lgpl-3.0.en.html" title="GNU Lesser General Public License Version 3">LGPLv3</a>.</dd>
            </dl></body></html>''')