    process_form.setObjectName(_fromUtf8("process_form"))
    process_form.setWindowModality(QtCore.Qt.WindowModal)
    process_form.resize(412, 199)
    font = QtGui.QFont()
    font.setStyleStrategy(QtGui.QFont.NoAntialias)
    process_form.setFont(font)
    process_form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/StartRender.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    process_form.setWindowIcon(icon)
    process_form.setWindowOpacity(1.0)
    process_form.cancel_boton = QtGui.QPushButton(process_form)
    process_form.cancel_boton.setGeometry(QtCore.QRect(360, 140, 51, 51))
    process_form.cancel_boton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    process_form.cancel_boton.setText(_fromUtf8(""))
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/errorIco.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    process_form.cancel_boton.setIcon(icon1)
    process_form.cancel_boton.setIconSize(QtCore.QSize(40, 40))
    process_form.cancel_boton.setAutoDefault(False)
    process_form.cancel_boton.setObjectName(_fromUtf8("cancel_boton"))
    process_form.info = QtGui.QPlainTextEdit(process_form)
    process_form.info.setGeometry(QtCore.QRect(10, 10, 281, 181))
    process_form.info.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    process_form.info.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n""color: rgb(0, 170, 255);"))
    process_form.info.setFrameShadow(QtGui.QFrame.Raised)
    process_form.info.setUndoRedoEnabled(False)
    process_form.info.setReadOnly(True)
    process_form.info.setMaximumBlockCount(10)
    process_form.info.setBackgroundVisible(True)
    process_form.info.setCenterOnScroll(True)
    process_form.info.setObjectName(_fromUtf8("info"))
    process_form.total_bar = QtGui.QProgressBar(process_form)
    process_form.total_bar.setGeometry(QtCore.QRect(300, 10, 51, 181))
    process_form.total_bar.setProperty("value", 24)
    process_form.total_bar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
    process_form.total_bar.setOrientation(QtCore.Qt.Vertical)
    process_form.total_bar.setInvertedAppearance(False)
    process_form.total_bar.setObjectName(_fromUtf8("total_bar"))
    process_form.actualBar = QtGui.QProgressBar(process_form)
    process_form.actualBar.setGeometry(QtCore.QRect(370, 10, 31, 121))
    process_form.actualBar.setProperty("value", 24)
    process_form.actualBar.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
    process_form.actualBar.setOrientation(QtCore.Qt.Vertical)
    process_form.actualBar.setInvertedAppearance(False)
    process_form.actualBar.setObjectName(_fromUtf8("actualBar"))
    QtCore.QMetaObject.connectSlotsByName(process_form)
    process_form.setWindowTitle(QtGui.QApplication.translate("process_form", "Titulo", None, QtGui.QApplication.UnicodeUTF8))
    process_form.cancel_boton.setToolTip(QtGui.QApplication.translate("process_form", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
    process_form.info.setPlainText(QtGui.QApplication.translate("process_form", "Output", None, QtGui.QApplication.UnicodeUTF8))
    process_form.total_bar.setToolTip(QtGui.QApplication.translate("process_form", "Total progress", None, QtGui.QApplication.UnicodeUTF8))
    process_form.actualBar.setToolTip(QtGui.QApplication.translate("process_form", "Current render progress", None, QtGui.QApplication.UnicodeUTF8))
