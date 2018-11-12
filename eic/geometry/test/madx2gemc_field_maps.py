#!/usr/local/bin python2.7
from string import *
import commands
import sys
import os.path
from copy import deepcopy
from math import pi
from math import trunc
from math import cos
from math import sin

ele_inpfile="jleic_v16v2_det_reg_elem_bg_sim_18Oct18_electron.txt"
ion_inpfile="ion_ir_v16_05sep18.txt"
f1=open(ele_inpfile,"r")
holder=f1.readlines()
length=len(holder)
f1.close()

elemlist=[]

outfile=ele_inpfile.replace(".txt","__geometry_Original.txt")
f2=open(outfile,"w")

os.system("cp jleic_detector_beamline_template.gcard jleic_detector_beamline.gcard")
f4=open("jleic_detector_beamline.gcard","a")

if not os.path.isdir("./field"):
  os.system("mkdir field")

for i in range(length):
  temp=holder[i]
  temp=temp.split()
  # print str(len(temp))+" \n"
  if len(temp) >= 2:
    if temp[1]=="QUADRUPOLE":
      elemlist.append(temp[0])
      elname=temp[0]+str(elemlist.count(temp[0]))
      xc=float(temp[8])
      yc=float(temp[9])
      zc=float(temp[10])
      thc=float(temp[11])
      iha=float(temp[4])
      ohs=float(temp[5])
      l=float(temp[2])
      dbydx=float(temp[6])
      dbxdx=float(temp[7])
      temp_write=elname+"_iron | root | "+elname+"_iron | "+str(xc)+"*m "+str(yc)+"*m "+str(zc)+"*m | 0*rad "+str(-thc)+"*rad 0*rad | "+\
                 "AA00FF | Tube | 0*cm "+str(ohs)+"*cm "+str(l/2)+"*m 0*deg 360*deg | Kryptonite | no | 1 | 1 | 1 | 1 | 1 | no | no | no \n"
      f2.write(temp_write)
      temp_write=elname+"_field | "+elname+"_iron | "+elname+"_field | 0*m 0*m 0*m | 0*rad 0*rad 0*rad | "+\
                 "CDE6FA | Tube | 0*cm "+str(iha)+"*cm "+str(l/2)+"*m 0*deg 360*deg | Vacuum | "+elname+"_map"+" | 1 | 1 | 1 | 1 | 1 | no | no | no \n"
      f2.write(temp_write)
      f3=open("./field/"+elname+"_map.dat","w")
      f3.write("<mfield> \n")
      f3.write("<description name=\""+elname+"_map\" factory=\"ASCII\" comment=\""+elname+"_map\"/> \n")
      f3.write("<symmetry type=\"cartesian_3D\" format=\"map\" />\n")
      f3.write("<map>\n")
      f3.write("<coordinate>\n")
      f3.write("<first name =\"X\" npoints=\"5\" min=\""+str(-iha)+"\" max=\""+str(iha)+"\" units=\"cm\"/> \n")
      f3.write("<second name =\"Y\" npoints=\"5\" min=\""+str(-iha)+"\" max=\""+str(iha)+"\" units=\"cm\"/> \n")
      f3.write("<third name =\"Z\" npoints=\"5\" min=\""+str(-l/2)+"\" max=\""+str(l/2)+"\" units=\"m\"/> \n")
      f3.write("</coordinate> \n")
      f3.write("<field unit=\"T\" />\n")
      f3.write("</map>\n")
      f3.write("</mfield>\n")
      for i in range(5):
        for j in range(5):
          for k in range(5):
            xm=(i-2)*iha/2
            ym=(j-2)*iha/2
            zm=(k-2)*l/2/2
            bx=dbxdx*xm*0.01+dbydx*ym*0.01
            by=dbydx*xm*0.01-dbxdx*ym*0.01
            f3.write(str(xm)+" "+str(ym)+" "+\
            str(zm)+" "+str(bx)+" "+str(by)+" 0\n")
      f3.close()
      f4.write("<option name=\"ROTATE_FIELDMAP\" value=\""+elname+"_map, 0*rad, "+str(thc)+"*rad, 0*rad\"/> \n")
      f4.write("<option name=\"DISPLACE_FIELDMAP\" value=\""+elname+"_map,"+str(xc)+"*m, "+str(yc)+"*m, "+str(zc)+"*m\"/> \n")
      f4.write("<option name=\"FIELD_PROPERTIES\" value=\""+elname+"_map, 1*mm, G4SimpleRunge, linear\"/> \n")
    elif temp[1]=="RBEND":
