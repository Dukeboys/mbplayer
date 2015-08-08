#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2015 Jim Duke
## All rights reserved.
##
## This file is part of MusicBrainz Player.
##
## MusicBrainz Player is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by the
## Free Software Foundation, either version 3 of the License, or (at your
## option) any later version.
##
## MusicBrainz Player is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
## or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
## for more details.
##
## You should have received a copy of the GNU General Public License along
## with MusicBrainz Player.  If not, see <http://www.gnu.org/licenses/>
##
#############################################################################

"""Usage: mbplayer

The MusicBrainz Player is a media player GUI application that is tightly
integrated with the MusicBrainz database.
"""

import mbplayer_rc

from PyQt5.QtCore import (QFile, Qt)
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
            QMenu, QSplitter, QTabWidget, QWidget)

class MainWindow(QMainWindow):
    """Main Window of the MusicBrainz application."""

    def __init__(self):
        super(MainWindow, self).__init__()

        fileMenu = QMenu("File", self)
        exitAction = fileMenu.addAction("Exit")

        helpMenu = QMenu("Help", self)
        aboutAction = helpMenu.addAction("About")

        self.setupViews()

        exitAction.triggered.connect(QApplication.instance().quit)

        self.menuBar().addMenu(fileMenu)
        self.menuBar().addMenu(helpMenu)
        self.statusBar()
        self.setupStyles()

        self.setWindowTitle("MusicBrainz Player")
        self.resize(870, 550)

    def setupViews(self):
        splitter = QSplitter()
        splitter.setHandleWidth(5)

        browsers = QTabWidget()

        label = QLabel('Placeholder')
        label.setAlignment(Qt.AlignCenter|Qt.AlignHCenter|Qt.AlignVCenter)

        layout = QHBoxLayout()
        layout.addWidget(label)

        rightPane = QWidget()
        rightPane.setLayout(layout)

        splitter.addWidget(browsers)
        splitter.addWidget(rightPane)
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 1)

        self.setCentralWidget(splitter)

    def setupStyles(self):
        file = QFile(":/qss/default.qss");
        file.open(QFile.ReadOnly)
        styleSheet = str(file.readAll(), encoding='utf8')
        QApplication.instance().setStyleSheet(styleSheet)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
