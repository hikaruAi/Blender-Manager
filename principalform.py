    principal.setObjectName(_fromUtf8("principal"))
    principal.resize(401, 406)
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(principal.sizePolicy().hasHeightForWidth())
    principal.setSizePolicy(sizePolicy)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/icono.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.setWindowIcon(icon)
    principal.setWindowOpacity(0.98)
    principal.setAutoFillBackground(True)
    principal.tab_tipo = QtGui.QTabWidget(principal)
    principal.tab_tipo.setGeometry(QtCore.QRect(140, 10, 41, 191))
    font = QtGui.QFont()
    font.setFamily(_fromUtf8("Aparajita"))
    font.setPointSize(10)
    font.setBold(True)
    font.setWeight(75)
    principal.tab_tipo.setFont(font)
    principal.tab_tipo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.tab_tipo.setLayoutDirection(QtCore.Qt.RightToLeft)
    principal.tab_tipo.setTabPosition(QtGui.QTabWidget.East)
    principal.tab_tipo.setTabShape(QtGui.QTabWidget.Rounded)
    principal.tab_tipo.setIconSize(QtCore.QSize(28, 31))
    principal.tab_tipo.setObjectName(_fromUtf8("tab_tipo"))
    principal.image_tab = QtGui.QWidget()
    principal.image_tab.setLayoutDirection(QtCore.Qt.LeftToRight)
    principal.image_tab.setAutoFillBackground(False)
    principal.image_tab.setObjectName(_fromUtf8("image_tab"))
    icon1 = QtGui.QIcon()
    icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/renderImage.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.tab_tipo.addTab(principal.image_tab, icon1, _fromUtf8(""))
    principal.animation_tab = QtGui.QWidget()
    principal.animation_tab.setObjectName(_fromUtf8("animation_tab"))
    icon2 = QtGui.QIcon()
    icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/renderAni.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.tab_tipo.addTab(principal.animation_tab, icon2, _fromUtf8(""))
    principal.lista_tareas = QtGui.QListWidget(principal)
    principal.lista_tareas.setGeometry(QtCore.QRect(10, 10, 131, 192))
    principal.lista_tareas.setObjectName(_fromUtf8("lista_tareas"))
    principal.agregarTarea_boton = QtGui.QToolButton(principal)
    principal.agregarTarea_boton.setGeometry(QtCore.QRect(200, 10, 41, 41))
    principal.agregarTarea_boton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.agregarTarea_boton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    icon3 = QtGui.QIcon()
    icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/addIco.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.agregarTarea_boton.setIcon(icon3)
    principal.agregarTarea_boton.setIconSize(QtCore.QSize(32, 32))
    principal.agregarTarea_boton.setObjectName(_fromUtf8("agregarTarea_boton"))
    principal.quitarTarea_buton = QtGui.QToolButton(principal)
    principal.quitarTarea_buton.setGeometry(QtCore.QRect(240, 10, 41, 41))
    principal.quitarTarea_buton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.quitarTarea_buton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    icon4 = QtGui.QIcon()
    icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/quitarIco.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.quitarTarea_buton.setIcon(icon4)
    principal.quitarTarea_buton.setIconSize(QtCore.QSize(32, 32))
    principal.quitarTarea_buton.setObjectName(_fromUtf8("quitarTarea_buton"))
    principal.quitarTarea_buton_2 = QtGui.QToolButton(principal)
    principal.quitarTarea_buton_2.setGeometry(QtCore.QRect(280, 10, 41, 41))
    principal.quitarTarea_buton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.quitarTarea_buton_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    icon5 = QtGui.QIcon()
    icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/guardarIco.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.quitarTarea_buton_2.setIcon(icon5)
    principal.quitarTarea_buton_2.setIconSize(QtCore.QSize(32, 32))
    principal.quitarTarea_buton_2.setObjectName(_fromUtf8("quitarTarea_buton_2"))
    principal.blendFile_group = QtGui.QGroupBox(principal)
    principal.blendFile_group.setGeometry(QtCore.QRect(190, 60, 201, 71))
    font = QtGui.QFont()
    font.setPointSize(7)
    principal.blendFile_group.setFont(font)
    principal.blendFile_group.setObjectName(_fromUtf8("blendFile_group"))
    principal.blendFile_edit = QtGui.QLineEdit(principal.blendFile_group)
    principal.blendFile_edit.setEnabled(True)
    principal.blendFile_edit.setGeometry(QtCore.QRect(10, 20, 111, 20))
    font = QtGui.QFont()
    font.setPointSize(6)
    principal.blendFile_edit.setFont(font)
    principal.blendFile_edit.setFrame(False)
    principal.blendFile_edit.setReadOnly(True)
    principal.blendFile_edit.setObjectName(_fromUtf8("blendFile_edit"))
    principal.browseBlend_boton = QtGui.QToolButton(principal.blendFile_group)
    principal.browseBlend_boton.setGeometry(QtCore.QRect(130, 10, 61, 51))
    principal.browseBlend_boton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.browseBlend_boton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    icon6 = QtGui.QIcon()
    icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/browseBlend.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.browseBlend_boton.setIcon(icon6)
    principal.browseBlend_boton.setIconSize(QtCore.QSize(40, 40))
    principal.browseBlend_boton.setPopupMode(QtGui.QToolButton.DelayedPopup)
    principal.browseBlend_boton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
    principal.browseBlend_boton.setObjectName(_fromUtf8("browseBlend_boton"))
    principal.blender_group = QtGui.QGroupBox(principal)
    principal.blender_group.setGeometry(QtCore.QRect(190, 130, 201, 71))
    font = QtGui.QFont()
    font.setPointSize(7)
    principal.blender_group.setFont(font)
    principal.blender_group.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    principal.blender_group.setObjectName(_fromUtf8("blender_group"))
    principal.browseBlender_button = QtGui.QToolButton(principal.blender_group)
    principal.browseBlender_button.setGeometry(QtCore.QRect(10, 10, 61, 51))
    principal.browseBlender_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.browseBlender_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    icon7 = QtGui.QIcon()
    icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/browse.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.browseBlender_button.setIcon(icon7)
    principal.browseBlender_button.setIconSize(QtCore.QSize(40, 40))
    principal.browseBlender_button.setPopupMode(QtGui.QToolButton.DelayedPopup)
    principal.browseBlender_button.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
    principal.browseBlender_button.setObjectName(_fromUtf8("browseBlender_button"))
    principal.blender_edit = QtGui.QLineEdit(principal.blender_group)
    principal.blender_edit.setEnabled(True)
    principal.blender_edit.setGeometry(QtCore.QRect(80, 30, 111, 20))
    font = QtGui.QFont()
    font.setPointSize(6)
    principal.blender_edit.setFont(font)
    principal.blender_edit.setFrame(False)
    principal.blender_edit.setReadOnly(True)
    principal.blender_edit.setObjectName(_fromUtf8("blender_edit"))
    principal.other_box = QtGui.QGroupBox(principal)
    principal.other_box.setGeometry(QtCore.QRect(270, 210, 131, 80))
    principal.other_box.setAlignment(QtCore.Qt.AlignCenter)
    principal.other_box.setObjectName(_fromUtf8("other_box"))
    principal.registrar_boton = QtGui.QToolButton(principal.other_box)
    principal.registrar_boton.setGeometry(QtCore.QRect(10, 20, 111, 21))
    font = QtGui.QFont()
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    principal.registrar_boton.setFont(font)
    principal.registrar_boton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.registrar_boton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    icon8 = QtGui.QIcon()
    icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/registrarBoton.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.registrar_boton.setIcon(icon8)
    principal.registrar_boton.setIconSize(QtCore.QSize(40, 40))
    principal.registrar_boton.setPopupMode(QtGui.QToolButton.DelayedPopup)
    principal.registrar_boton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
    principal.registrar_boton.setObjectName(_fromUtf8("registrar_boton"))
    principal.debug_button = QtGui.QToolButton(principal.other_box)
    principal.debug_button.setGeometry(QtCore.QRect(10, 50, 111, 21))
    font = QtGui.QFont()
    font.setStyleStrategy(QtGui.QFont.PreferAntialias)
    principal.debug_button.setFont(font)
    principal.debug_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.debug_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    icon9 = QtGui.QIcon()
    icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/debug.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.debug_button.setIcon(icon9)
    principal.debug_button.setIconSize(QtCore.QSize(40, 40))
    principal.debug_button.setPopupMode(QtGui.QToolButton.DelayedPopup)
    principal.debug_button.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
    principal.debug_button.setObjectName(_fromUtf8("debug_button"))
    principal.render_boton = QtGui.QToolButton(principal)
    principal.render_boton.setGeometry(QtCore.QRect(270, 300, 131, 91))
    principal.render_boton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.render_boton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    icon10 = QtGui.QIcon()
    icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/StartRender.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.render_boton.setIcon(icon10)
    principal.render_boton.setIconSize(QtCore.QSize(90, 90))
    principal.render_boton.setPopupMode(QtGui.QToolButton.DelayedPopup)
    principal.render_boton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
    principal.render_boton.setObjectName(_fromUtf8("render_boton"))
    principal.options_group = QtGui.QGroupBox(principal)
    principal.options_group.setGeometry(QtCore.QRect(10, 210, 251, 191))
    principal.options_group.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
    principal.options_group.setFlat(False)
    principal.options_group.setCheckable(False)
    principal.options_group.setObjectName(_fromUtf8("options_group"))
    principal.frame = QtGui.QFrame(principal.options_group)
    principal.frame.setGeometry(QtCore.QRect(0, 10, 91, 81))
    principal.frame.setFrameShape(QtGui.QFrame.StyledPanel)
    principal.frame.setFrameShadow(QtGui.QFrame.Raised)
    principal.frame.setObjectName(_fromUtf8("frame"))
    principal.start_box = QtGui.QSpinBox(principal.frame)
    principal.start_box.setGeometry(QtCore.QRect(10, 10, 81, 22))
    font = QtGui.QFont()
    font.setPointSize(7)
    principal.start_box.setFont(font)
    principal.start_box.setWrapping(False)
    principal.start_box.setFrame(False)
    principal.start_box.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
    principal.start_box.setObjectName(_fromUtf8("start_box"))
    principal.end_box = QtGui.QSpinBox(principal.frame)
    principal.end_box.setEnabled(False)
    principal.end_box.setGeometry(QtCore.QRect(10, 30, 81, 22))
    font = QtGui.QFont()
    font.setPointSize(7)
    principal.end_box.setFont(font)
    principal.end_box.setWrapping(False)
    principal.end_box.setFrame(False)
    principal.end_box.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
    principal.end_box.setSuffix(_fromUtf8(""))
    principal.end_box.setMaximum(999999)
    principal.end_box.setObjectName(_fromUtf8("end_box"))
    principal.jump_box = QtGui.QSpinBox(principal.frame)
    principal.jump_box.setEnabled(False)
    principal.jump_box.setGeometry(QtCore.QRect(10, 50, 81, 22))
    font = QtGui.QFont()
    font.setPointSize(7)
    principal.jump_box.setFont(font)
    principal.jump_box.setWrapping(False)
    principal.jump_box.setFrame(False)
    principal.jump_box.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
    principal.jump_box.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
    principal.jump_box.setAccelerated(False)
    principal.jump_box.setSuffix(_fromUtf8(""))
    principal.jump_box.setMaximum(999999)
    principal.jump_box.setObjectName(_fromUtf8("jump_box"))
    principal.frame_2 = QtGui.QFrame(principal.options_group)
    principal.frame_2.setGeometry(QtCore.QRect(0, 90, 91, 41))
    principal.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
    principal.frame_2.setFrameShadow(QtGui.QFrame.Raised)
    principal.frame_2.setObjectName(_fromUtf8("frame_2"))
    principal.runPy_boton = QtGui.QToolButton(principal.frame_2)
    principal.runPy_boton.setGeometry(QtCore.QRect(10, 10, 21, 21))
    principal.runPy_boton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.runPy_boton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    icon11 = QtGui.QIcon()
    icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/runPy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.runPy_boton.setIcon(icon11)
    principal.runPy_boton.setIconSize(QtCore.QSize(40, 40))
    principal.runPy_boton.setCheckable(True)
    principal.runPy_boton.setChecked(False)
    principal.runPy_boton.setPopupMode(QtGui.QToolButton.DelayedPopup)
    principal.runPy_boton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
    principal.runPy_boton.setObjectName(_fromUtf8("runPy_boton"))
    principal.py_edit = QtGui.QLineEdit(principal.frame_2)
    principal.py_edit.setEnabled(True)
    principal.py_edit.setGeometry(QtCore.QRect(30, 10, 51, 21))
    sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(principal.py_edit.sizePolicy().hasHeightForWidth())
    principal.py_edit.setSizePolicy(sizePolicy)
    font = QtGui.QFont()
    font.setPointSize(6)
    principal.py_edit.setFont(font)
    principal.py_edit.setFrame(False)
    principal.py_edit.setReadOnly(False)
    principal.py_edit.setObjectName(_fromUtf8("py_edit"))
    principal.frame_3 = QtGui.QFrame(principal.options_group)
    principal.frame_3.setGeometry(QtCore.QRect(10, 130, 81, 31))
    principal.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
    principal.frame_3.setFrameShadow(QtGui.QFrame.Raised)
    principal.frame_3.setObjectName(_fromUtf8("frame_3"))
    principal.setThreads_SpinBox = QtGui.QSpinBox(principal.frame_3)
    principal.setThreads_SpinBox.setGeometry(QtCore.QRect(30, 0, 41, 31))
    font = QtGui.QFont()
    font.setPointSize(7)
    principal.setThreads_SpinBox.setFont(font)
    principal.setThreads_SpinBox.setWrapping(False)
    principal.setThreads_SpinBox.setFrame(False)
    principal.setThreads_SpinBox.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
    principal.setThreads_SpinBox.setPrefix(_fromUtf8(""))
    principal.setThreads_SpinBox.setObjectName(_fromUtf8("setThreads_SpinBox"))
    principal.setThreads_boton = QtGui.QToolButton(principal.frame_3)
    principal.setThreads_boton.setGeometry(QtCore.QRect(0, 0, 31, 31))
    principal.setThreads_boton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.setThreads_boton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    icon12 = QtGui.QIcon()
    icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/setThread.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.setThreads_boton.setIcon(icon12)
    principal.setThreads_boton.setIconSize(QtCore.QSize(40, 40))
    principal.setThreads_boton.setCheckable(True)
    principal.setThreads_boton.setChecked(False)
    principal.setThreads_boton.setPopupMode(QtGui.QToolButton.DelayedPopup)
    principal.setThreads_boton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
    principal.setThreads_boton.setObjectName(_fromUtf8("setThreads_boton"))
    principal.frame_4 = QtGui.QFrame(principal.options_group)
    principal.frame_4.setGeometry(QtCore.QRect(90, 10, 161, 101))
    principal.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
    principal.frame_4.setFrameShadow(QtGui.QFrame.Raised)
    principal.frame_4.setObjectName(_fromUtf8("frame_4"))
    principal.changeOutput_boton = QtGui.QToolButton(principal.frame_4)
    principal.changeOutput_boton.setGeometry(QtCore.QRect(10, 10, 141, 21))
    principal.changeOutput_boton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.changeOutput_boton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    icon13 = QtGui.QIcon()
    icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/imagenBrowse.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.changeOutput_boton.setIcon(icon13)
    principal.changeOutput_boton.setIconSize(QtCore.QSize(40, 40))
    principal.changeOutput_boton.setCheckable(True)
    principal.changeOutput_boton.setChecked(False)
    principal.changeOutput_boton.setPopupMode(QtGui.QToolButton.DelayedPopup)
    principal.changeOutput_boton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
    principal.changeOutput_boton.setObjectName(_fromUtf8("changeOutput_boton"))
    principal.browseOuput_boton = QtGui.QToolButton(principal.frame_4)
    principal.browseOuput_boton.setGeometry(QtCore.QRect(10, 40, 31, 31))
    principal.browseOuput_boton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.browseOuput_boton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    principal.browseOuput_boton.setIcon(icon7)
    principal.browseOuput_boton.setIconSize(QtCore.QSize(40, 40))
    principal.browseOuput_boton.setPopupMode(QtGui.QToolButton.DelayedPopup)
    principal.browseOuput_boton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
    principal.browseOuput_boton.setObjectName(_fromUtf8("browseOuput_boton"))
    principal.output_edit = QtGui.QLineEdit(principal.frame_4)
    principal.output_edit.setEnabled(True)
    principal.output_edit.setGeometry(QtCore.QRect(40, 40, 111, 21))
    font = QtGui.QFont()
    font.setPointSize(6)
    principal.output_edit.setFont(font)
    principal.output_edit.setFrame(False)
    principal.output_edit.setReadOnly(False)
    principal.output_edit.setObjectName(_fromUtf8("output_edit"))
    principal.format_combo = QtGui.QComboBox(principal.frame_4)
    principal.format_combo.setGeometry(QtCore.QRect(50, 70, 81, 22))
    font = QtGui.QFont()
    font.setPointSize(7)
    principal.format_combo.setFont(font)
    principal.format_combo.setIconSize(QtCore.QSize(16, 16))
    principal.format_combo.setObjectName(_fromUtf8("format_combo"))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.format_combo.addItem(_fromUtf8(""))
    principal.frame_5 = QtGui.QFrame(principal.options_group)
    principal.frame_5.setGeometry(QtCore.QRect(90, 110, 161, 51))
    principal.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
    principal.frame_5.setFrameShadow(QtGui.QFrame.Raised)
    principal.frame_5.setObjectName(_fromUtf8("frame_5"))
    principal.scena_edit = QtGui.QLineEdit(principal.frame_5)
    principal.scena_edit.setEnabled(True)
    principal.scena_edit.setGeometry(QtCore.QRect(50, 20, 101, 21))
    font = QtGui.QFont()
    font.setPointSize(6)
    principal.scena_edit.setFont(font)
    principal.scena_edit.setFrame(False)
    principal.scena_edit.setReadOnly(False)
    principal.scena_edit.setObjectName(_fromUtf8("scena_edit"))
    principal.cambiarScena_boton = QtGui.QToolButton(principal.frame_5)
    principal.cambiarScena_boton.setGeometry(QtCore.QRect(10, 10, 31, 31))
    principal.cambiarScena_boton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    principal.cambiarScena_boton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
    icon14 = QtGui.QIcon()
    icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/scena.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    principal.cambiarScena_boton.setIcon(icon14)
    principal.cambiarScena_boton.setIconSize(QtCore.QSize(40, 40))
    principal.cambiarScena_boton.setCheckable(True)
    principal.cambiarScena_boton.setPopupMode(QtGui.QToolButton.DelayedPopup)
    principal.cambiarScena_boton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
    principal.cambiarScena_boton.setObjectName(_fromUtf8("cambiarScena_boton"))
    principal.hibernar_check = QtGui.QCheckBox(principal.options_group)
    principal.hibernar_check.setGeometry(QtCore.QRect(10, 170, 70, 17))
    font = QtGui.QFont()
    font.setPointSize(7)
    principal.hibernar_check.setFont(font)
    principal.hibernar_check.setObjectName(_fromUtf8("hibernar_check"))
    principal.tab_tipo.setCurrentIndex(0)
    QtCore.QObject.connect(principal.lista_tareas, QtCore.SIGNAL(_fromUtf8("currentItemChanged(QListWidgetItem*,QListWidgetItem*)")), principal.cambiarScena_boton.toggle)
    QtCore.QMetaObject.connectSlotsByName(principal)
    principal.setWindowTitle(QtGui.QApplication.translate("principal", "Blender Console Manager", None, QtGui.QApplication.UnicodeUTF8))
    principal.tab_tipo.setToolTip(QtGui.QApplication.translate("principal", "<html><head/><body><p>Image: Render single image.</p><p>Animation:Render animation.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    principal.image_tab.setToolTip(QtGui.QApplication.translate("principal", "Render Single Image", None, QtGui.QApplication.UnicodeUTF8))
    principal.tab_tipo.setTabText(principal.tab_tipo.indexOf(principal.image_tab), QtGui.QApplication.translate("principal", "Image", None, QtGui.QApplication.UnicodeUTF8))
    principal.animation_tab.setToolTip(QtGui.QApplication.translate("principal", "Render Animation", None, QtGui.QApplication.UnicodeUTF8))
    principal.tab_tipo.setTabText(principal.tab_tipo.indexOf(principal.animation_tab), QtGui.QApplication.translate("principal", "Animation", None, QtGui.QApplication.UnicodeUTF8))
    principal.lista_tareas.setToolTip(QtGui.QApplication.translate("principal", "List of tasks.", None, QtGui.QApplication.UnicodeUTF8))
    principal.agregarTarea_boton.setToolTip(QtGui.QApplication.translate("principal", "Add new task.", None, QtGui.QApplication.UnicodeUTF8))
    principal.agregarTarea_boton.setText(QtGui.QApplication.translate("principal", "...", None, QtGui.QApplication.UnicodeUTF8))
    principal.quitarTarea_buton.setToolTip(QtGui.QApplication.translate("principal", "Delete Task.", None, QtGui.QApplication.UnicodeUTF8))
    principal.quitarTarea_buton.setText(QtGui.QApplication.translate("principal", "...", None, QtGui.QApplication.UnicodeUTF8))
    principal.quitarTarea_buton_2.setToolTip(QtGui.QApplication.translate("principal", "Save Task.", None, QtGui.QApplication.UnicodeUTF8))
    principal.quitarTarea_buton_2.setText(QtGui.QApplication.translate("principal", "...", None, QtGui.QApplication.UnicodeUTF8))
    principal.blendFile_group.setTitle(QtGui.QApplication.translate("principal", "Blend File:", None, QtGui.QApplication.UnicodeUTF8))
    principal.browseBlend_boton.setToolTip(QtGui.QApplication.translate("principal", "Browse Blend File.", None, QtGui.QApplication.UnicodeUTF8))
    principal.browseBlend_boton.setText(QtGui.QApplication.translate("principal", "...", None, QtGui.QApplication.UnicodeUTF8))
    principal.blender_group.setTitle(QtGui.QApplication.translate("principal", "Blender:", None, QtGui.QApplication.UnicodeUTF8))
    principal.browseBlender_button.setToolTip(QtGui.QApplication.translate("principal", "<html><head/><body><p>Browse Blender Directory:</p><p><img src=\":/iconos/recursos/browseBlenderToolTip.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    principal.browseBlender_button.setText(QtGui.QApplication.translate("principal", "...", None, QtGui.QApplication.UnicodeUTF8))
    principal.other_box.setTitle(QtGui.QApplication.translate("principal", "Others", None, QtGui.QApplication.UnicodeUTF8))
    principal.registrar_boton.setToolTip(QtGui.QApplication.translate("principal", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">Register .blend extension</span></pre></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    principal.registrar_boton.setText(QtGui.QApplication.translate("principal", "...", None, QtGui.QApplication.UnicodeUTF8))
    principal.debug_button.setToolTip(QtGui.QApplication.translate("principal", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">Start Blender and Turn debugging on</span></pre></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    principal.debug_button.setText(QtGui.QApplication.translate("principal", "...", None, QtGui.QApplication.UnicodeUTF8))
    principal.render_boton.setToolTip(QtGui.QApplication.translate("principal", "<html><head/><body><p><span style=\" font-size:16pt;\">Start </span><span style=\" font-size:20pt; color:#ff0000;\">Render!</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    principal.render_boton.setText(QtGui.QApplication.translate("principal", "...", None, QtGui.QApplication.UnicodeUTF8))
    principal.options_group.setTitle(QtGui.QApplication.translate("principal", "Options", None, QtGui.QApplication.UnicodeUTF8))
    principal.start_box.setToolTip(QtGui.QApplication.translate("principal", "Start Frame", None, QtGui.QApplication.UnicodeUTF8))
    principal.start_box.setPrefix(QtGui.QApplication.translate("principal", "StartFrame: ", None, QtGui.QApplication.UnicodeUTF8))
    principal.end_box.setToolTip(QtGui.QApplication.translate("principal", "Animation\'s end frame.", None, QtGui.QApplication.UnicodeUTF8))
    principal.end_box.setPrefix(QtGui.QApplication.translate("principal", "EndFrame: ", None, QtGui.QApplication.UnicodeUTF8))
    principal.jump_box.setToolTip(QtGui.QApplication.translate("principal", "Render every x frames (jump frames by this number)", None, QtGui.QApplication.UnicodeUTF8))
    principal.jump_box.setPrefix(QtGui.QApplication.translate("principal", "Jump: ", None, QtGui.QApplication.UnicodeUTF8))
    principal.runPy_boton.setToolTip(QtGui.QApplication.translate("principal", "Run the specified Python script (filename or Blender Text)", None, QtGui.QApplication.UnicodeUTF8))
    principal.runPy_boton.setText(QtGui.QApplication.translate("principal", "...", None, QtGui.QApplication.UnicodeUTF8))
    principal.setThreads_SpinBox.setToolTip(QtGui.QApplication.translate("principal", "Use amount of <threads> for rendering", None, QtGui.QApplication.UnicodeUTF8))
    principal.setThreads_boton.setToolTip(QtGui.QApplication.translate("principal", "<html><head/><body><p>Change default amount of &lt;threads&gt; for rendering</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    principal.setThreads_boton.setText(QtGui.QApplication.translate("principal", "...", None, QtGui.QApplication.UnicodeUTF8))
    principal.changeOutput_boton.setToolTip(QtGui.QApplication.translate("principal", "<html><head/><body><p>Change default ouput settings.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    principal.changeOutput_boton.setText(QtGui.QApplication.translate("principal", "...", None, QtGui.QApplication.UnicodeUTF8))
    principal.browseOuput_boton.setToolTip(QtGui.QApplication.translate("principal", "<html><head/><body><p>Browse for the file output.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    principal.browseOuput_boton.setText(QtGui.QApplication.translate("principal", "...", None, QtGui.QApplication.UnicodeUTF8))
    principal.output_edit.setToolTip(QtGui.QApplication.translate("principal", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">Set the render path and file name.</span></pre><pre style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">Use // as &lt;dir&gt; to use the path render relative to the blend file.</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">Use # in the filename to be replaced with the frame number</span></pre><pre style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">eg: blender -b foobar.blend -o //render_# -F PNG -x 1</span></pre></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setToolTip(QtGui.QApplication.translate("principal", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">Set the render format, Valid options are..</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">TGA IRIS HAMX FTYPE JPEG MOVIE IRIZ RAWTGA</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">AVIRAW AVIJPEG PNG BMP FRAMESERVER</span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">(formats that can be compiled into blender, </span></pre><pre style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">not available on all systems)</span></pre><pre style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New,courier\';\">HDR TIFF EXR MPEG AVICODEC QUICKTIME CINEON DPX</span></pre></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(0, QtGui.QApplication.translate("principal", "PNG", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(1, QtGui.QApplication.translate("principal", "TGA", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(2, QtGui.QApplication.translate("principal", "IRIS", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(3, QtGui.QApplication.translate("principal", "HAMX", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(4, QtGui.QApplication.translate("principal", "FTYPE", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(5, QtGui.QApplication.translate("principal", "JPEG", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(6, QtGui.QApplication.translate("principal", "MOVIE", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(7, QtGui.QApplication.translate("principal", "IRIZ", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(8, QtGui.QApplication.translate("principal", "RAWTGA", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(9, QtGui.QApplication.translate("principal", "AVIRAW", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(10, QtGui.QApplication.translate("principal", "AVIJPEG", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(11, QtGui.QApplication.translate("principal", "BMP", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(12, QtGui.QApplication.translate("principal", "FRAMESERVER", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(13, QtGui.QApplication.translate("principal", "HDR", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(14, QtGui.QApplication.translate("principal", "TIFF", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(15, QtGui.QApplication.translate("principal", "EXR", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(16, QtGui.QApplication.translate("principal", "MPEG", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(17, QtGui.QApplication.translate("principal", "AVICODEC", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(18, QtGui.QApplication.translate("principal", "QUICKTIME", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(19, QtGui.QApplication.translate("principal", "CINEON", None, QtGui.QApplication.UnicodeUTF8))
    principal.format_combo.setItemText(20, QtGui.QApplication.translate("principal", "DPX", None, QtGui.QApplication.UnicodeUTF8))
    principal.scena_edit.setToolTip(QtGui.QApplication.translate("principal", "<html><head/><body><pre style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Courier New,courier\';\"><br/></pre></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    principal.cambiarScena_boton.setToolTip(QtGui.QApplication.translate("principal", "<html><head/><body><p>Changed default Scene</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
    principal.cambiarScena_boton.setText(QtGui.QApplication.translate("principal", "...", None, QtGui.QApplication.UnicodeUTF8))
    principal.hibernar_check.setText(QtGui.QApplication.translate("principal", "Hibernate", None, QtGui.QApplication.UnicodeUTF8))
