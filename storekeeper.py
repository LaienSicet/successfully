from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from pickle import dump, load


SLOI, SLOI_2, SLOI_3, SLAID = 1, 1, 1, 1
kolor_aktiv_kno = "blue"
#kolor = ["white", "red", "violet", "purple", "blue", "green", "yellow", "orange", "red", "black"]
ohi = ''

logi = []
baza_zapas, baza_inf, baza_blokov, baza_inf_blokov = {}, {}, {}, {}

teh = [['log', logi], ['baza_zapas', baza_zapas], ['baza_inf', baza_inf],
       ['baza_blokov', baza_blokov], ['baza_inf_blokov', baza_inf_blokov]]
for l, i in enumerate(teh):
    try:
        with open(i[0]+'.bin', 'rb') as fa:
            teh[l][1] = load(fa)
    except:
        with open(i[0]+'.bin', 'wb') as fa:
            dump(i[1], fa)

logi = teh[0][1]
baza_zapas = teh[1][1]
baza_inf = teh[2][1]
baza_blokov = teh[3][1]
baza_inf_blokov = teh[4][1]


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font_1, font_2, font_3, font_4, font_5, font_6, font_7, font_8, font_9 = QtGui.QFont(), QtGui.QFont(),\
            QtGui.QFont(), QtGui.QFont(), QtGui.QFont(), QtGui.QFont(), QtGui.QFont(), QtGui.QFont(), QtGui.QFont()
        spisok_font = [[font_1, 14, True], [font_2, 23, True], [font_3, 12, True], [font_4, 16, True],
                       [font_5, 20, True], [font_6, 26, True], [font_7, 10, True], [font_8, 16, False],
                       [font_9, 12, False]]
        for i in range(len(spisok_font)):
            spisok_font[i][0].setFamily("Segoe Print")
            spisok_font[i][0].setPointSize(spisok_font[i][1])
            spisok_font[i][0].setBold(spisok_font[i][2])
            spisok_font[i][0].setWeight(75)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 260, 40))
        self.pushButton.setFont(font_1)
        if SLOI == 1:
            self.pushButton.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
        self.pushButton.clicked.connect(lambda: knopka_izmen_sloi(1))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 10, 260, 40))
        self.pushButton_2.setFont(font_1)
        if SLOI == 2:
            self.pushButton_2.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
        self.pushButton_2.clicked.connect(lambda: knopka_izmen_sloi(2))

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 10, 260, 40))
        self.pushButton_3.setFont(font_1)
        if SLOI == 3:
            self.pushButton_3.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
        self.pushButton_3.clicked.connect(lambda: knopka_izmen_sloi(3))

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(880, 10, 260, 40))
        self.pushButton_4.setFont(font_1)
        if SLOI == 4:
            self.pushButton_4.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
        self.pushButton_4.clicked.connect(lambda: knopka_izmen_sloi(4))

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1170, 10, 260, 40))
        self.pushButton_5.setFont(font_1)
        if SLOI == 5:
            self.pushButton_5.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
        self.pushButton_5.clicked.connect(lambda: knopka_izmen_sloi(5))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 60, 300, 50))
        self.label.setFont(font_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(1250, 750, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(8)
        font.setWeight(75)
        self.label_1.setFont(font)
####################################################################################################################
        if SLOI == 1:
            self.spisok_b_z = []
            x = 0
            y = 0
            for i in baza_zapas:
                self.label_z = QtWidgets.QLabel(self.centralwidget)
                self.label_z.setGeometry(QtCore.QRect(45 + 350*y, 120 + 40*x, 300, 50))
                self.label_z.setFont(font_3)
                self.spisok_b_z.append([self.label_z, i])
                x += 1
                if x == 15 and y <= 2:
                    x = 0
                    y += 1
###################################################################################################################
        if SLOI == 2:
            self.spisok_izm_d = []
            x = 0
            y = 0
            for i in baza_zapas:
                self.label_p = QtWidgets.QLabel(self.centralwidget)
                self.label_p.setGeometry(QtCore.QRect(45 + 350 * y, 120 + 40 * x, 250, 50))
                self.label_p.setFont(font_3)

                self.spinBox_p = QtWidgets.QSpinBox(self.centralwidget)
                self.spinBox_p.setGeometry(QtCore.QRect(280 + 350 * y, 130 + 40 * x, 75, 25))
                self.spinBox_p.setFont(font_1)
                self.spinBox_p.setRange(0, 9999)
                self.spisok_izm_d.append([self.label_p, i, self.spinBox_p])
                x += 1
                if x == 15 and y <= 2:
                    x = 0
                    y += 1

            self.pushButton_pri = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_pri.setGeometry(QtCore.QRect(590, 740, 260, 40))
            self.pushButton_pri.setFont(font_1)
            self.pushButton_pri.clicked.connect(lambda: popolnenie_zapacov(1))
###################################################################################################################
        if SLOI == 3:
            self.pushButton_rash_d = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_rash_d.setGeometry(QtCore.QRect(300, 75, 260, 40))
            self.pushButton_rash_d.setFont(font_1)
            if SLOI_2 == 1:
                self.pushButton_rash_d.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
            self.pushButton_rash_d.clicked.connect(lambda: knopka_izmen_sloi_2(1))

            self.pushButton_rash_bl = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_rash_bl.setGeometry(QtCore.QRect(880, 75, 260, 40))
            self.pushButton_rash_bl.setFont(font_1)
            if SLOI_2 == 2:
                self.pushButton_rash_bl.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
            self.pushButton_rash_bl.clicked.connect(lambda: knopka_izmen_sloi_2(2))

            if SLOI_2 == 1:
                self.pushButton_trat_d = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_trat_d.setGeometry(QtCore.QRect(590, 740, 260, 40))
                self.pushButton_trat_d.setFont(font_1)
                self.pushButton_trat_d.clicked.connect(lambda: popolnenie_zapacov(-1))

                self.spisok_izm_d = []
                x = 0
                y = 0
                for i in baza_zapas:
                    self.label_r = QtWidgets.QLabel(self.centralwidget)
                    self.label_r.setGeometry(QtCore.QRect(45 + 350 * y, 130 + 40 * x, 250, 50))
                    self.label_r.setFont(font_3)

                    self.spinBox_r = QtWidgets.QSpinBox(self.centralwidget)
                    self.spinBox_r.setGeometry(QtCore.QRect(280 + 350 * y, 140 + 40 * x, 75, 25))
                    self.spinBox_r.setFont(font_1)
                    self.spinBox_r.setRange(0, baza_zapas[i])

                    self.spisok_izm_d.append([self.label_r, i, self.spinBox_r])
                    x += 1
                    if x == 15 and y <= 2:
                        x = 0
                        y += 1

            if SLOI_2 == 2:
                if SLOI_3 == 1:
                    self.spisok_rash_blo = []
                    x = 0
                    y = 0
                    for i in baza_blokov:
                        self.label_rash_blo = QtWidgets.QLabel(self.centralwidget)
                        self.label_rash_blo.setGeometry(QtCore.QRect(45 + 350 * y, 150 + 50 * x, 250, 50))
                        self.label_rash_blo.setFont(font_4)

                        self.spinBox_rash_blo = QtWidgets.QSpinBox(self.centralwidget)
                        self.spinBox_rash_blo.setGeometry(QtCore.QRect(290 + 350 * y, 160 + 50 * x, 50, 25))
                        self.spinBox_rash_blo.setFont(font_1)
                        self.spinBox_rash_blo.setRange(0, 99)

                        self.spisok_rash_blo.append([self.label_rash_blo, i, self.spinBox_rash_blo])
                        x += 1
                        if x == 10 and y <= 2:
                            x = 0
                            y += 1

                    self.label_teh_stroka = QtWidgets.QLabel(self.centralwidget)
                    self.label_teh_stroka.setGeometry(QtCore.QRect(50, 720, 1300, 50))
                    self.label_teh_stroka.setFont(font_4)
                    self.label_teh_stroka.setAlignment(QtCore.Qt.AlignCenter)

                    self.pushButton_3_2_blo_dez_izm = QtWidgets.QPushButton(self.centralwidget)
                    self.pushButton_3_2_blo_dez_izm.setGeometry(QtCore.QRect(440, 670, 260, 40))
                    self.pushButton_3_2_blo_dez_izm.setFont(font_1)
                    self.pushButton_3_2_blo_dez_izm.clicked.connect(kno_3_2_blo_dez_izm)

                    self.pushButton_3_2_vihit_blocov = QtWidgets.QPushButton(self.centralwidget)
                    self.pushButton_3_2_vihit_blocov.setGeometry(QtCore.QRect(740, 670, 260, 40))
                    self.pushButton_3_2_vihit_blocov.setFont(font_1)
                    self.pushButton_3_2_vihit_blocov.clicked.connect(kno_rashod_blok)

                if SLOI_3 == 2:
                    self.label_3_2_1_zagolovok = QtWidgets.QLabel(self.centralwidget)
                    self.label_3_2_1_zagolovok.setGeometry(QtCore.QRect(45, 175, 350, 50))
                    self.label_3_2_1_zagolovok.setFont(font_5)

                    self.spisok_smeta_0 = []
                    x = 0
                    y = 0
                    for i in smeta_0:
                        self.label_s_0 = QtWidgets.QLabel(self.centralwidget)
                        self.label_s_0.setGeometry(QtCore.QRect(45 + 500 * y, 250 + 50 * x, 400, 50))
                        self.label_s_0.setFont(font_4)
                        self.spisok_smeta_0.append([self.label_s_0, i])
                        x += 1
                        if x == 5 and y <= 1:
                            x = 0
                            y += 1

                    self.pushButton_3_2_1_odratno = QtWidgets.QPushButton(self.centralwidget)
                    self.pushButton_3_2_1_odratno.setGeometry(QtCore.QRect(440, 600, 260, 40))
                    self.pushButton_3_2_1_odratno.setFont(font_1)
                    self.pushButton_3_2_1_odratno.clicked.connect(lambda: knopka_izmen_sloi_3(1))

                    self.pushButton_3_2_1_nehvat = QtWidgets.QPushButton(self.centralwidget)
                    self.pushButton_3_2_1_nehvat.setGeometry(QtCore.QRect(740, 600, 260, 40))
                    self.pushButton_3_2_1_nehvat.setFont(font_1)
                    self.pushButton_3_2_1_nehvat.clicked.connect(kno_3_2_nedostayhee)

                if SLOI_3 == 3:
                    self.label_3_2_1_zagolovok = QtWidgets.QLabel(self.centralwidget)
                    self.label_3_2_1_zagolovok.setGeometry(QtCore.QRect(45, 175, 350, 50))
                    self.label_3_2_1_zagolovok.setFont(font_5)

                    self.spisok_smeta_0 = []
                    x = 0
                    y = 0
                    for i in smeta_1:
                        self.label_s_0 = QtWidgets.QLabel(self.centralwidget)
                        self.label_s_0.setGeometry(QtCore.QRect(45 + 500 * y, 250 + 50 * x, 400, 50))
                        self.label_s_0.setFont(font_4)
                        self.spisok_smeta_0.append([self.label_s_0, i])
                        x += 1
                        if x == 5 and y <= 1:
                            x = 0
                            y += 1

                    self.pushButton_3_2_2_odratno = QtWidgets.QPushButton(self.centralwidget)
                    self.pushButton_3_2_2_odratno.setGeometry(QtCore.QRect(440, 600, 260, 40))
                    self.pushButton_3_2_2_odratno.setFont(font_1)
                    self.pushButton_3_2_2_odratno.clicked.connect(lambda: knopka_izmen_sloi_3(1))

                    if len(smeta_1) != 0:
                        self.pushButton_3_2_2_txt = QtWidgets.QPushButton(self.centralwidget)
                        self.pushButton_3_2_2_txt.setGeometry(QtCore.QRect(740, 600, 260, 40))
                        self.pushButton_3_2_2_txt.setFont(font_1)
                        self.pushButton_3_2_2_txt.clicked.connect(lambda: kno_xtx(smeta_1))
###################################################################################################################
        if SLOI == 4:
            self.pushButton_4_det = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_4_det.setGeometry(QtCore.QRect(300, 75, 260, 40))
            self.pushButton_4_det.setFont(font_1)
            if SLOI_2 == 1:
                self.pushButton_4_det.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
            self.pushButton_4_det.clicked.connect(lambda: knopka_izmen_sloi_2(1))

            self.pushButton_4_del_det = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_4_del_det.setGeometry(QtCore.QRect(10, 75, 260, 40))
            self.pushButton_4_del_det.setFont(font_1)
            if SLOI_2 == 2:
                self.pushButton_4_del_det.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
            self.pushButton_4_del_det.clicked.connect(lambda: knopka_izmen_sloi_2(2))

            self.pushButton_4_blo = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_4_blo.setGeometry(QtCore.QRect(880, 75, 260, 40))
            self.pushButton_4_blo.setFont(font_1)
            if SLOI_2 == 3:
                self.pushButton_4_blo.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
            self.pushButton_4_blo.clicked.connect(lambda: knopka_izmen_sloi_2(3))

            self.pushButton_4_del_blo = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_4_del_blo.setGeometry(QtCore.QRect(1170, 75, 260, 40))
            self.pushButton_4_del_blo.setFont(font_1)
            if SLOI_2 == 4:
                self.pushButton_4_del_blo.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
            self.pushButton_4_del_blo.clicked.connect(lambda: knopka_izmen_sloi_2(4))

            if SLOI_2 == 1:
                self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
                self.textEdit.setGeometry(QtCore.QRect(300, 300, 260, 50))
                font = QtGui.QFont()
                font.setFamily("Segoe Script")
                font.setPointSize(16)
                self.textEdit.setFont(font)

                self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
                self.plainTextEdit.setGeometry(QtCore.QRect(700, 300, 645, 320))
                font = QtGui.QFont()
                font.setFamily("Segoe Script")
                font.setPointSize(14)
                self.plainTextEdit.setFont(font)

                self.spinBox_skolko = QtWidgets.QSpinBox(self.centralwidget)
                self.spinBox_skolko.setGeometry(QtCore.QRect(410, 435, 75, 25))
                self.spinBox_skolko.setFont(font_1)
                self.spinBox_skolko.setRange(0, 999)

                self.label_nazv = QtWidgets.QLabel(self.centralwidget)
                self.label_nazv.setGeometry(QtCore.QRect(300, 250, 250, 50))
                self.label_nazv.setFont(font_4)

                self.label_opi = QtWidgets.QLabel(self.centralwidget)
                self.label_opi.setGeometry(QtCore.QRect(700, 250, 250, 50))
                self.label_opi.setFont(font_4)

                self.label_skolko = QtWidgets.QLabel(self.centralwidget)
                self.label_skolko.setGeometry(QtCore.QRect(300, 425, 100, 50))
                self.label_skolko.setFont(font_4)

                self.pushButton_4_2_dobav_det = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_4_2_dobav_det.setGeometry(QtCore.QRect(300, 560, 260, 40))
                self.pushButton_4_2_dobav_det.setFont(font_1)
                self.pushButton_4_2_dobav_det.clicked.connect(knopka_dobavl_det)

                self.label_teh_stroka = QtWidgets.QLabel(self.centralwidget)
                self.label_teh_stroka.setGeometry(QtCore.QRect(300, 625, 750, 50))
                self.label_teh_stroka.setFont(font_4)
                self.label_teh_stroka.setAlignment(QtCore.Qt.AlignCenter)

            if SLOI_2 == 2:
                self.spisok_del_det = []
                x = 0
                y = 0
                self.pushButton_del_det = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_del_det.setGeometry(QtCore.QRect(590, 740, 260, 40))
                self.pushButton_del_det.setFont(font_1)
                self.pushButton_del_det.clicked.connect(knopka_del_det)

                for i in baza_zapas:
                    self.label_del_det = QtWidgets.QLabel(self.centralwidget)
                    self.label_del_det.setGeometry(QtCore.QRect(45 + 350 * y, 130 + 40 * x, 200, 30))
                    self.label_del_det.setFont(font_3)
                    z = 0
                    if proverka_isp_det(i) == True:
                        z = 1
                    self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
                    self.checkBox.setGeometry(QtCore.QRect(250 + 350 * y, 130 + 40 * x + 5000 * z, 25, 25))
                    self.checkBox.setText("")

                    self.spisok_del_det.append([self.label_del_det, i, self.checkBox])

                    x += 1
                    if x == 15 and y <= 2:
                        x = 0
                        y += 1

                self.label_primahanie = QtWidgets.QLabel(self.centralwidget)
                self.label_primahanie.setGeometry(QtCore.QRect(20, 750, 500, 30))

                self.label_primahanie.setFont(font_9)

            if SLOI_2 == 3:
                self.label_nazv = QtWidgets.QLabel(self.centralwidget)
                self.label_nazv.setGeometry(QtCore.QRect(25, 170, 250, 50))

                self.label_nazv.setFont(font_8)

                self.label_opi = QtWidgets.QLabel(self.centralwidget)
                self.label_opi.setGeometry(QtCore.QRect(25, 300, 250, 50))
                self.label_opi.setFont(font_8)

                self.label_sost_iz = QtWidgets.QLabel(self.centralwidget)
                self.label_sost_iz.setGeometry(QtCore.QRect(320, 140, 250, 50))
                self.label_sost_iz.setFont(font_8)

                self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
                self.textEdit.setGeometry(QtCore.QRect(25, 220, 260, 50))
                font = QtGui.QFont()
                font.setFamily("Segoe Script")
                font.setPointSize(16)
                self.textEdit.setFont(font)

                self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
                self.plainTextEdit.setGeometry(QtCore.QRect(25, 350, 280, 300))
                font = QtGui.QFont()
                font.setFamily("Segoe Script")
                font.setPointSize(14)
                self.plainTextEdit.setFont(font)

                self.pushButton_4_3_dobav_blo = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_4_3_dobav_blo.setGeometry(QtCore.QRect(45, 680, 260, 40))
                self.pushButton_4_3_dobav_blo.setFont(font_1)
                self.pushButton_4_3_dobav_blo.clicked.connect(knopka_dobavl_blo)

                self.label_teh_stroka = QtWidgets.QLabel(self.centralwidget)
                self.label_teh_stroka.setGeometry(QtCore.QRect(100, 725, 750, 50))
                self.label_teh_stroka.setFont(font_4)
                self.label_teh_stroka.setAlignment(QtCore.Qt.AlignCenter)

                self.spisok_nov_blok = []
                x = 0
                y = 0
                for i in baza_zapas:
                    self.label_nov_blok = QtWidgets.QLabel(self.centralwidget)
                    self.label_nov_blok.setGeometry(QtCore.QRect(340 + 280 * y, 185 + 35 * x, 150, 50))
                    self.label_nov_blok.setFont(font_7)

                    self.spinBox_nov_blok = QtWidgets.QSpinBox(self.centralwidget)
                    self.spinBox_nov_blok.setGeometry(QtCore.QRect(500 + 280 * y, 195 + 35 * x, 75, 25))
                    self.spinBox_nov_blok.setFont(font_1)
                    self.spinBox_nov_blok.setRange(0, 99)

                    self.spisok_nov_blok.append([self.label_nov_blok, i, self.spinBox_nov_blok])
                    x += 1
                    if x == 15 and y <= 2:
                        x = 0
                        y += 1

            if SLOI_2 == 4:
                self.spisok_del_blo = []
                x = 0
                y = 0
                self.pushButton_del_blo = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_del_blo.setGeometry(QtCore.QRect(590, 690, 260, 40))
                self.pushButton_del_blo.setFont(font_1)
                self.pushButton_del_blo.clicked.connect(knopka_del_blo)

                for i in baza_blokov:
                    self.label_del_det = QtWidgets.QLabel(self.centralwidget)
                    self.label_del_det.setGeometry(QtCore.QRect(45 + 350 * y, 150 + 50 * x, 250, 50))
                    self.label_del_det.setFont(font_4)

                    self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
                    self.checkBox.setGeometry(QtCore.QRect(300 + 350 * y, 165 + 50 * x, 25, 25))
                    self.checkBox.setText("")

                    self.spisok_del_blo.append([self.label_del_det, i, self.checkBox])

                    x += 1
                    if x == 10 and y <= 2:
                        x = 0
                        y += 1
####################################################################################################################
        if SLOI == 5:
            self.pushButton_5_inf_prog = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_5_inf_prog.setGeometry(QtCore.QRect(10, 75, 260, 40))
            self.pushButton_5_inf_prog.setFont(font_1)
            if SLOI_2 == 1:
                self.pushButton_5_inf_prog.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
            self.pushButton_5_inf_prog.clicked.connect(lambda: knopka_izmen_sloi_2(1))

            self.pushButton_5_inf_det = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_5_inf_det.setGeometry(QtCore.QRect(300, 75, 260, 40))
            self.pushButton_5_inf_det.setFont(font_1)
            if SLOI_2 == 2:
                self.pushButton_5_inf_det.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
            self.pushButton_5_inf_det.clicked.connect(lambda: knopka_izmen_sloi_2(2))

            if (SLOI_2 == 2 or SLOI_2 == 3 or SLOI_2 == 4) and SLAID > 1:
                self.pushButton_5_sla_obr = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_5_sla_obr.setGeometry(QtCore.QRect(110, 300, 60, 50))
                self.pushButton_5_sla_obr.setFont(font_5)
                self.pushButton_5_sla_obr.clicked.connect(lambda: knopka_sla(-1))

            if (SLOI_2 == 2 and SLAID < len(baza_inf)) or (SLOI_2 == 3 and SLAID < len(baza_inf_blokov)) or \
                    (SLOI_2 == 4 and SLAID < len(logi) / 10):
                self.pushButton_5_sla_tyda = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_5_sla_tyda.setGeometry(QtCore.QRect(1270, 300, 60, 50))
                self.pushButton_5_sla_tyda.setFont(font_5)
                self.pushButton_5_sla_tyda.clicked.connect(lambda: knopka_sla(1))

            self.pushButton_5_inf_blo = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_5_inf_blo.setGeometry(QtCore.QRect(880, 75, 260, 40))
            self.pushButton_5_inf_blo.setFont(font_1)
            if SLOI_2 == 3:
                self.pushButton_5_inf_blo.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
            self.pushButton_5_inf_blo.clicked.connect(lambda: knopka_izmen_sloi_2(3))

            self.pushButton_5_logi = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_5_logi.setGeometry(QtCore.QRect(1170, 75, 260, 40))
            self.pushButton_5_logi.setFont(font_1)
            if SLOI_2 == 4:
                self.pushButton_5_logi.setStyleSheet(f'background-color:{kolor_aktiv_kno}')
            self.pushButton_5_logi.clicked.connect(lambda: knopka_izmen_sloi_2(4))

            if SLOI_2 == 1:
                self.label_1 = QtWidgets.QLabel(self.centralwidget)
                self.label_1.setGeometry(QtCore.QRect(50, 100, 1000, 250))
                self.label_1.setFont(font_3)

                self.label_2 = QtWidgets.QLabel(self.centralwidget)
                self.label_2.setGeometry(QtCore.QRect(50, 300, 1000, 250))
                self.label_2.setFont(font_3)

                self.label_3 = QtWidgets.QLabel(self.centralwidget)
                self.label_3.setGeometry(QtCore.QRect(50, 500, 1000, 250))
                self.label_3.setFont(font_3)

            if SLOI_2 == 2:
                self.label_nazv = QtWidgets.QLabel(self.centralwidget)
                self.label_nazv.setGeometry(QtCore.QRect(560, 200, 500, 50))
                self.label_nazv.setFont(font_6)

                self.label_opi = QtWidgets.QLabel(self.centralwidget)
                self.label_opi.setGeometry(QtCore.QRect(610, 230, 540, 350))
                self.label_opi.setFont(font_3)

            if SLOI_2 == 3:
                self.label_nazv = QtWidgets.QLabel(self.centralwidget)
                self.label_nazv.setGeometry(QtCore.QRect(280, 200, 430, 50))
                self.label_nazv.setFont(font_6)

                self.label_sostoit = QtWidgets.QLabel(self.centralwidget)
                self.label_sostoit.setGeometry(QtCore.QRect(280, 270, 380, 50))
                self.label_sostoit.setFont(font_1)

                self.label_opi = QtWidgets.QLabel(self.centralwidget)
                self.label_opi.setGeometry(QtCore.QRect(730, 320, 500, 400))
                self.label_opi.setFont(font_3)

                l = 1
                for i in baza_inf_blokov:
                    if l == SLAID:
                        f1 = str(i)
                    l += 1
                y = 0
                self.spisok_d = []
                if len(baza_blokov) != 0:
                    for j in baza_blokov[f1]:
                        self.label_d= QtWidgets.QLabel(self.centralwidget)
                        self.label_d.setGeometry(QtCore.QRect(310, 320 + 40 * y, 320, 40))
                        self.label_d.setFont(font_1)
                        self.spisok_d.append([self.label_d, j])
                        y += 1


            if SLOI_2 == 4:
                if len(logi) > 10:
                    spisok_log = logi[(SLAID-1)*10: SLAID*10]
                else:
                    spisok_log = logi
                y = 0
                self.spisok_log_2 = []
                for i in spisok_log:
                    self.label_log = QtWidgets.QLabel(self.centralwidget)
                    self.label_log.setGeometry(QtCore.QRect(200, 150 + 60 * y, 1000, 60))
                    self.label_log.setFont(font_7)
                    self.spisok_log_2.append([self.label_log, i])
                    y += 1
###################################################################################################################

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1250, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "запас"))
        self.pushButton_2.setText(_translate("MainWindow", "приход"))
        self.pushButton_3.setText(_translate("MainWindow", "расход"))
        self.pushButton_4.setText(_translate("MainWindow", "настройка"))
        self.pushButton_5.setText(_translate("MainWindow", "информация"))
        self.label_1.setText(_translate("MainWindow", 'разработчик: Тарасов Д.Л.'))
        tema = ["запас", "приход", "расход", "настройка", "информация"]
        self.label.setText(_translate("MainWindow", tema[SLOI-1]))

        if SLOI == 1:
            for l in self.spisok_b_z:
                l[0].setText(_translate("MainWindow", f'{str(l[1])}      {str(baza_zapas[l[1]])}шт.'))

        if SLOI == 2:
            for l in self.spisok_izm_d:
                l[0].setText(_translate("MainWindow", f'{str(l[1])}'))
            self.pushButton_pri.setText(_translate("MainWindow", "добавить"))

        if SLOI == 3:
            self.pushButton_rash_d.setText(_translate("MainWindow", "расход деталей"))
            self.pushButton_rash_bl.setText(_translate("MainWindow", "расход блоков"))
            if SLOI_2 == 1:
                for l in self.spisok_izm_d:
                    l[0].setText(_translate("MainWindow", f'{str(l[1])}'))
                self.pushButton_trat_d.setText(_translate("MainWindow", "списать"))
            if SLOI_2 == 2:
                if SLOI_3 == 1:
                    for l in self.spisok_rash_blo:
                        l[0].setText(_translate("MainWindow", f'{str(l[1])}'))
                    self.label_teh_stroka.setText(_translate("MainWindow", ohi))
                    self.pushButton_3_2_blo_dez_izm.setText(_translate("MainWindow", "черновик"))
                    self.pushButton_3_2_vihit_blocov.setText(_translate("MainWindow", "списать"))

                if SLOI_3 == 2:
                    self.label_3_2_1_zagolovok.setText(_translate("MainWindow", 'нужно (в наличии):'))
                    for l in self.spisok_smeta_0:
                        l[0].setText(_translate("MainWindow",
                                                f'{str(l[1])}      {str(smeta_0[l[1]])}шт.({str(baza_zapas[l[1]])})'))
                    self.pushButton_3_2_1_odratno.setText(_translate("MainWindow", "обратно"))
                    self.pushButton_3_2_1_nehvat.setText(_translate("MainWindow", "список недостающего"))

                if SLOI_3 == 3:
                    self.label_3_2_1_zagolovok.setText(_translate("MainWindow", 'не хватает:'))
                    for l in self.spisok_smeta_0:
                        l[0].setText(_translate("MainWindow", f'{str(l[1])}      {str(smeta_1[l[1]])}шт.'))
                    self.pushButton_3_2_2_odratno.setText(_translate("MainWindow", "обратно"))
                    if len(smeta_1) != 0:
                        self.pushButton_3_2_2_txt.setText(_translate("MainWindow", "в текстовый документ"))

        if SLOI == 4:
            self.pushButton_4_blo.setText(_translate("MainWindow", "добавить блок"))
            self.pushButton_4_det.setText(_translate("MainWindow", "добавить деталь"))
            self.pushButton_4_del_det.setText(_translate("MainWindow", "удалить деталь"))
            self.pushButton_4_del_blo.setText(_translate("MainWindow", "удалить блок"))
            if SLOI_2 == 1:
                self.label_nazv.setText(_translate("MainWindow", 'название:'))
                self.label_opi.setText(_translate("MainWindow", 'описание:'))
                self.label_skolko.setText(_translate("MainWindow", 'сколько:'))
                self.pushButton_4_2_dobav_det.setText(_translate("MainWindow", 'добавить'))
                self.label_teh_stroka.setText(_translate("MainWindow", ohi))

            if SLOI_2 == 2:
                self.pushButton_del_det.setText(_translate("MainWindow", 'удалить'))
                self.label_primahanie.setText(
                    _translate("MainWindow", 'детали задействованные в блоках, удалить нельзя.'))
                for l in self.spisok_del_det:
                    l[0].setText(_translate("MainWindow", str(l[1])))

            if SLOI_2 == 3:
                self.label_nazv.setText(_translate("MainWindow", 'название:'))
                self.label_opi.setText(_translate("MainWindow", 'описание:'))
                self.label_sost_iz.setText(_translate("MainWindow", 'состоит из:'))
                self.pushButton_4_3_dobav_blo.setText(_translate("MainWindow", 'добавить'))
                self.label_teh_stroka.setText(_translate("MainWindow", ohi))
                for l in self.spisok_nov_blok:
                    l[0].setText(_translate("MainWindow", f'{str(l[1])}'))

            if SLOI_2 == 4:
                self.pushButton_del_blo.setText(_translate("MainWindow", 'удалить'))
                for l in self.spisok_del_blo:
                    l[0].setText(_translate("MainWindow", str(l[1])))

        if SLOI == 5:
            self.pushButton_5_inf_prog.setText(_translate("MainWindow", 'о программе'))
            self.pushButton_5_inf_det.setText(_translate("MainWindow", 'описание деталей'))
            self.pushButton_5_inf_blo.setText(_translate("MainWindow", 'описание блоков'))
            self.pushButton_5_logi.setText(_translate("MainWindow", 'логи'))

            if SLOI_2 == 1:
                self.label_1.setText(_translate("MainWindow", 'данная программа предназначена для оптимизации учёта.'))
                self.label_2.setText(_translate("MainWindow", 'расход деталей возможет как поштучно, так и блоками\изделиями исходя\n'
                                                              'из состава блоков\изделий.\n'
                                                              'добавление новых деталей и блоков возможно через настройки.'))
                self.label_3.setText(_translate("MainWindow", 'формат названий  и описаний (деталей и блоков) имеет следующие ограничения:\n'
                                                              'названия:   одна строка до 16 знаков,\n'
                                                              'описание деталей:  10 строк по 45 знаков,\n'
                                                              'описание блоков: 9 строк по 19 знаков. '))

            if SLOI_2 == 2 or SLOI_2 == 3 or SLOI_2 == 4:
                if SLAID > 1:
                    self.pushButton_5_sla_obr.setText(_translate("MainWindow", '<<<'))
                if (SLOI_2 == 2 and SLAID < len(baza_inf)) or (SLOI_2 == 3 and SLAID < len(baza_inf_blokov)) or \
                        (SLOI_2 == 4 and SLAID < len(logi) / 10):
                    self.pushButton_5_sla_tyda.setText(_translate("MainWindow", '>>>'))

            if SLOI_2 == 2:
                l = 1
                f1 = ''
                f2 = ''
                for i in baza_inf:

                    if l == SLAID:
                        f1 = str(i)
                        f2 = str(baza_inf[i])
                    l += 1
                self.label_nazv.setText(_translate("MainWindow", f1))
                self.label_opi.setText(_translate("MainWindow", f2))

            if SLOI_2 == 3:
                l = 1
                f1 = ''
                f2 = ''
                for i in baza_inf_blokov:
                    if l == SLAID:
                        f1 = str(i)
                        f2 = str(baza_inf_blokov[i])
                    l += 1
                self.label_nazv.setText(_translate("MainWindow", f1))
                self.label_sostoit.setText(_translate("MainWindow", 'состоит из:'))
                self.label_opi.setText(_translate("MainWindow", f2))
                for d in self.spisok_d:
                    d[0].setText(_translate("MainWindow", f'{d[1]}  {str(baza_blokov[f1][d[1]])}шт'))

            if SLOI_2 == 4:
                for i in self.spisok_log_2:
                    i[0].setText(_translate("MainWindow", str(i[1])))

