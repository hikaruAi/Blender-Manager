#######################################
# Blender Console Manager 3 Main File:#
#              12/12/2012             #
#######################################

#imports#
from PyQt4 import QtCore,QtGui
import os,subprocess, recursos, sys, time
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
##APP
app = QtGui.QApplication(sys.argv)
#Classes
class Task(object):
    """Base class for all tasks"""
    def __init__(self):
        self.formatos=("PNG","TGA","IRIS","HAMX","FTYPE","JPEG","MOVIE",
                    "IRIZ","RAWTGA","AVIRAW","AVIJPEG","BMP","FRAMESERVER",
                    "HDR","TIFF","EXR","MPEG","AVICODEC","QUICKTIME","CINEON","DPX")
        self.blend="/Empty.blend"
        self.modo=0
        self.blender=str()
        self.startFrame=0
        self.endFrame=int()
        self.jump=1
        self.runPython=False
        self.pyScript=str()
        self.changeThreads=False
        self.threadsNumber=int()
        self.changeOutput=False
        self.outputFile=str()
        self.format=0
        self.changeScene=False
        self.scene=str()
        self.addItem()
    def title(self):
        blend=self.blend
        punto=blend.rfind("/")+1
        nombre=str()
        for i in range(punto,len(blend)):
            nombre+=blend[i]
        punto2=nombre.rfind(".")
        nombre2=str()
        for i in range(0,punto2):
            nombre2+=nombre[i]
        nombre2+=" ( "+str(self.startFrame)+", "+str(self.endFrame)+")"
        return(nombre2)
    def addItem(self):
        blendFileIco = QtGui.QIcon()
        blendFileIco.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/blendFile.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.item=QtGui.QListWidgetItem(blendFileIco,self.title(),principal.lista_tareas,1)
        taskList.append(self)
        principal.lista_tareas.setCurrentItem(self.item)
    def __repr__(self):
        return(self.title())
    def __str__(self):
        return(self.__repr__())
    def arg(self):
        comand="-b "
        comand+=(self.blend+" ")
        if self.changeOutput:
            comand+=("-o "+self.outputFile+" ")
            comand+=("-F "+self.formatos[self.format]+" ")
            comand+=("-x 1 ")
        if self.changeThreads:
            comand+=("-t "+str(self.threadsNumber)+" ")
        if self.changeScene:
            comand+=("-S "+self.scene+" ")
        if self.modo==0:
            comand+=("-f "+str(self.startFrame)+" ")
        elif self.modo==1:
            comand+=("-s "+str(self.startFrame)+" -e "+str(self.endFrame)+" -a ")
        else:
            pass
        if self.jump>1:
            comand+=("-j "+str(self.jump)+" ")
        if self.runPython:
            comand+=("-P "+self.pyScript+" ")
        return(comand)
