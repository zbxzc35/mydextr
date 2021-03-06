# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MyDextrDialog
                                 A QGIS plugin
 This plugin is used to capture objects in a photo.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-05-07
        git sha              : $Format:%H$
        copyright            : (C) 2018 by siriusk
        email                : kai475@163.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QApplication

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'mydextr_dialog_base.ui'))


class MyDextrDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None, filename=None):
        """Constructor."""
        super(MyDextrDialog, self).__init__(parent)
        self.filename = filename
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

    def openfile(self):
        """Clicked open button or start up"""
        self.filename = QFileDialog.getOpenFileName(self, "OpenFile", ".", 
            "Image Files(*.jpg *.jpeg)")[0]
        
        
    