def formatir_text(a, st=1, zn=16):
    a1 = ''
    s = 1
    z = 0
    for i in a:
        if i != '\n' and z != zn:
            a1 += i
            z += 1
        elif i != '\n' and z == zn and s < st:
            a1 += i + '\n'
            s += 1
            z = 1
        elif i == '\n' and s < st:
            a1 += i
            s += 1
            z = 1
    return a1

def log(a, b):
    global logi
    b1 = ''
    k = 0
    for i, l in enumerate(b):
        b1 += l
        if (i+1) % 90 == 0:
            k = 1
        if k == 1 and (l == ']' or l == ')' or l == ' '):
            b1 += '\n' + ' ' * 45
            k = 0
    if len(b) > 0:
        c = datetime.now()
        d = f'{a}.({str(c)[0:19]}): {b1}'
        logi.append(d)
        save(0)

def error(a):
    global ohi
    ohi = a

def save(a):
    if a == 0:
        i = ['log', logi]
    elif a == 1:
        i = ['baza_zapas', baza_zapas]
    elif a == 2:
        i = ['baza_inf', baza_inf]
    elif a == 3:
        i = ['baza_blokov', baza_blokov]
    elif a == 4:
        i = ['baza_inf_blokov', baza_inf_blokov]

    with open(i[0] + '.bin', 'wb') as l:
        dump(i[1], l)