#    elif temp[0]=="eBDS1":
      elemlist.append(temp[0])
      elname=temp[0]+str(elemlist.count(temp[0]))
      xc=float(temp[8])
      yc=float(temp[9])
      zc=float(temp[10])
      thc=float(temp[11])
      iha=float(temp[4])
      ohs=float(temp[5])
      l=float(temp[2])
      by=float(temp[6])
      temp_write=elname+"_iron | root | "+elname+"_iron | "+str(xc)+"*m "+str(yc)+"*m "+str(zc)+"*m | 0*rad "+str(-thc)+"*rad 0*rad | "+\
                 "00FF00 | Box | "+str(ohs)+"*cm "+str(ohs)+"*cm "+str(l/2)+"*m | Kryptonite | no | 1 | 1 | 1 | 1 | 1 | no | no | no \n"
      f2.write(temp_write)
      temp_write=elname+"_field | "+elname+"_iron | "+elname+"_field | 0*m 0*m 0*m | 0*rad 0*rad 0*rad | "+\
                 "CDE6FA | Box | "+str(iha)+"*cm "+str(iha)+"*cm "+str(l/2)+"*m | Vacuum | "+elname+"_map | 1 | 1 | 1 | 1 | 1 | no | no | no \n"
      f2.write(temp_write)
      f3=open("./field/"+elname+"_map.dat","w")
      f3.write("<mfield> \n")
      f3.write("<description name=\""+elname+"_map\" factory=\"ASCII\" comment=\""+elname+"_map\"/> \n")
      f3.write("<symmetry type=\"cartesian_3D\" format=\"map\" />\n")
      f3.write("<map>\n")
      f3.write("<coordinate>\n")
      f3.write("<first name =\"X\" npoints=\"5\" min=\""+str(-iha)+"\" max=\""+str(iha)+"\" units=\"cm\"/> \n")
      f3.write("<second name =\"Y\" npoints=\"5\" min=\""+str(-iha)+"\" max=\""+str(iha)+"\" units=\"cm\"/> \n")
      f3.write("<third name =\"Z\" npoints=\"5\" min=\""+str(-l/2)+"\" max=\""+str(l/2)+"\" units=\"m\"/> \n")
      f3.write("</coordinate> \n")
      f3.write("<field unit=\"T\" />\n")
      f3.write("</map>\n")
      f3.write("</mfield>\n")
      for i in range(5):
	    for j in range(5):
		  for k in range(5):
		    f3.write(str((i-2)*iha/2)+" "+str((j-2)*iha/2)+" "+\
			str((k-2)*l/2/2)+" 0 "+str(by)+" 0\n")
      f3.close()
      f4.write("<option name=\"ROTATE_FIELDMAP\" value=\""+elname+"_map, 0*rad, "+str(thc)+"*rad, 0*rad\"/> \n")
      f4.write("<option name=\"DISPLACE_FIELDMAP\" value=\""+elname+"_map,"+str(xc)+"*m, "+str(yc)+"*m, "+str(zc)+"*m\"/> \n")
      f4.write("<option name=\"FIELD_PROPERTIES\" value=\""+elname+"_map, 1*mm, G4SimpleRunge, linear\"/> \n")
    elif temp[1]=="SOLENOID":
      elemlist.append(temp[0])
      elname=temp[0]+str(elemlist.count(temp[0]))
      xc=float(temp[8])
      yc=float(temp[9])
      zc=float(temp[10])
      thc=float(temp[11])
      iha=float(temp[4])
      ohs=float(temp[5])
      l=float(temp[2])
      bz=float(temp[6])
      temp_write=elname+"_iron | root | "+elname+"_iron | "+str(xc)+"*m "+str(yc)+"*m "+str(zc)+"*m | 0*rad "+str(-thc)+"*rad 0*rad | "+\
                 "0000FF2 | Tube | 0*cm "+str(ohs)+"*cm "+str(l/2)+"*m 0*deg 360*deg | Kryptonite | no | 1 | 1 | 1 | 1 | 1 | no | no | no \n"
      f2.write(temp_write)
      temp_write=elname+"_field | "+elname+"_iron | "+elname+"_field | 0*m 0*m 0*m | 0*rad 0*rad 0*rad | "+\
                 "CDE6FA2 | Tube | 0*cm "+str(iha)+"*cm "+str(l/2)+"*m 0*deg 360*deg | Vacuum | "+elname+"_map"+" | 1 | 1 | 1 | 1 | 1 | no | no | no \n"
      f2.write(temp_write)
      f3=open("./field/"+elname+"_map.dat","w")
      f3.write("<mfield> \n")
      f3.write("<description name=\""+elname+"_map\" factory=\"ASCII\" comment=\""+elname+"_map\"/> \n")
      f3.write("<symmetry type=\"cartesian_3D\" format=\"map\" />\n")
      f3.write("<map>\n")
      f3.write("<coordinate>\n")
      f3.write("<first name =\"X\" npoints=\"5\" min=\""+str(-iha)+"\" max=\""+str(iha)+"\" units=\"cm\"/> \n")
      f3.write("<second name =\"Y\" npoints=\"5\" min=\""+str(-iha)+"\" max=\""+str(iha)+"\" units=\"cm\"/> \n")
      f3.write("<third name =\"Z\" npoints=\"5\" min=\""+str(-l/2)+"\" max=\""+str(l/2)+"\" units=\"m\"/> \n")
      f3.write("</coordinate> \n")
      f3.write("<field unit=\"T\" />\n")
      f3.write("</map>\n")
      f3.write("</mfield>\n")
      for i in range(5):
        for j in range(5):
          for k in range(5):
            xm=(i-2)*iha/2
            ym=(j-2)*iha/2
            zm=(k-2)*l/2/2
            f3.write(str(xm)+" "+str(ym)+" "+\
            str(zm)+" 0 0 "+str(bz)+" \n")
      f3.close()
      f4.write("<option name=\"ROTATE_FIELDMAP\" value=\""+elname+"_map, 0*rad, "+str(thc)+"*rad, 0*rad\"/> \n")
      f4.write("<option name=\"DISPLACE_FIELDMAP\" value=\""+elname+"_map,"+str(xc)+"*m, "+str(yc)+"*m, "+str(zc)+"*m\"/> \n")
      f4.write("<option name=\"FIELD_PROPERTIES\" value=\""+elname+"_map, 1*mm, G4SimpleRunge, linear\"/> \n")
