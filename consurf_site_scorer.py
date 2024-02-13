#!/usr/bin/env python3
#README for input format & use python 3

import csv
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--sitemap", required=True, help='input file with SiteMap residues // FORMAT --> See README for formating of input files.')
parser.add_argument("-c", "--consurf", required=True, help='input file with ConSurf data // FORMAT --> CSV See README for formating of input files.')
parser.add_argument("-o", "--output_score", required=True, help='score parameter that you want output // options --> average position of sites: [pos]; average conversvation score using normalized score [scoren]; average conservation score using color scores [color].')
args = parser.parse_args()

class Akagi:
  def __init__(self, pos, seq, atom3l, scoren, color, confidenceinterval, confidenceintervalcolors, msadata, residuevariety):
    self.pos = pos
    self.seq = seq
    self.seq = atom3l
    self.scoren = scoren
    self.color = color
    self.confidenceinterval = confidenceinterval
    self.confidenceintervalcolors = confidenceintervalcolors
    self.msadata = msadata
    self.residuevariety = residuevariety

Kaga=[]
    
with open(str(args.consurf), newline='') as csvfile:
    Noshiro = csv.reader(csvfile, delimiter=',', quotechar='"')
    for column in Noshiro:
        Kaga.append(Akagi(column[0],column[1],column[2],column[3],column[4],column[5],column[6],column[7],column[8]))

Little_Javi=[]

number_of_sites=np.arange(1,6)
for i in number_of_sites:
    file1 = open(str(args.sitemap),"r") #input file goes here
    site_residues=file1.readlines()[i-1]
    site_residues=site_residues.replace('\n','')
    site_residues=site_residues.replace('Chain A: ','')
    Little_Javi.append(site_residues.split(','))

site_conservation=[]
input_variable=str(args.output_score)

for i in number_of_sites:
    score_sum=0
    for j in Little_Javi[i-1]:
        dataline=Kaga[int(j)]
        exec("score_sum+=float(dataline.%s.replace('*',''))"%(input_variable))
    site_conservation.append(score_sum/len(Little_Javi[i-1]))
    exec("print('site_%s_score: ',site_conservation[%s-1])"%(i,i))