def knopka_izmen_sloi(a):
    'функция для кнопок изменения слоёв'
    global SLOI, SLOI_2, SLOI_3, SLAID
    SLOI = a
    SLOI_2, SLOI_3, SLAID = 1, 1, 1
    error('')
    ui.setupUi(MainWindow)

def knopka_izmen_sloi_2(a):
    'функция для кнопок изменения слоёв'
    global SLOI_2, SLOI_3, SLAID
    SLOI_2 = a
    SLOI_3, SLAID = 1, 1
    error('')
    ui.setupUi(MainWindow)

def knopka_izmen_sloi_3(a):
    'функция для кнопок изменения слоёв'
    global SLOI_3
    SLOI_3 = a
    error('')
    ui.setupUi(MainWindow)

def popolnenie_zapacov(a):
    'внесение поступлений и расходов в базу'
    global baza_zapas
    L = ''
    for i in ui.spisok_izm_d:
        if i[2].value() != 0:
            baza_zapas[i[1]] += i[2].value()*a
            L += f'[{i[1]}_{str(i[2].value())}] '
    if a == 1:
        log('прих', L)
    elif a == -1:
        log('расх', L)
    save(1)
    ui.setupUi(MainWindow)

def kno_3_2_blo_dez_izm():
    global smeta_0, SLOI_3
    smeta_0 = {}
    for i in ui.spisok_rash_blo:
        if i[2].value() != 0:
            for l in range(i[2].value()):
                for j in baza_blokov[i[1]]:
                    if j in smeta_0:
                        smeta_0[j] += baza_blokov[i[1]][j]
                    else:
                        smeta_0.setdefault(j, baza_blokov[i[1]][j])
    SLOI_3 = 2
    ui.setupUi(MainWindow)