f2.close()

# Ion elements

f1=open(ion_inpfile,"r")
holder=f1.readlines()
length=len(holder)
f1.close()

elemlist=[]

outfile=ion_inpfile.replace(".txt","__geometry_Original.txt")
f2=open(outfile,"w")

for i in range(length):
  temp=holder[i]
  temp=temp.split()
  # print str(len(temp))+" \n"
  if len(temp) >= 2:
    if temp[1]=="QUADRUPOLE":
      elemlist.append(temp[0])
      elname=temp[0]+str(elemlist.count(temp[0]))
      xc=float(temp[12])
      yc=float(temp[13])
      zc=float(temp[14])
      thc=float(temp[15])
      iha=float(temp[4])
      ohs=float(temp[5])
      l=float(temp[2])
      dbydx=float(temp[8])
      dbxdx=float(temp[9])
      temp_write=elname+"_iron | root | "+elname+"_iron | "+str(xc)+"*m "+str(yc)+"*m "+str(zc)+"*m | 0*rad "+str(-thc)+"*rad 0*rad | "+\
                 "FF00002 | Tube | 0*cm "+str(ohs)+"*cm "+str(l/2)+"*m 0*deg 360*deg | Kryptonite | no | 1 | 1 | 1 | 1 | 1 | no | no | no \n"
      f2.write(temp_write)
      temp_write=elname+"_field | "+elname+"_iron | "+elname+"_field | 0*m 0*m 0*m | 0*rad 0*rad 0*rad | "+\
                 "CDE6FA | Tube | 0*cm "+str(iha)+"*cm "+str(l/2)+"*m 0*deg 360*deg | Vacuum | "+elname+"_map"+" | 1 | 1 | 1 | 1 | 1 | no | no | no \n"
      f2.write(temp_write)
      f3=open("./field/"+elname+"_map.dat","w")
      f3.write("<mfield> \n")
      f3.write("<description name=\""+elname+"_map\" factory=\"ASCII\" comment=\""+elname+"_map\"/> \n")
      f3.write("<symmetry type=\"cartesian_3D\" format=\"map\" />\n")
      f3.write("<map>\n")
      f3.write("<coordinate>\n")
      f3.write("<first name =\"X\" npoints=\"5\" min=\""+str(-iha)+"\" max=\""+str(iha)+"\" units=\"cm\"/> \n")
      f3.write("<second name =\"Y\" npoints=\"5\" min=\""+str(-iha)+"\" max=\""+str(iha)+"\" units=\"cm\"/> \n")
      f3.write("<third name =\"Z\" npoints=\"5\" min=\""+str(-l/2)+"\" max=\""+str(l/2)+"\" units=\"m\"/> \n")
      f3.write("</coordinate> \n")
      f3.write("<field unit=\"T\" />\n")
      f3.write("</map>\n")
      f3.write("</mfield>\n")
      for i in range(5):
        for j in range(5):
          for k in range(5):
            xm=(i-2)*iha/2
            ym=(j-2)*iha/2
            zm=(k-2)*l/2/2
            bx=dbxdx*xm*0.01+dbydx*ym*0.01
            by=dbydx*xm*0.01-dbxdx*ym*0.01
            f3.write(str(xm)+" "+str(ym)+" "+\
            str(zm)+" "+str(bx)+" "+str(by)+" 0\n")
      f3.close()
      f4.write("<option name=\"ROTATE_FIELDMAP\" value=\""+elname+"_map, 0*rad, "+str(thc)+"*rad, 0*rad\"/> \n")
      f4.write("<option name=\"DISPLACE_FIELDMAP\" value=\""+elname+"_map,"+str(xc)+"*m, "+str(yc)+"*m, "+str(zc)+"*m\"/> \n")
      f4.write("<option name=\"FIELD_PROPERTIES\" value=\""+elname+"_map, 1*mm, G4SimpleRunge, linear\"/> \n")
    elif temp[1] in ["RBEND","KICKER"]:
      elemlist.append(temp[0])
      elname=temp[0]+str(elemlist.count(temp[0]))
      xc=float(temp[12])
      yc=float(temp[13])
      zc=float(temp[14])
      thc=float(temp[15])
      iha=float(temp[4])
      ohs=float(temp[5])
      l=float(temp[2])
      bx=float(temp[6])
      by=float(temp[7])
      dbydx=float(temp[8])
      dbxdx=float(temp[9])
      temp_write=elname+"_iron | root | "+elname+"_iron | "+str(xc)+"*m "+str(yc)+"*m "+str(zc)+"*m | 0*rad "+str(-thc)+"*rad 0*rad | "+\
                 "00FF00 | Box | "+str(ohs)+"*cm "+str(ohs)+"*cm "+str(l/2)+"*m | Kryptonite | no | 1 | 1 | 1 | 1 | 1 | no | no | no \n"
      f2.write(temp_write)
      temp_write=elname+"_field | "+elname+"_iron | "+elname+"_field | 0*m 0*m 0*m | 0*rad 0*rad 0*rad | "+\
                 "CDE6FA | Box | "+str(iha)+"*cm "+str(iha)+"*cm "+str(l/2)+"*m | Vacuum | "+elname+"_map | 1 | 1 | 1 | 1 | 1 | no | no | no \n"
      f2.write(temp_write)
      f3=open("./field/"+elname+"_map.dat","w")
      f3.write("<mfield> \n")
      f3.write("<description name=\""+elname+"_map\" factory=\"ASCII\" comment=\""+elname+"_map\"/> \n")
      f3.write("<symmetry type=\"cartesian_3D\" format=\"map\" />\n")
      f3.write("<map>\n")
      f3.write("<coordinate>\n")
      f3.write("<first name =\"X\" npoints=\"5\" min=\""+str(-iha)+"\" max=\""+str(iha)+"\" units=\"cm\"/> \n")
      f3.write("<second name =\"Y\" npoints=\"5\" min=\""+str(-iha)+"\" max=\""+str(iha)+"\" units=\"cm\"/> \n")
      f3.write("<third name =\"Z\" npoints=\"5\" min=\""+str(-l/2)+"\" max=\""+str(l/2)+"\" units=\"m\"/> \n")
      f3.write("</coordinate> \n")
      f3.write("<field unit=\"T\" />\n")
      f3.write("</map>\n")
      f3.write("</mfield>\n")
      for i in range(5):
        for j in range(5):
          for k in range(5):
            xm=(i-2)*iha/2
            ym=(j-2)*iha/2
            zm=(k-2)*l/2/2
            bxm=bx+dbxdx*xm*0.01+dbydx*ym*0.01
            bym=by+dbydx*xm*0.01-dbxdx*ym*0.01
            f3.write(str(xm)+" "+str(ym)+" "+str(zm)+" "+str(bxm)+" "+str(bym)+" 0\n")
      f3.close()
      f4.write("<option name=\"ROTATE_FIELDMAP\" value=\""+elname+"_map, 0*rad, "+str(thc)+"*rad, 0*rad\"/> \n")
      f4.write("<option name=\"DISPLACE_FIELDMAP\" value=\""+elname+"_map,"+str(xc)+"*m, "+str(yc)+"*m, "+str(zc)+"*m\"/> \n")
      f4.write("<option name=\"FIELD_PROPERTIES\" value=\""+elname+"_map, 1*mm, G4SimpleRunge, linear\"/> \n")
    elif temp[1]=="SOLENOID" and temp[0] not in ["iDSUS","iDSDS"]:
      elemlist.append(temp[0])
      elname=temp[0]+str(elemlist.count(temp[0]))
      xc=float(temp[12])
      yc=float(temp[13])
      zc=float(temp[14])
      thc=float(temp[15])
      iha=float(temp[4])
      ohs=float(temp[5])
      l=float(temp[2])
      bz=float(temp[11])
      temp_write=elname+"_iron | root | "+elname+"_iron | "+str(xc)+"*m "+str(yc)+"*m "+str(zc)+"*m | 0*rad "+str(-thc)+"*rad 0*rad | "+\
                 "0000FF2 | Tube | 0*cm "+str(ohs)+"*cm "+str(l/2)+"*m 0*deg 360*deg | Kryptonite | no | 1 | 1 | 1 | 1 | 1 | no | no | no \n"
      f2.write(temp_write)
      temp_write=elname+"_field | "+elname+"_iron | "+elname+"_field | 0*m 0*m 0*m | 0*rad 0*rad 0*rad | "+\
                 "CDE6FA2 | Tube | 0*cm "+str(iha)+"*cm "+str(l/2)+"*m 0*deg 360*deg | Vacuum | "+elname+"_map"+" | 1 | 1 | 1 | 1 | 1 | no | no | no \n"
      f2.write(temp_write)
      f3=open("./field/"+elname+"_map.dat","w")
      f3.write("<mfield> \n")
      f3.write("<description name=\""+elname+"_map\" factory=\"ASCII\" comment=\""+elname+"_map\"/> \n")
      f3.write("<symmetry type=\"cartesian_3D\" format=\"map\" />\n")
      f3.write("<map>\n")
      f3.write("<coordinate>\n")
      f3.write("<first name =\"X\" npoints=\"5\" min=\""+str(-iha)+"\" max=\""+str(iha)+"\" units=\"cm\"/> \n")
      f3.write("<second name =\"Y\" npoints=\"5\" min=\""+str(-iha)+"\" max=\""+str(iha)+"\" units=\"cm\"/> \n")
      f3.write("<third name =\"Z\" npoints=\"5\" min=\""+str(-l/2)+"\" max=\""+str(l/2)+"\" units=\"m\"/> \n")
      f3.write("</coordinate> \n")
      f3.write("<field unit=\"T\" />\n")
      f3.write("</map>\n")
      f3.write("</mfield>\n")
      for i in range(5):
        for j in range(5):
          for k in range(5):
            xm=(i-2)*iha/2
            ym=(j-2)*iha/2
            zm=(k-2)*l/2/2
            f3.write(str(xm)+" "+str(ym)+" "+str(zm)+" 0 0 "+str(bz)+" \n")
      f3.close()
      f4.write("<option name=\"ROTATE_FIELDMAP\" value=\""+elname+"_map, 0*rad, "+str(thc)+"*rad, 0*rad\"/> \n")
      f4.write("<option name=\"DISPLACE_FIELDMAP\" value=\""+elname+"_map,"+str(xc)+"*m, "+str(yc)+"*m, "+str(zc)+"*m\"/> \n")
      f4.write("<option name=\"FIELD_PROPERTIES\" value=\""+elname+"_map, 1*mm, G4SimpleRunge, linear\"/> \n")
f2.close()

f4.write("</gcard> \n")
f4.close()
sys.exit()