###RENDER
def render():
    global taskList, taskId, processForm, app, principal, cancelar, hibernar
    QtCore.QObject.connect(processForm, QtCore.SIGNAL(_fromUtf8("destroyed")),cancelarRender)
    principal.setVisible(False)
    cancelar=False
    processForm.setWindowTitle("Rendering")
    for i in range(len(taskList)):
        if cancelar:
            tarea.terminate()
            break
        processForm.setWindowTitle(taskList[i].title())
        os.chdir(taskList[i].blender)
        batch=open("batch.bat","wt")
        batch.write("blender "+taskList[i].arg())
        batch.close()
        tarea=subprocess.Popen(["batch.bat",""],stdout=subprocess.PIPE,shell=True, universal_newlines=True)
        processForm.show()
        processForm.total_bar.setMaximum(len(taskList))
        processForm.total_bar.setValue(i)
        actual=int()
        total=int()
        if cancelar:
            tarea.terminate()
            break
        for linea in tarea.stdout:
            if "juan23287382asja" in linea:
                print("No file")
                tarea.kill()
                break
            else:
                pass
            if "Path Tracing Tile" in linea: #CYCLES
                punto=linea.rfind("Tile")+5
                a=""
                for c in range(punto,len(linea)):
                    a+=linea[c]
                    slash=a.rfind("/")
                    n=str()#Numerador
                    for p in range(0,slash):
                        n+=a[p]
                    d=str()#Denominador
                    for p in range(slash+1,len(a)):
                        d+=a[p]
                    processForm.setWindowTitle("Rendering: "+taskList[i].title()+" -- Cycles Render: "+a)
                actual=int(n)
                total=int(d)
                app.processEvents()
            elif "Part " in linea:#Render BI
                punto=linea.rfind("Part ")+4#Part n-d
                a=""
                for k in range(punto,len(linea)):
                    a+=linea[k]
                guion=linea.rfind("-")
                n=str()#Numerador
                for k in range(punto+1,guion):
                    n+=linea[k]
                d=str()#Denominador
                for k in range(guion+1,len(linea)):
                    d+=linea[k]
                actual=int(n)
                total=int(d)
                processForm.setWindowTitle("Rendering: "+taskList[i].title()+" -- BI Render: "+a)
                app.processEvents()
            else:#External Render
                processForm.setWindowTitle("Rendering: "+taskList[i].title()+" -- External Renderer")
                total=0
                actual=0
            processForm.actualBar.setMaximum(total)
            processForm.actualBar.setValue(actual)
            app.processEvents()
            processForm.info.appendPlainText(str(linea))
            app.processEvents()
            if cancelar:
                tarea.terminate()
                break
    processForm.setWindowTitle("Finished")
    principal.setVisible(True)
    os.remove("batch.bat")
    time.sleep(2)
    processForm.close()
    if cancelar==False and hibernar==True:
        os.system("shutdown /h")
######################################  FORMS #########################################3333

#Principal:
def principal_Make():#funcion constructora
    principal = QtGui.QWidget()
    principal.setWindowFlags(QtCore.Qt.Dialog)
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
    icon5 = QtGui.QIcon()
    icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/guardarIco.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
    principal.start_box.setMaximum(999999)
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
    principal.py_edit.setEnabled(False)
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
    principal.setThreads_SpinBox.setEnabled(False)
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
    principal.browseOuput_boton.setEnabled(False)
    principal.output_edit = QtGui.QLineEdit(principal.frame_4)
    principal.output_edit.setEnabled(False)
    principal.output_edit.setGeometry(QtCore.QRect(40, 40, 111, 21))
    font = QtGui.QFont()
    font.setPointSize(6)
    principal.output_edit.setFont(font)
    principal.output_edit.setFrame(False)
    principal.output_edit.setReadOnly(False)
    principal.output_edit.setObjectName(_fromUtf8("output_edit"))
    principal.format_combo = QtGui.QComboBox(principal.frame_4)
    principal.format_combo.setEnabled(False)
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
    principal.scena_edit.setEnabled(False)
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
    principal.hibernar_check.setToolTip("Hibernate computer when all task finish")
    font = QtGui.QFont()
    font.setPointSize(7)
    principal.hibernar_check.setFont(font)
    principal.hibernar_check.setObjectName(_fromUtf8("hibernar_check"))
    principal.tab_tipo.setCurrentIndex(0)
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
    return(principal)
principal=principal_Make() #Creo
###Eventos
#lista
def list_changed(n):
    global principal, processForm, warningForm, taskId
    taskId=n
    task=taskList[n]
    principal.blendFile_edit.setText(task.blend)
    principal.tab_tipo.setCurrentIndex(task.modo)
    principal.blender_edit.setText(task.blender)
    principal.start_box.setValue(task.startFrame)
    principal.end_box.setValue(task.endFrame)
    principal.jump_box.setValue(task.jump)
    principal.runPy_boton.setChecked(task.runPython)
    principal.py_edit.setText(task.pyScript)
    principal.setThreads_boton.setChecked(task.changeThreads)
    principal.setThreads_SpinBox.setValue(task.threadsNumber)
    principal.changeOutput_boton.setChecked(task.changeOutput)
    principal.output_edit.setText(task.outputFile)
    principal.format_combo.setCurrentIndex(task.format)
    principal.cambiarScena_boton.setChecked(task.changeScene)
    principal.scena_edit.setText(task.scene)
