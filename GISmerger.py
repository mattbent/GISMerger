#!/usr/bin/python

########################################
# Author: Matthew Bent
# Project: GIS Merger
# Description: This program takes a folder full of plats
# and merges them together, asking for names
########################################
import Tkinter
from Tkinter import *
import tkMessageBox
import tkFileDialog
import tkSimpleDialog
from collections import defaultdict
from PyPDF2 import PdfFileReader, PdfFileMerger
import os

top = Tkinter.Tk()
top.geometry('{}x{}'.format(200, 200))
showDir = Tkinter.Entry(top)
destDir = Tkinter.Entry(top)
dirName = ""
theDict = defaultdict(list)

def resetCall():
    dirName = ""
    theDict = defaultdict(list)
    showDir.delete(0,'end')
    destDir.delete(0,'end')

def fileFind():
    root = Tkinter.Toplevel(top)
    currdir = os.getcwd()
    dirName = tkFileDialog.askdirectory(parent=root,initialdir = currdir)
    print dirName
    showDir.insert(0,dirName)
    theDict = makeDict(dirName)
    root.withdraw()

def destFind():
    root = Tkinter.Toplevel(top)
    currdir = os.getcwd()
    dirName = tkFileDialog.askdirectory(parent=root,initialdir = currdir)
    destDir.insert(0,dirName)
    root.withdraw()

def makeDict(directory):
    mydict= defaultdict(list)

    for file in os.listdir(directory):
        fileName = file[:-5].encode("ascii")
        print fileName
        if fileName not in mydict:
            mydict[fileName] = [file.encode("ascii")]
        else:
            mydict[fileName].append(file.encode("ascii"))
    return mydict

def mergeIt(fileNames, output, dire):

    merger = PdfFileMerger()
    for filename in fileNames:
        merger.append(PdfFileReader(dire + "/" + filename, 'rb'))
    merger.write(output+".pdf")

def mergeFiles():
    mergedir = showDir.get()
    mergedir += ""
    destdir = destDir.get()
    pageNum = IntVar()
    diction = makeDict(mergedir)
    print diction
    for key in diction:
        print key
        mergeList = diction[key]
        mergeIt(mergeList, destdir+ "/"+ key, mergedir)
        print "merged"
    print "Finished"



pickFile = Tkinter.Button(top, text="Chose File", command = fileFind)
pickDest = Tkinter.Button(top, text="Chose Dest", command = destFind)


m = Tkinter.Button(top, text="Merge", command = mergeFiles)
r = Tkinter.Button(top, text="Reset", command = resetCall)

pickFile.pack()
pickDest.pack()
showDir.pack()
destDir.pack()
m.pack()
r.pack()
top.mainloop()