def kno_rashod_blok():
    global baza_zapas
    b_z = baza_zapas
    L = ''
    try:
        for i in ui.spisok_rash_blo:
            if i[2].value() != 0:
                for j in baza_blokov[i[1]]:
                    if b_z[j] - baza_blokov[i[1]][j]*i[2].value() >= 0:
                        b_z[j] -= baza_blokov[i[1]][j]*i[2].value()
                    else:
                        error('увы....  недостаточно деталей')
                        raise ValueError('1')
                L += f'[{i[1]}_{str(i[2].value())}]'
        baza_zapas = b_z
        log('расх._бл', L)
        error('готово')
    except:
        pass
    save(1)
    ui.setupUi(MainWindow)

def kno_3_2_nedostayhee():
    global smeta_1, SLOI_3
    smeta_1 = {}
    for i in smeta_0:
        if smeta_0[i] > baza_zapas[i]:
            smeta_1.setdefault(i, smeta_0[i] - baza_zapas[i])
    SLOI_3 = 3
    ui.setupUi(MainWindow)

def kno_xtx(a):
    global SLOI_3
    stroka = ''
    for i in a:
        stroka += str(i) + '   ' + str(a[i]) + ' шт.\n'
    try:
        f = open('надо.txt', 'w', encoding='utf-8')
        f.write(stroka)
        f.close()
    except:
        pass
    SLOI_3 = 0
    error('готово.')
    ui.setupUi(MainWindow)