QtCore.QObject.connect(principal.lista_tareas, QtCore.SIGNAL(_fromUtf8("currentRowChanged (int)")),list_changed)
#tab
def tab_changed(n):
    global taskId, taskList, principal
    task=taskList[taskId]
    task.modo=n
    principal.end_box.setEnabled(bool(n))
    principal.jump_box.setEnabled(bool(n))
QtCore.QObject.connect(principal.tab_tipo, QtCore.SIGNAL(_fromUtf8("currentChanged (int)")),tab_changed)
#blend
def blendText_changed(text):
    global taskId, taskList, principal
    task=taskList[taskId]
    task.blend=text
QtCore.QObject.connect(principal.blendFile_edit, QtCore.SIGNAL(_fromUtf8("textChanged (QString)")),blendText_changed)
#browseBlend_boton
def browse_blend():
    global taskList, taskId, principal
    task=taskList[taskId]
    blend=QtGui.QFileDialog.getOpenFileName(principal,"Select Blend",os.getcwd(),"Blend File(*.blend)")
    principal.blendFile_edit.setText(blend)
    task.item.setText(task.title())
QtCore.QObject.connect(principal.browseBlend_boton, QtCore.SIGNAL(_fromUtf8("clicked()")),browse_blend)
#browse blender
def browse_blender():
    global taskList, taskId, principal
    task=taskList[taskId]
    blender=QtGui.QFileDialog.getExistingDirectory (principal,"Select Blender Folder",os.getcwd(),QtGui.QFileDialog.ShowDirsOnly)
    principal.blender_edit.setText(blender)
QtCore.QObject.connect(principal.browseBlender_button, QtCore.SIGNAL(_fromUtf8("clicked()")),browse_blender) 
#Blender text
def blenderText_changed(text):
    global taskId, taskList, principal
    task=taskList[taskId]
    task.blender=text
QtCore.QObject.connect(principal.blender_edit, QtCore.SIGNAL(_fromUtf8("textChanged (QString)")),blenderText_changed)
#Start Frame
def startFrame_changed(n):
    global taskList, taskId
    task=taskList[taskId]
    task.startFrame=n
    task.item.setText(task.title())
QtCore.QObject.connect(principal.start_box, QtCore.SIGNAL(_fromUtf8("valueChanged (int)")),startFrame_changed)
#end_box
def endBox_changed(n):
    global taskId, taskList, principal
    task=taskList[taskId]
    task.endFrame=n
    task.item.setText(task.title())
QtCore.QObject.connect(principal.end_box, QtCore.SIGNAL(_fromUtf8("valueChanged (int)")),endBox_changed)
#jump_box
def jumpBox_changed(n):
    global taskList, taskId
    task=taskList[taskId]
    task.jump=n
QtCore.QObject.connect(principal.jump_box, QtCore.SIGNAL(_fromUtf8("valueChanged (int)")),jumpBox_changed)
#runPy_boton
def runPyBoton_toggle(valor):
    global taskList, taskId, principal
    task=taskList[taskId]
    task.runPython=valor
    principal.py_edit.setEnabled(valor)
QtCore.QObject.connect(principal.runPy_boton, QtCore.SIGNAL(_fromUtf8("toggled (bool)")),runPyBoton_toggle)
#py_edit
def pyEdit_changed(text):
    global taskId, taskList, principal
    task=taskList[taskId]
    task.pyScript=text
