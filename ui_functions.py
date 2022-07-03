################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################

## ==> GUI FILE
from main import *

## ==> GLOBALS

GLOBAL_STATE = 0

class UIFunctions(MainWindow):
    
    def init(self):
        self.ui.btn_maxi.setToolTip("Maximize")
        self.ui.btn_mini.setToolTip("sleep")
        self.ui.btn_close.setToolTip("close")

    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.Drop_Shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.ui.Drop_Shadow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.94, y1:0.892, x2:0.034, y2:0.085, stop:0.0501949 rgba(0, 0, 56, 255), stop:0.275797 rgba(39, 0, 59, 255), stop:0.545966 rgba(39, 0, 59, 255), stop:0.793621 rgba(0, 0, 74, 255), stop:0.949805 rgba(36, 0, 54, 255));")
            self.ui.btn_maxi.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.Drop_Shadow_layout.setContentsMargins(10, 10, 10, 10)
            self.ui.Drop_Shadow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.94, y1:0.892, x2:0.034, y2:0.085, stop:0.0501949 rgba(0, 0, 56, 255), stop:0.275797 rgba(39, 0, 59, 255), stop:0.545966 rgba(39, 0, 59, 255), stop:0.793621 rgba(0, 0, 74, 255), stop:0.949805 rgba(36, 0, 54, 255));")
            self.ui.btn_maxi.setToolTip("Maximize")

    ## ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.Drop_Shadow.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.btn_maxi.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.btn_mini.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.btn_close.clicked.connect(lambda: self.close())

        ## ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_grip)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px } QSizeGrip:hover { background-color: rgb(50, 42, 94) }")
        self.sizegrip.setToolTip("Resize Window") 


    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE
