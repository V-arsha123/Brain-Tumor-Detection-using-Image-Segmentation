from django.shortcuts import render,redirect

# Create your views here.

from patients.models import UserRegistration,Feeback_Model,Post_MRIimageScan
from doctors.models import Add_Doctors_Details,Doc_MRI_ScanValue
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
import json
import os
import requests
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import tkinter.filedialog
import cv2
from skimage import exposure
import pickle
import sys
import imutils
from matplotlib import pyplot as plt
from skimage.measure import compare_ssim
from scipy import linalg
import numpy
import argparse
newfile = 'test15.txt'


def adminlogin(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username =='admin' and password == 'admin':


            return redirect('adddoctor')

    return render(request,'doctors/adminlogin.html')
def adddoctor(request):
    if request.method=="POST":
        doctorID = request.POST.get('doctorID')
        doctorname = request.POST.get('doctorname')
        doctoraddress = request.POST.get('doctoraddress')
        mobileno = request.POST.get('mobileno')
        emailid = request.POST.get('emailid')
        doctorage = request.POST.get('doctorage')
        doctorgender = request.POST.get('doctorgender')
        speciality = request.POST.get('speciality')


        Add_Doctors_Details.objects.create(doctorID=doctorID,doctorname=doctorname,doctoraddress=doctoraddress,mobileno=mobileno,emailid=emailid,doctorage=doctorage,doctorgender=doctorgender,speciality=speciality)



    return render(request,'doctors/adddoctor.html')




def patientsdetails(request):
    ted = UserRegistration.objects.all()
    return render(request, 'doctors/patientsdetails.html',{'objects':ted})

def patientsreviews(request):
    obj=Feeback_Model.objects.all()
    return render(request,'doctors/patientsreviews.html',{'objects':obj})

def viewdoctors(request):
    ted = Add_Doctors_Details.objects.all()
    return render(request, 'doctors/viewdoctors.html',{'objects':ted})

def viewMRIimage(request):
    ted = Post_MRIimageScan.objects.all()
    return render(request, 'doctors/viewMRIimage.html',{'objects':ted})


def tumourscan(request):
    def select_image1():
        # grab a reference to the image panels
        global panelA, panelB

        # open a file chooser dialog and allow the user to select an input
        # image
        path = filedialog.askopenfilename()

        # ensure a file path was selected
        if len(path) > 0:
            image = cv2.imread(path)
            picture = image
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            ted = gray
            ret, thresh1 = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
            (score, diff) = compare_ssim(ted, thresh1, full=True)
            diff = (diff * 255).astype("uint8")

            val1 = format(score)
            print("VALUE (1.0) IS ANALYSIS, :{}", "\n", val1)
            analysisva = val1

            thresh = cv2.threshold(diff, 0, 255,
                                   cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
            cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)

            for c in cnts:
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(ted, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.rectangle(thresh1, (x, y), (x + w, y + h), (0, 0, 255), 2)

            with open(newfile, "ab") as fi:
                # dump your data into the file
                pickle.dump(val1, fi)

            ret, thresh = cv2.threshold(thresh1, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
            dst = cv2.GaussianBlur(thresh1, (5, 5), cv2.BORDER_DEFAULT)
            edges = cv2.Canny(thresh1, 100, 200)
            kernel = np.ones((5, 5), np.uint8)
            img_erosion = cv2.erode(thresh1, kernel, iterations=1)
            edged = cv2.Canny(gray, 50, 100)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(image)
            edged = Image.fromarray(edged)
            image = ImageTk.PhotoImage(image)
            edged = ImageTk.PhotoImage(edged)
            cnts = cv2.findContours(img_erosion.copy(), cv2.RETR_EXTERNAL,
                                    cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            print("[INFO] {} unique contours found".format(len(cnts)))

            uniquecon = ("{}".format(len(cnts)))

            # loop over the contours
            for (i, c) in enumerate(cnts):
                # draw the contour
                ((x, y), _) = cv2.minEnclosingCircle(c)
                cv2.putText(picture, "#{}".format(i + 1), (int(x) - 10, int(y)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                Opj = cv2.drawContours(picture, [c], -1, (0, 255, 0), 2)

            cv2.imshow(' Brain MRI Grayscale', ted)
            cv2.imshow('Binary Threshold', thresh1)
            cv2.imshow('Image Segmentation', thresh)
            cv2.imshow("Gaussian Smoothing", numpy.hstack((thresh1, dst)))
            cv2.imshow('Erosion', img_erosion)
            cv2.imshow("Image Con", Opj)
            plt.subplot(121), plt.imshow(dst, cmap='gray')
            plt.title('Original Image'), plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(edges, cmap='gray')
            plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
            plt.show()
            cv2.waitKey(0)
            sys.stdout.close()

            Doc_MRI_ScanValue.objects.create( analysisvalue=analysisva, uniquecontors=uniquecon)

        if panelA is None or panelB is None:
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)
            panelB = Label(image=edged)
            panelB.image = edged
            panelB.pack(side="right", padx=10, pady=10)


        else:
            panelA.configure(image=image)
            panelB.configure(image=edged)
            panelA.image = imagepanelB.image = edged

    brainimg = request.POST.get('brainimg')
    # initialize the window toolkit along with the two image panels
    root = Tk()
    panelA = None
    panelB = None

    # create a button, then when pressed, will trigger a file chooser
    # dialog and allow the user to select an input image; then add the
    # button the GUI
    btn = Button(root, text="Select an Brain MRI image", command=select_image1)
    btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
    root.mainloop()

    Vobj = Doc_MRI_ScanValue.objects.all()
    return render(request, 'doctors/tumourscan.html', {'v': Vobj})


def adminlogout(request):
    return redirect('adminlogin')