QtCore.QObject.connect(principal.py_edit, QtCore.SIGNAL(_fromUtf8("textChanged (QString)")),pyEdit_changed)
#setThreads_boton
def setThreads_toggled(valor):
    global taskId, taskList, principal
    task=taskList[taskId]
    principal.setThreads_SpinBox.setEnabled(valor)
    task.changeThreads=valor
QtCore.QObject.connect(principal.setThreads_boton, QtCore.SIGNAL(_fromUtf8("toggled (bool)")),setThreads_toggled)
#setThreads_SpinBox
def threadsN_changed(n):
    global taskList, taskId
    task=taskList[taskId]
    task.threadsNumber=n
QtCore.QObject.connect(principal.setThreads_SpinBox, QtCore.SIGNAL(_fromUtf8("valueChanged (int)")),threadsN_changed)
#changeOutput_boton
def changeOutput_toggled(valor):
    global taskList, taskId, principal
    task=taskList[taskId]
    principal.output_edit.setEnabled(valor)
    principal.browseOuput_boton.setEnabled(valor)
    principal.format_combo.setEnabled(valor)
    task.changeOutput=valor
QtCore.QObject.connect(principal.changeOutput_boton, QtCore.SIGNAL(_fromUtf8("toggled (bool)")),changeOutput_toggled)
#output_edit
def ouputEdit_chaged(text):
    global taskList, taskId
    task=taskList[taskId]
    task.outputFile=text
QtCore.QObject.connect(principal.output_edit, QtCore.SIGNAL(_fromUtf8("textChanged (QString)")),ouputEdit_chaged)
#browseOuput_boton
def browseOutput_clicked():
    global principal
    archivo=QtGui.QFileDialog.getSaveFileName(principal,"Output File","Images(*.*)")
    principal.output_edit.setText(archivo)
QtCore.QObject.connect(principal.browseOuput_boton, QtCore.SIGNAL(_fromUtf8("clicked()")),browseOutput_clicked) 
#format_combo
def formatCombo_activated(n):
    global taskList, taskId
    task=taskList[taskId]
    task.format=n
QtCore.QObject.connect(principal.format_combo, QtCore.SIGNAL(_fromUtf8("activated (int)")),formatCombo_activated) 
#cambiarScena_boton
def cambiarScena_toggled(valor):
    global taskList, taskId, principal
    task=taskList[taskId]
    principal.scena_edit.setEnabled(valor)
    task.changeScene=valor
QtCore.QObject.connect(principal.cambiarScena_boton, QtCore.SIGNAL(_fromUtf8("toggled (bool)")),cambiarScena_toggled)
#scena_edit
def escenaEdit_changed(text):
    global taskList, taskId
    task=taskList[taskId]
    task.scene=text
QtCore.QObject.connect(principal.scena_edit, QtCore.SIGNAL(_fromUtf8("textChanged (QString)")),escenaEdit_changed)
#hibernar_check
def hibernarCheck_toggled(valor):
    global hibernar
    hibernar=valor
QtCore.QObject.connect(principal.hibernar_check, QtCore.SIGNAL(_fromUtf8("toggled (bool)")),hibernarCheck_toggled)
#render_boton
def renderBoton_click():
    global principal, warningForm, taskList, taskId
    task=taskList[taskId]
    if task.blender=="":
        warningForm.show()
        warningForm.setWindowTitle("ERROR!!")
        warningForm.mensaje.setText("The blender folder can't be empty")
    if task.blend=="/Empty.blend":
        warningForm.show()
        warningForm.setWindowTitle("ERROR")
        warningForm.mensaje.setText("First select a blend file")
    elif task.blender!="" and task.blend!="/Empty.blend":
        render()
QtCore.QObject.connect(principal.render_boton, QtCore.SIGNAL(_fromUtf8("clicked()")),renderBoton_click)
def agregar_click():
    global taskList, taskId
    a=Task()
QtCore.QObject.connect(principal.agregarTarea_boton, QtCore.SIGNAL(_fromUtf8("clicked()")),agregar_click)
def borrar_click():
    global principal, taskList, taskId
    item=principal.lista_tareas.takeItem(taskId)
    taskList.remove(taskList[taskId])
QtCore.QObject.connect(principal.quitarTarea_buton, QtCore.SIGNAL(_fromUtf8("clicked()")),borrar_click)
#registrar_boton
def registar_click():
    blender=QtGui.QFileDialog.getExistingDirectory (principal,"Select Blender Folder",os.getcwd(),QtGui.QFileDialog.ShowDirsOnly)
    if blender=="":
        pass
    else:
        os.chdir(blender)
        subprocess.Popen(["blender","-r"])
QtCore.QObject.connect(principal.registrar_boton, QtCore.SIGNAL(_fromUtf8("clicked()")),registar_click)
#debug_button
def debug_click():
    blender=QtGui.QFileDialog.getExistingDirectory (principal,"Select Blender Folder",os.getcwd(),QtGui.QFileDialog.ShowDirsOnly)
    if blender=="":
        pass
    else:
        os.chdir(blender)
        subprocess.Popen(["blender","-d"])
QtCore.QObject.connect(principal.debug_button, QtCore.SIGNAL(_fromUtf8("clicked()")),debug_click)
######ProcessForm
def processForm_Make():
    process_form=QtGui.QWidget()
    process_form.setWindowFlags(QtCore.Qt.Dialog)
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
    return(process_form)
processForm=processForm_Make()
def cancelarRender():
    global cancelar, proceesForm
    cancelar=True
    processForm.close()
    os.remove("batch.bat")
QtCore.QObject.connect(processForm.cancel_boton, QtCore.SIGNAL(_fromUtf8("clicked()")),cancelarRender)


########Warning Form
def warningForm_Make():
    warning_form=QtGui.QWidget()
    warning_form.setWindowFlags(QtCore.Qt.Dialog)
    warning_form.setObjectName(_fromUtf8("warning_form"))
    warning_form.setWindowModality(QtCore.Qt.ApplicationModal)
    warning_form.resize(341, 105)
    warning_form.setWindowOpacity(0.98)
    warning_form.ok_button = QtGui.QDialogButtonBox(warning_form)
    warning_form.ok_button.setGeometry(QtCore.QRect(80, 70, 156, 23))
    warning_form.ok_button.setStandardButtons(QtGui.QDialogButtonBox.Ok)
    warning_form.ok_button.setObjectName(_fromUtf8("ok_button"))
    warning_form.imagen = QtGui.QLabel(warning_form)
    warning_form.imagen.setGeometry(QtCore.QRect(10, 10, 101, 91))
    warning_form.imagen.setText(_fromUtf8(""))
    warning_form.imagen.setPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/recursos/errorIco.png")))
    warning_form.imagen.setObjectName(_fromUtf8("imagen"))
    warning_form.mensaje = QtGui.QLabel(warning_form)
    warning_form.mensaje.setGeometry(QtCore.QRect(70, 20, 261, 20))
    font = QtGui.QFont()
    font.setPointSize(13)
    warning_form.mensaje.setFont(font)
    warning_form.mensaje.setAlignment(QtCore.Qt.AlignCenter)
    warning_form.mensaje.setObjectName(_fromUtf8("mensaje"))
    QtCore.QMetaObject.connectSlotsByName(warning_form)
    warning_form.setWindowTitle(QtGui.QApplication.translate("warning_form", "Form", None, QtGui.QApplication.UnicodeUTF8))
    warning_form.mensaje.setText(QtGui.QApplication.translate("warning_form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
    return(warning_form)
warningForm=warningForm_Make()
def aceptar_warning():
    global warningForm
    warningForm.close()
QtCore.QObject.connect(warningForm.ok_button, QtCore.SIGNAL(_fromUtf8("accepted()")),aceptar_warning)
#### INIT
taskList=list()
hibernar=False
taskId=0
cancelar=False
############
principal.show()
a=Task()

sys.exit(app.exec_())