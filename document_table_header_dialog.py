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

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QButtonGroup, QCheckBox, QDialog, QDialogButtonBox, QGridLayout, QGroupBox, QRadioButton, QVBoxLayout

from settings import Settings


class DocumentTableHeaderDialog(QDialog):

    def __init__(self, number, parent=None):
        super(DocumentTableHeaderDialog, self).__init__(parent)

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # Group box
        text = 'Binary Number' if number >= 0 else 'Binary Numbers'
        toolTip = 'Change label to a binary number' if number >= 0 else 'Change all labels to binary numbers'
        rdbBinary = QRadioButton(text)
        rdbBinary.setToolTip(toolTip)

        text = 'With prefix 0b'
        toolTip = 'Change label to a binary number with prefix 0b otherwise without prefix' if number >= 0 else 'Change all labels to binary numbers with prefix 0b otherwise without prefix'
        self.chkBinary = QCheckBox(text)
        self.chkBinary.setChecked(True)
        self.chkBinary.setEnabled(False)
        self.chkBinary.setToolTip(toolTip)
        rdbBinary.toggled.connect(lambda checked: self.chkBinary.setEnabled(checked))

        text = 'Octal Number' if number >= 0 else 'Octal Numbers'
        toolTip = 'Change label to a octal number' if number >= 0 else 'Change all labels to octal numbers'
        rdbOctal = QRadioButton(text)
        rdbOctal.setToolTip(toolTip)

        text = 'Decimal Number' if number >= 0 else 'Decimal Numbers'
        toolTip = 'Change label to a decimal number' if number >= 0 else 'Change all labels to decimal numbers'
        rdbDecimal = QRadioButton(text)
        rdbDecimal.setToolTip(toolTip)

        text = 'Hexadecimal Number' if number >= 0 else 'Hexadecimal Numbers'
        toolTip = 'Change label to a hexadecimal number' if number >= 0 else 'Change all labels to hexadecimal numbers'
        rdbHexadecimal = QRadioButton(text)
        rdbHexadecimal.setToolTip(toolTip)

        text = 'Capital Letter' if number >= 0 else 'Capital Letters'
        toolTip = 'Change label to a capital letter' if number >= 0 else 'Change all labels to capital letters'
        rdbLetter = QRadioButton(text)
        rdbLetter.setToolTip(toolTip)

        self.grpHeaderLabel = QButtonGroup(self)
        self.grpHeaderLabel.addButton(rdbBinary, Settings.HeaderLabel.Binary.value)
        self.grpHeaderLabel.addButton(rdbOctal, Settings.HeaderLabel.Octal.value)
        self.grpHeaderLabel.addButton(rdbDecimal, Settings.HeaderLabel.Decimal.value)
        self.grpHeaderLabel.addButton(rdbHexadecimal, Settings.HeaderLabel.Hexadecimal.value)
        self.grpHeaderLabel.addButton(rdbLetter, Settings.HeaderLabel.Letter.value)
        self.grpHeaderLabel.buttonClicked.connect(self.onSettingChanged)

        groupLayout = QGridLayout()
        groupLayout.addWidget(rdbBinary, 0, 0)
        groupLayout.addWidget(self.chkBinary, 0, 1)
        groupLayout.addWidget(rdbOctal, 1, 0)
        groupLayout.addWidget(rdbDecimal, 2, 0)
        groupLayout.addWidget(rdbHexadecimal, 3, 0)
        groupLayout.addWidget(rdbLetter, 4, 0)

        text = 'Change label to a …' if number >= 0 else 'Change all labels to …'
        groupBox = QGroupBox(text)
        groupBox.setLayout(groupLayout)

        # Button box
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonOk = buttonBox.button(QDialogButtonBox.Ok)
        self.buttonOk.setEnabled(False)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(groupBox)
        layout.addWidget(buttonBox)

        self.setLayout(layout)


    def onSettingChanged(self):
        """
        Enables the ok button if a setting has been changed.
        """
        self.buttonOk.setEnabled(True)


    def headerLabelType(self):
        """
        Returns the type of the header label.
        """
        return Settings.HeaderLabel(self.grpHeaderLabel.checkedId())


    def headerLabelParameter(self):
        """
        Returns the parameter of the header label.
        """
        type = self.headerLabelType()

        if type == Settings.HeaderLabel.Binary:
            return '0b' if self.chkBinary.isChecked() else ''
        else:
            return ''
