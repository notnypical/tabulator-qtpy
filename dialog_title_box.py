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

from PySide2.QtSvg import QSvgWidget
from PySide2.QtWidgets import QApplication, QHBoxLayout, QLabel, QVBoxLayout, QWidget


class DialogTitleBox(QWidget):

    def __init__(self, parent=None):
        """
        Initializes the DialogTitleBox class.
        """
        super(DialogTitleBox, self).__init__(parent)

        name = QLabel(f'<strong style="font-size:large;">{QApplication.applicationName()}</strong> v{QApplication.applicationVersion()}')
        description = QLabel('A CSV editor written in Qt for Python.')

        widgetTmp = QWidget()
        vboxlayoutTmp = QVBoxLayout(widgetTmp)
        vboxlayoutHeight = name.sizeHint().height() + vboxlayoutTmp.layout().spacing() + description.sizeHint().height()

        logo = QSvgWidget()
        logo.load(':/icons/apps/22/tabulator.svg')
        logo.setFixedSize(vboxlayoutHeight, vboxlayoutHeight)

        labels = QVBoxLayout()
        labels.addWidget(name)
        labels.addWidget(description)

        titleBox = QHBoxLayout()
        titleBox.addWidget(logo)
        titleBox.addLayout(labels)

        # Main layout
        layout = QVBoxLayout()
        layout.addLayout(titleBox)
        layout.addStretch(1)

        self.setLayout(layout)