def knopka_dobavl_det():
    global baza_zapas, baza_inf
    tex = formatir_text(ui.textEdit.toPlainText())

    if len(tex) == 0:
        error('увы....   нет названия!')
    else:
        if tex in baza_zapas:
            baza_zapas[tex] += ui.spinBox_skolko.value()
            if ui.spinBox_skolko.value() != 0:
                log('прих', f'[{str(tex)}_{str(ui.spinBox_skolko.value())}]')
            error('добавлено')
        else:
            baza_zapas.setdefault(tex, ui.spinBox_skolko.value())
            baza_inf.setdefault(tex, formatir_text(ui.plainTextEdit.toPlainText(), st=10, zn=45))
            log('нов._дет', tex)
            if ui.spinBox_skolko.value() != 0:
                log('прих', f'[{str(tex)}_{str(ui.spinBox_skolko.value())}]')
            error('готово.')
    save(1)
    save(2)
    ui.setupUi(MainWindow)

def proverka_isp_det(a):
    'проверка задействованности детали в блоках'
    for i in baza_blokov:
        if a in baza_blokov[i]:
            return True
    return False

def knopka_del_det():
    global baza_zapas, baza_inf
    L = ''
    for i in ui.spisok_del_det:
        if i[2].isChecked() == True:
            L += f'{i[1]}({str(baza_zapas[i[1]])}) '
            del baza_zapas[i[1]]
            del baza_inf[i[1]]
    log('удал', L)
    save(1)
    save(2)
    ui.setupUi(MainWindow)

