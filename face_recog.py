import numpy as np
import cv2
import pymysql
import datetime

def get_name_from_id(reg_no):
    connection = pymysql.connect(host="localhost", user="root", password="", database="smart_society")
    cursors = connection.cursor()
    c1 = connection.cursor()
    c2 = connection.cursor()
    c3 = connection.cursor()
    
    sql1 = "select o_name from owner where reg_no="+str(reg_no)
    sql2 = "select s_name from staff where reg_no="+str(reg_no)
    sql3 = "select m_name from member where reg_no="+str(reg_no)
    try:
        c1.execute(sql1)
        c2.execute(sql2)
        c3.execute(sql3)
    except Exception as E:
        print(E)

    tmp1 = c1.fetchone()
    tmp2 = c2.fetchone()
    tmp3 = c3.fetchone()
    
    if not tmp1 == None:
        name = tmp1[0]
    elif not tmp2 == None:
        name = tmp2[0]
    elif not tmp3 == None:
        name = tmp3[0]
    else:
        name = "Unknown"

    return str(name)
    
def add_entry_timestamp(reg_no):
    connection = pymysql.connect(host="localhost", user="root", password="", database="smart_society")
    cursors = connection.cursor()
    c1 = connection.cursor()
    timestamp = datetime.datetime.now()
    val = (reg_no, timestamp)
    sql = "insert into reg_entries values(%s, %s)"
    try:
        c1.execute(sql, val)
        connection.commit()
    except Exception as E:
        print(E)


def detect_faces():
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    cap = cv2.VideoCapture(0)
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read("FaceRecTrain/trainingdata.yml")
    id=0
    #font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while 1:
        stop_flooding = []
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.5, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            
            # cv2.putText(img,"Karan",(x,y+h),font,255,(255, 0, 0))
            name = get_name_from_id(id)
            cv2.putText(img,name+"-"+str(id), (x, y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 1, cv2.LINE_AA)
            
            avail = False
            for x in stop_flooding:
                if int(x) == int(id):
                    avail = True
                    print("HERE")
            if avail == False:
                add_entry_timestamp(id)
                stop_flooding.append(id)
            print(stop_flooding)
        
        cv2.imshow('img',img)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

detect_faces()