from datetime import datetime
import sys
from typing_extensions import Self
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate, QRandomGenerator, QDateTime
from PyQt5.QtWidgets import QDialog, QApplication
from Ui_ui_main import *
import pymysql
import string
import random
from face_save import *
from face_train import *
from auto_what import *

global_user_id = "1"
global_videocam_bool = True

ex = Ui_MainWindow()


#################################################
#        Database Conn. & Cursor Creation       #
#################################################

connection = pymysql.connect(host="localhost", user="smart_society", password="smart_society", database="smart_society")
cursors = connection.cursor()
c1 = connection.cursor()
c2 = connection.cursor()

print("Connected")

#################################################

#################################################
#         PAGES LINKING SUB FUNCTIONS           #
#################################################

def home():
    ex.stackedWidget.setCurrentIndex(0)
def manage_society():
    ex.stackedWidget.setCurrentIndex(1)

def whatsapp_notice():
    ex.stackedWidget.setCurrentIndex(2)

def complaint_forum():
    ex.stackedWidget.setCurrentIndex(3)

def about():
    ex.stackedWidget.setCurrentIndex(4)

def owner():
    ex.stackedWidget_home.setCurrentIndex(0)
    owner_fetch_combo()

def staff():
    ex.stackedWidget_home.setCurrentIndex(1)
    staff_fetch_combo()

def member():
    ex.stackedWidget_home.setCurrentIndex(2)
    member_fetch_combo(global_user_id)

def vehicle():
    ex.stackedWidget_home.setCurrentIndex(3)
    vehicle_fetch_combo(global_user_id)

#################################################
#            MAIN LINKING FUNCTIONS             #
#################################################

def connect_pages():
    ex.bn_home.clicked.connect(home)
    ex.bn_manage_society.clicked.connect(manage_society)
    ex.bn_whatsapp_notice.clicked.connect(whatsapp_notice)
    ex.bn_complaint_forum.clicked.connect(complaint_forum)
    ex.bn_about.clicked.connect(about)

    ex.sub_btn_owner.clicked.connect(owner)
    ex.sub_btn_staff.clicked.connect(staff)
    ex.sub_btn_member.clicked.connect(member)
    ex.sub_btn_vehicle.clicked.connect(vehicle)
    
##################################################
  
##################################################
#                RESET FUNCTIONS                 # 
##################################################

def owner_reset():
    ex.o_curr_owners_combo.setCurrentIndex(0)
    ex.o_owner_id_txt.setText(owner_getmaxid())
    ex.o_owner_name_txt.setText("")
    ex.o_male_radio.setChecked(False)
    ex.o_female_radio.setChecked(False)
    ex.o_marital_combo.setCurrentIndex(0)
    ex.o_phno_txt.setText("")
    ex.o_address_txt.setPlainText("")
    ex.o_status_lbl.setText("Status: Not Registered")
    ex.o_wing_combo.setCurrentIndex(0)
    ex.o_flat_no_combo.setCurrentIndex(0)
    ex.o_uname_txt.setText("")
    ex.o_pwd_txt.setText("")
    ex.o_save_btn.setText("SAVE")
    ex.o_save_btn.setEnabled(True)
    ex.o_delete_btn.setEnabled(False)
    global_videocam_bool = True

def staff_reset():
    # print(staff_grab())
    ex.s_curr_staff_combo.setCurrentIndex(0)
    ex.s_staff_id_txt.setText(staff_getmaxid())
    ex.s_staff_name_txt.setText("")
    ex.s_male_radio.setChecked(False)
    ex.s_female_radio.setChecked(False)
    ex.s_marital_combo.setCurrentIndex(0)
    ex.s_phno_txt.setText("")
    ex.s_address_txt.setPlainText("")
    ex.o_status_lbl.setText("Status: Not Registered")
    ex.s_position_combo.setCurrentIndex(0)    
    ex.s_save_btn.setText("SAVE")
    ex.s_save_btn.setEnabled(True)
    ex.s_delete_btn.setEnabled(False)
    global_videocam_bool = True

def member_reset():
    # print(member_grab())
    ex.m_curr_mem_combo.setCurrentIndex(0)
    ex.m_member_id_txt.setText(member_getmaxid())
    ex.m_member_name_txt.setText("")
    ex.m_male_radio.setChecked(False)
    ex.m_female_radio.setChecked(False)
    ex.m_relation_combo.setCurrentIndex(0)
    ex.m_email_txt.setText("")
    ex.m_ph_txt.setText("")
    ex.m_status_lbl.setText("Status: Not Registered")
    ex.m_save_btn.setText("SAVE")
    ex.m_save_btn.setEnabled(True)
    ex.m_delete_btn.setEnabled(False)
    global_videocam_bool = True

def vehicle_reset():
    # print(vehicle_grab())
    ex.v_reg_no_api_btn.setText("")
    ex.v_curr_veh_combo.setCurrentIndex(0)
    ex.v_owner_name_txt.setText("")
    ex.v_model_txt.setText("")
    ex.v_rto_name_txt.setText("")
    ex.v_reg_date_txt.setDateTime(QDateTime.currentDateTime())
    ex.v_reg_no_txt.setText("")
    ex.v_save_btn.setText("SAVE")
    ex.v_save_btn.setEnabled(True)
    ex.v_delete_btn.setEnabled(False)

def wing_reset():
    ex.w_wing_name_txt.setText("")
    ex.w_tot_flats_txt.setText("")

def notice_reset():
    ex.wh_msg_id_txt.setText(notice_getmaxid())
    ex.wh_msg_txt.setPlainText("")

##################################################


##################################################
#                ENABLE FUNCTION                 # 
##################################################

def owner_enable():
    ex.o_owner_id_txt.setEnabled(True)
    ex.o_owner_name_txt.setEnabled(True)
    ex.o_male_radio.setEnabled(True)
    ex.o_female_radio.setEnabled(True)
    ex.o_marital_combo.setEnabled(True)
    ex.o_phno_txt.setEnabled(True)
    ex.o_address_txt.setEnabled(True)
    ex.o_wing_combo.setEnabled(True)
    ex.o_flat_no_combo.setEnabled(True)
    ex.o_uname_txt.setEnabled(True)
    ex.o_pwd_txt.setEnabled(True)
    ex.o_save_btn.setEnabled(True)
    ex.o_delete_btn.setEnabled(True)

def staff_enable():
    ex.s_staff_id_txt.setEnabled(True)
    ex.s_staff_name_txt.setEnabled(True)
    ex.s_male_radio.setEnabled(True)
    ex.s_female_radio.setEnabled(True)
    ex.s_marital_combo.setEnabled(True)
    ex.s_phno_txt.setEnabled(True)
    ex.s_address_txt.setEnabled(True)
    ex.s_position_combo.setEnabled(True)
    ex.s_save_btn.setEnabled(True)
    ex.s_delete_btn.setEnabled(True)


def member_enable():
    ex.m_member_id_txt.setEnabled(True)
    ex.m_member_name_txt.setEnabled(True)
    ex.m_male_radio.setEnabled(True)
    ex.m_female_radio.setEnabled(True)
    ex.m_relation_combo.setEnabled(True)
    ex.m_email_txt.setEnabled(True)
    ex.m_ph_txt.setEnabled(True)
    ex.m_save_btn.setEnabled(True)
    ex.m_delete_btn.setEnabled(True)
    
def vehicle_enable():
    ex.v_owner_name_txt.setEnabled(True)
    ex.v_model_txt.setEnabled(True)
    ex.v_rto_name_txt.setEnabled(True)
    ex.v_reg_date_txt.setEnabled(True)
    ex.v_reg_no_txt.setEnabled(True)
    ex.v_save_btn.setEnabled(True)
    ex.v_delete_btn.setEnabled(True)

##################################################


##################################################
#                DISABLE FUNCTIONS               # 
##################################################

def owner_disable():
    ex.o_owner_id_txt.setEnabled(False)
    ex.o_owner_name_txt.setEnabled(False)
    ex.o_male_radio.setEnabled(False)
    ex.o_female_radio.setEnabled(False)
    ex.o_marital_combo.setEnabled(False)
    ex.o_phno_txt.setEnabled(False)
    ex.o_address_txt.setEnabled(False)
    ex.o_wing_combo.setEnabled(False)
    ex.o_flat_no_combo.setEnabled(False)
    ex.o_uname_txt.setEnabled(False)
    ex.o_pwd_txt.setEnabled(False)
    ex.o_status_lbl.setText("Status: Not Registered")
    ex.o_save_btn.setText("UPDATE")
    ex.o_save_btn.setEnabled(False)

def staff_disable():
    ex.s_staff_id_txt.setEnabled(False)
    ex.s_staff_name_txt.setEnabled(False)
    ex.s_male_radio.setEnabled(False)
    ex.s_female_radio.setEnabled(False)
    ex.s_marital_combo.setEnabled(False)
    ex.s_phno_txt.setEnabled(False)
    ex.s_address_txt.setEnabled(False)
    ex.s_position_combo.setEnabled(False)
    ex.s_status_lbl.setText("Status: Registered")
    ex.s_save_btn.setText("UPDATE")
    ex.s_save_btn.setEnabled(False)

def member_disable():
    ex.m_member_id_txt.setEnabled(False)
    ex.m_member_name_txt.setEnabled(False)
    ex.m_male_radio.setEnabled(False)
    ex.m_female_radio.setEnabled(False)
    ex.m_relation_combo.setEnabled(False)
    ex.m_email_txt.setEnabled(False)
    ex.m_ph_txt.setEnabled(False)
    ex.m_status_lbl.setText("Status: Not Registered")  
    ex.m_save_btn.setText("UPDATE")
    ex.m_save_btn.setEnabled(False)

def vehicle_disable():
    ex.v_owner_name_txt.setEnabled(False)
    ex.v_model_txt.setEnabled(False)
    ex.v_rto_name_txt.setEnabled(False)
    ex.v_reg_date_txt.setEnabled(False)
    ex.v_reg_no_txt.setEnabled(False)
    ex.v_save_btn.setText("UPDATE")
    ex.v_save_btn.setEnabled(False)

##################################################

##################################################
#              GET MAX_ID FUNCTIONS              # 
##################################################

def owner_getmaxid():
    sql = "select max(o_id) from owner"
    c1.execute(sql)
    tmp = c1.fetchone()
    if tmp[0] == None:
        max_id = 1
    else:
        max_id = tmp[0] + 1

    return str(max_id)

def staff_getmaxid():
    sql = "select max(s_id) from staff"
    c1.execute(sql)
    tmp = c1.fetchone()
    if tmp[0] == None:
        max_id = 1
    else:
        max_id = tmp[0] + 1

    return str(max_id)

def member_getmaxid():
    sql = "select max(m_id) from member"
    c1.execute(sql)
    tmp = c1.fetchone()
    if tmp[0] == None:
        max_id = 1
    else:
        max_id = tmp[0] + 1

    return str(max_id)

def vehicle_getmaxid():
    sql = "select max(v_id) from vehicle"
    c1.execute(sql)
    tmp = c1.fetchone()
    if tmp[0] == None:
        max_id = 1
    else:
        max_id = tmp[0] + 1

    return str(max_id)

def wing_getmaxid():
    sql = "select max(w_id) from wings"
    c1.execute(sql)
    tmp = c1.fetchone()
    if tmp[0] == None:
        max_id = 1
    else:
        max_id = tmp[0] + 1

    return str(max_id)

def flat_getmaxid():
    sql = "select max(f_id) from flats"
    c1.execute(sql)
    tmp = c1.fetchone()
    if tmp[0] == None:
        max_id = 1
    else:
        max_id = tmp[0] + 1

    return str(max_id)


def notice_getmaxid():
    sql = "select max(n_id) from notice"
    c1.execute(sql)
    tmp = c1.fetchone()
    if tmp[0] == None:
        max_id = 1
    else:
        max_id = tmp[0] + 1

    return str(max_id)

def reg_getmaxid():
    sql = "select max(reg_no) from reg"
    c1.execute(sql)
    tmp = c1.fetchone()
    if tmp[0] == None:
        max_id = 1
    else:
        max_id = tmp[0] + 1

    return str(max_id)
    
##################################################


##################################################
#             StartVideoCam FUNCTIONS            # 
##################################################

def owner_StartVideoCam():
    if global_videocam_bool == False:
        return
    reg_no = reg_getmaxid()
    save_images(reg_no)
    train_dataset()

def staff_StartVideoCam(s_id):
    if global_videocam_bool == False:
        return
    reg_no = reg_getmaxid()
    save_images(reg_no)
    train_dataset()

def member_StartVideoCam(m_id):
    if global_videocam_bool == False:
        return
    reg_no = reg_getmaxid()
    save_images(reg_no)
    train_dataset()

##################################################

##################################################
#                 DELETE FUNCTIONS               # 
##################################################

def owner_delete():
    id = ex.o_owner_id_txt.text()
    sql = "delete from owner where o_id=" + id
    try:
        c1.execute(sql)
        connection.commit()
    except Exception as E:
        print(E)
    print("Record Deleted from OWNER")
    owner_reset()
    owner_fetch_combo()

def staff_delete():
    id = ex.s_staff_id_txt.text()
    sql = "delete from staff where s_id=" + id    
    try:
        c1.execute(sql)
        connection.commit()
    except Exception as E:
        print(E)
    print("Record Deleted from STAFF")
    staff_reset()
    staff_fetch_combo()

def member_delete():
    id = ex.m_member_id_txt.text()
    sql = "delete from member where m_id=" + id
    try:
        c1.execute(sql)
        connection.commit()
    except Exception as E:
        print(E)
    print("Record Deleted from MEMBER")
    member_reset()
    member_fetch_combo()

def vehicle_delete():
    id = ex.v_reg_no_txt.text()
    sql = "delete from vehicle where v_id=" + id
    try:
        c1.execute(sql)
        connection.commit()
    except Exception as E:
        print(E)
    print("Record Deleted from VEHICLE")
    vehicle_reset()
    vehicle_fetch_combo()

##################################################

##################################################
#            FETCH * DATA FUNCTIONS            # 
##################################################

def owner_fetch():
    name = ex.o_curr_owners_combo.currentText()
    sql = "select * from owner where o_name='" + name + "'"  
    try:
        c1.execute(sql)
    except Exception as E:
        print(E)
    row = c1.fetchone()    
    # print(row)
    return row

def staff_fetch():
    name = ex.s_curr_staff_combo.currentText()
    sql = "select * from staff where s_name='" + name + "'"  
    try:
        c1.execute(sql)
    except Exception as E:
        print(E)
    row = c1.fetchone()    
    
    return row

def member_fetch():
    name = ex.m_curr_mem_combo.currentText()
    sql = "select * from member where m_name='" + name + "'"  
    try:
        c1.execute(sql)
    except Exception as E:
        print(E)
    row = c1.fetchone()    
    
    return row

def vehicle_fetch():
    regno = ex.v_curr_veh_combo.currentText()
    sql = "select * from vehicle where v_reg_no='" + regno + "'"  
    try:
        c1.execute(sql)
    except Exception as E:
        print(E)
    row = c1.fetchone()    
    
    return row

##################################################

##################################################
#           LOAD COMBO DATA FUNCTIONS            # 
##################################################

def owner_fetch_combo():
    ex.o_curr_owners_combo.clear()
    ex.o_curr_owners_combo.addItem("")
    q1 = "select o_name from owner"
    c1.execute(q1)
    row = c1.fetchall()
    for x in row:
        ex.o_curr_owners_combo.addItem(x[0])

def staff_fetch_combo():
    ex.s_curr_staff_combo.clear()
    ex.s_curr_staff_combo.addItem("")
    q1 = "select s_name from staff"
    c1.execute(q1)
    row = c1.fetchall()
    for x in row:
        ex.s_curr_staff_combo.addItem(x[0])

def member_fetch_combo(o_id):
    ex.m_curr_mem_combo.clear()
    ex.m_curr_mem_combo.addItem("")
    q1 = "select m_name from member where o_id="+ o_id
    c1.execute(q1)
    row = c1.fetchall()
    for x in row:
        ex.m_curr_mem_combo.addItem(x[0])

def vehicle_fetch_combo(o_id):
    ex.v_curr_veh_combo.clear()
    ex.v_curr_veh_combo.addItem("")
    q1 = "select v_reg_no from vehicle where o_id="+ o_id
    c1.execute(q1)
    row = c1.fetchall()
    for x in row:
        ex.v_curr_veh_combo.addItem(x[0])

def wing_fetch_combo():
    ex.o_wing_combo.clear()
    ex.o_wing_combo.addItem("")
    q1 = "select w_name from wings"
    c1.execute(q1)
    row = c1.fetchall()
    for x in row:
        ex.o_wing_combo.addItem(x[0])

def flat_fetch_combo():
    ex.o_flat_no_combo.clear()
    ex.o_flat_no_combo.addItem("")
    q1 = "select f_name from flats"
    c1.execute(q1)
    row = c1.fetchall()
    for x in row:
        ex.o_flat_no_combo.addItem(x[0])
    
##################################################


##################################################
#             GRAB DATA FROM DATAFIELDS          # 
##################################################

def owner_grab():
    id = ex.o_owner_id_txt.text()
    name = ex.o_owner_name_txt.text()
    if(ex.o_male_radio.isChecked()):
        gender = ex.o_male_radio.text()
    else:
        gender = ex.o_female_radio.text()
    marital = ex.o_marital_combo.currentText()
    phno = ex.o_phno_txt.text()
    addr = ex.o_address_txt.toPlainText()
    wing = ex.o_wing_combo.currentText()
    flat = ex.o_flat_no_combo.currentText()
    
    q2 = "select f_id from flats where f_name=" + "'" + flat + "'"
    c1.execute(q2)
    tmp = c1.fetchone()
    flat_id = str(tmp[0])

    uname = ex.o_uname_txt.text()
    pwd = ex.o_pwd_txt.text()
    status = ex.o_status_lbl.text()
    max_reg_no = reg_getmaxid()

    return id, name, gender, marital, phno, addr, status, flat_id, uname, pwd, max_reg_no

def staff_grab():
    id = ex.s_staff_id_txt.text()
    name = ex.s_staff_name_txt.text()
    if(ex.s_male_radio.isChecked()):
        gender = ex.s_male_radio.text()
    else:
        gender = ex.s_female_radio.text()
    marital = ex.s_marital_combo.currentText()
    phno = ex.s_phno_txt.text()
    addr = ex.s_address_txt.toPlainText()
    status = ex.s_status_lbl.text()
    pos = ex.s_position_combo.currentText()    
    max_reg_no = reg_getmaxid()

    return id, name, gender, marital, phno, addr, status, pos, max_reg_no

def member_grab():
    id = ex.m_member_id_txt.text()
    name = ex.m_member_name_txt.text()
    if(ex.m_male_radio.isChecked()):
        gender = ex.m_male_radio.text()
    else:
        gender = ex.m_female_radio.text()
    relation = ex.m_relation_combo.currentText()
    email = ex.m_email_txt.text()
    phno = ex.m_ph_txt.text()
    status = ex.m_status_lbl.text()
    max_reg_no = reg_getmaxid()
    
    return id, name, gender, relation, email, phno, status, global_user_id, max_reg_no

def vehicle_grab():
    id = vehicle_getmaxid()
    name = ex.v_owner_name_txt.text()
    model = ex.v_model_txt.text()
    rto_name = ex.v_rto_name_txt.text()
    reg_date = ex.v_reg_date_txt.text()
    reg_no = ex.v_reg_no_txt.text()    
    
    return id, name,model, rto_name, reg_date, reg_no, global_user_id

def wing_grab():    
    q1 = "select max(w_id) from wings"
    c1.execute(q1)
    tmp = c1.fetchone()
    if tmp[0] == None:
        max_w_id = 1
    else:
        max_w_id = tmp[0] + 1
    
    wing_name = ex.w_wing_name_txt.text()
    tot_flats = ex.w_tot_flats_txt.text()
    
    return max_w_id, wing_name, tot_flats

def notice_grab():    
    id = ex.wh_msg_id_txt.text()
    notice_msg = ex.w_wing_name_txt.text()
    timestamp = ex.w_tot_flats_txt.text()
    
    return id, notice_msg, timestamp
        
##################################################

##################################################
#             SET DATA FROM DATAFIELDS          # 
##################################################

def owner_set():
    row = owner_fetch()    
    if row == None:
        owner_reset()
        return
    id = ex.o_owner_id_txt.setText(str(row[0]))
    name = ex.o_owner_name_txt.setText(str(row[1]))
    if(row[2] == "Male"):
        ex.o_male_radio.setChecked(True)
    else:
        ex.o_female_radio.setChecked(True)
    marital = ex.o_marital_combo.setCurrentText(str(row[3]))
    phno = ex.o_phno_txt.setText(str(row[4]))
    addr = ex.o_address_txt.setPlainText(str(row[5]))
    status = ex.o_status_lbl.setText(str(row[6]))
    uname = ex.o_uname_txt.setText(str(row[8]))
    pwd = ex.o_pwd_txt.setText(str(row[9]))
    q2 = "SELECT wings.w_name,flats.f_name FROM wings,flats WHERE flats.w_id = wings.w_id and flats.f_id=" + str(row[7])
    try:
        c1.execute(q2)
    except Exception as E:
        print(E)
    tmp = c1.fetchone()
    wing = ex.o_wing_combo.setCurrentText(tmp[0])
    flat = ex.o_flat_no_combo.setCurrentText(tmp[1])  
    owner_disable()
    ex.o_delete_btn.setEnabled(True)
    global_videocam_bool = False

def staff_set():
    row = staff_fetch()    
    if row == None:
        staff_reset()
        return
    id = ex.s_staff_id_txt.setText(str(row[0]))
    name = ex.s_staff_name_txt.setText(str(row[1]))
    if(row[2] == "Male"):
        ex.s_male_radio.setChecked(True)
    else:
        ex.s_female_radio.setChecked(True)
    marital = ex.s_marital_combo.setCurrentText(str(row[3]))
    phno = ex.s_phno_txt.setText(str(row[4]))
    addr = ex.s_address_txt.setPlainText(str(row[5]))
    status = ex.s_status_lbl.setText(str(row[6]))
    pos = ex.s_position_combo.setCurrentText(str(row[7]))
    staff_disable()
    ex.s_delete_btn.setEnabled(True)
    global_videocam_bool = False

def member_set():
    row = member_fetch()
    if row == None:
        member_reset()
        return
    id = ex.m_member_id_txt.setText(str(row[0]))
    name = ex.m_member_name_txt.setText(str(row[1]))
    if(row[2] == "Male"):
        ex.m_male_radio.setChecked(True)
    else:
        ex.m_female_radio.setChecked(True)
    relation = ex.m_relation_combo.setCurrentText(str(row[3]))
    email = ex.m_email_txt.setText(str(row[4]))
    phno = ex.m_ph_txt.setText(str(row[5]))
    status = ex.m_status_lbl.setText(str(row[6]))
    member_disable()
    ex.m_delete_btn.setEnabled(True)
    global_videocam_bool = False
    

def vehicle_set():
    row = vehicle_fetch()
    if row == None:
        vehicle_reset()
        return
    id = vehicle_getmaxid()
    name = ex.v_owner_name_txt.setText(str(row[1]))
    model = ex.v_model_txt.setText(str(row[2]))
    rto_name = ex.v_rto_name_txt.setText(str(row[3]))
    tmp = str(row[4])
    tmp = tmp.split("/")
    d = QDate(int(tmp[2]), int(tmp[1]), int(tmp[0]))
    reg_date = ex.v_reg_date_txt.setDate(d)
    reg_no = ex.v_reg_no_txt.setText(str(row[5]))
    vehicle_disable()
    ex.v_delete_btn.setEnabled(True)

def member_relation_set():
    ex.m_relation_combo.clear()
    ex.m_relation_combo.addItem("")
    ex.m_relation_combo.addItem("Mother")
    ex.m_relation_combo.addItem("Father")
    ex.m_relation_combo.addItem("Brother")
    ex.m_relation_combo.addItem("Sister")
    ex.m_relation_combo.addItem("Cousin")
    ex.m_relation_combo.addItem("Relative")
    ex.m_relation_combo.addItem("Guest")    
##################################################



##################################################
#        INSERT INTO DATABASE FUNCTIONS          # 
##################################################

def owner_insert():
    val = owner_grab()
    inc_reg_in_db(val[10])
    sql = "INSERT INTO owner VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql_update = """ UPDATE TABLE owner set 
                    o_id=%s and 
                    o_name=%s and 
                    o_gnd=%s and 
                    o_marrital_status=%s and 
                    o_phno=%s and 
                    o_addr=%s and 
                    o_reg_status=%s and 
                    f_id=%s and 
                    o_uname=%s and 
                    o_pwd=%s and 
                    reg_no=%s
                """
    try:
        c1.execute(sql, val)
        connection.commit()
    except Exception as E:
        print(E)
    print("Record Inserted in OWNER")
    owner_fetch_combo()
    owner_reset()

def staff_insert():
    val = staff_grab()
    inc_reg_in_db(val[8])
    sql = "INSERT INTO staff VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sql_update = """ UPDATE TABLE owner set                     
                    s_id=%s and 
                    s_name=%s and 
                    s_gnd=%s and 
                    s_marrital_status=%s and 
                    s_phno=%s and 
                    s_addr=%s and 
                    s_reg_status=%s and 
                    s_position=%s and 
                    reg_n=%s 
                """
    try:
        c1.execute(sql, val)
        connection.commit()
    except Exception as E:
        print(E)
    print("Record Inserted in STAFF")
    staff_fetch_combo()
    staff_reset()
    
def member_insert():
    val = member_grab()
    inc_reg_in_db(val[8])
    sql = "INSERT INTO member VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        c1.execute(sql, val)
        connection.commit()
    except Exception as E:
        print(E)
    print("Record Inserted in MEMBER")
    inc_reg_in_db(val[8])
    # member_fetch_combo()
    member_reset()

def vehicle_insert():
    val = vehicle_grab()
    sql = "INSERT INTO vehicle VALUES (%s, %s, %s, %s, %s, %s, %s)"
    try:
        c1.execute(sql, val)
        connection.commit()
    except Exception as E:
        print(E)
    print("Record Inserted in VEHICLE")
    # vehicle_fetch_combo()
    vehicle_reset()

def wing_insert():
    val = wing_grab()
    sql = "INSERT INTO wings VALUES (%s, %s, %s)"
    try:
        c1.execute(sql, val)
        connection.commit()
    except Exception as E:
        print(E)
    print("Record Inserted in WINGS")
    
    
    q1 = "select max(f_id) from flats"
    print(c1.execute(q1))
    tmp = c1.fetchone()
    if tmp[0] == None:
        max_f_id = 1
    else:
        max_f_id = int(tmp[0] + 1)

    # Insert N Flats 
    tmp = int(val[2])
    w_id = int(val[0])
    for x in range(tmp):
        print(x)
        sql = "INSERT INTO flats VALUES (%s, %s, %s, %s)"
        val = (max_f_id, x+1, w_id, "available")
        try:
            c1.execute(sql, val)
            connection.commit()
        except Exception as E:
            print(E)
        max_f_id = max_f_id + 1
    
    print("Record Inserted in FLATS")

    
def notice_insert():
    val = notice_grab()
    sql = "INSERT INTO notice VALUES (%s, %s, %s)"
    try:
        c1.execute(sql, val)
        connection.commit()
    except Exception as E:
        print(E)
    print("Record Inserted in OWNER")
    
    msg = str(val[1])
    no_list = ["999999999"]
    th = "9"
    tm = "7" 
    for x in no_list:
        send_notice(x, msg, th, tm)

def complaint_insert():
    # sql = "INSERT INTO complaint VALUES (%s, %s, %s, %s)"
    # val = (2, "W1", 20)
    # c1.execute(sql, val)
    # connection.commit()
    pass

def flats_insert():
    # sql = "INSERT INTO flats VALUES (%s, %s, %s, %s)"
    # val = (2, "W1", 20)
    # c1.execute(sql, val)
    # connection.commit()
    pass

##################################################

def generate_uname_pwd():
    try:
        wa = ex.o_owner_name_txt.text()
        no = random.randint(1, 500)
        tt = wa[0:4]+str(no)
        ex.o_uname_txt.setText(tt)

        S = 6
        ran = ''.join(random.choices(
            string.ascii_uppercase+string.digits, k=S))
        ss = str(ran)
        ex.o_pwd_txt.setText(ss)
    except:
        print("Error")

def inc_reg_in_db(val):
    sql = "INSERT INTO reg VALUES (%s)"
    try:
        c1.execute(sql, val)
        connection.commit()
    except Exception as E:
        print(E)

##################################################

def temp():
    a = 3
    b = "Krishna"
    if(a==3):
        pass
    else:
        print("HEYY")

    c = 20
    print("HEYY")

    return a, b, c


# wing = "W1"
# q2 = "select w_id from wings where w_name=" + "'" + wing + "'"
# max_staff_id = c1.execute(q2)
# print(max_staff_id)



##################################################
#             LINK FUNCTIONS TO BUTTONS          # 
##################################################

def reset_buttons_fun_linking():
    ex.o_reset_btn.clicked.connect(owner_reset)
    ex.s_reset_btn.clicked.connect(staff_reset)
    ex.m_reset_btn.clicked.connect(member_reset)
    ex.v_reset_btn.clicked.connect(vehicle_reset)
    ex.w_clear_btn.clicked.connect(wing_reset)
    ex.wh_clear_btn.clicked.connect(notice_reset)

def edit_buttons_fun_linking():
    ex.o_edit_btn.clicked.connect(owner_enable)
    ex.s_edit_btn.clicked.connect(staff_enable)
    ex.m_edit_btn.clicked.connect(member_enable)
    ex.v_edit_btn.clicked.connect(vehicle_enable)  

def save_buttons_fun_linking():
    ex.o_save_btn.clicked.connect(owner_insert)  
    ex.s_save_btn.clicked.connect(staff_insert)  
    ex.m_save_btn.clicked.connect(member_insert)  
    ex.v_save_btn.clicked.connect(vehicle_insert)  
    ex.w_add_btn.clicked.connect(wing_insert)
    ex.wh_send_btn.clicked.connect(notice_insert)

def delete_buttons_fun_linking():
    ex.o_delete_btn.clicked.connect(owner_delete)  
    ex.s_delete_btn.clicked.connect(staff_delete)  
    ex.m_delete_btn.clicked.connect(member_delete)  
    ex.v_delete_btn.clicked.connect(vehicle_delete)      

def start_videocam_btn_linking():
    ex.o_start_videocam_btn.clicked.connect(owner_StartVideoCam)
    ex.s_start_videocam_btn.clicked.connect(staff_StartVideoCam)
    ex.m_start_videocam_btn.clicked.connect(member_StartVideoCam)

def generate_btn_fun_linking():
    ex.o_generate_btn.clicked.connect(generate_uname_pwd)


##################################################


##################################################
#     COMBO ITEM CHANGED EVENT TO FILL DATA      # 
##################################################

def combo_change_event():    
    ex.o_curr_owners_combo.currentIndexChanged.connect(owner_set)
    ex.s_curr_staff_combo.currentIndexChanged.connect(staff_set)
    ex.m_curr_mem_combo.currentIndexChanged.connect(member_set)
    ex.v_curr_veh_combo.currentIndexChanged.connect(vehicle_set)

##################################################


##################################################
#        ****----- MAIN FUNCTION -----****       # 
##################################################

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)

    #CALL TO LINK PAGES
    connect_pages()

    #LINK BUTTONS
    reset_buttons_fun_linking()
    edit_buttons_fun_linking()
    save_buttons_fun_linking()
    delete_buttons_fun_linking()
    start_videocam_btn_linking()
    generate_btn_fun_linking()

    combo_change_event()
    
    #LOAD COMBOXES WITH RECORDS
    owner_fetch_combo()
    staff_fetch_combo()
    member_fetch_combo(str(1))
    vehicle_fetch_combo(str(1))
    wing_fetch_combo()
    flat_fetch_combo()
    member_relation_set()

    #CALLING RESET FUNCTIONS FOR MODULES
    owner_reset()
    staff_reset()
    member_reset()
    vehicle_reset()  

    #Combo Index Changed
    combo_change_event()

    w.show()
    sys.exit(app.exec_())

##################################################