def knopka_del_blo():
    global baza_blokov, baza_inf_blokov
    L = ''
    for i in ui.spisok_del_blo:
        if i[2].isChecked() == True:
            L += f'{i[1]}   '
            del baza_blokov[i[1]]
            del baza_inf_blokov[i[1]]
    log('удал._бл', L)
    save(3)
    save(4)
    ui.setupUi(MainWindow)

def knopka_dobavl_blo():
    global baza_blokov, baza_inf_blokov
    tex = formatir_text(ui.textEdit.toPlainText())
    b = {}
    L = '('
    if len(tex) == 0:
        error('увы....   нет названия!')
    else:
        for i in ui.spisok_nov_blok:
            if i[2].value() != 0:
                b.setdefault(i[1], i[2].value())
                L += f'{i[1]}_{str(i[2].value())} '
    if len(b) > 0:
        baza_blokov.setdefault(tex, b)
        baza_inf_blokov.setdefault(tex, formatir_text(ui.plainTextEdit.toPlainText(), st=9, zn=19))
        log('нов._бл', f'{tex} {L})')
        error('готово.')
    else:
        error('увы.... в составе блока нет деталей.')
    save(3)
    save(4)
    ui.setupUi(MainWindow)

def knopka_sla(a):
    global SLAID
    SLAID += a
    ui.setupUi(MainWindow)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
