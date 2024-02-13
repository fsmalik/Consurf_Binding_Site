# Consurf_Binding_Site
Contains the python script for determining conservation level of a binding site
#####################################################################
#####		                 	CONSURF CONVERTER		                   	#####
#####								                                                   #####
#####################################################################
### First use the converter script on your input data -- follow the steps before running
### Save the ""results summary"" from consurf in normal text format
### Open the file in a text editor and cmd+f to replace a goofiness replace ", " with "," -- note the space
### The first line for the input for the converter script should be the pos	seq	3latom ....
### Remove the second line in the file that only contains "(normalized)" -- you can change the "score" title to scoren if you like
### Delete any spaces from the title names
### First two lines should look something like this:
 POS	 SEQ	    3LATOM	SCOREN		COLOR	CONFIDENCEINTERVAL	CONFIDENCEINTERVALCOLORS	MSADATA		RESIDUEVARIETY
   1	   P	 PRO1000:A	 1.452		  1	 0.211,3.276			    4,1			   7/300	P,K,A,I,C,L
### THE THREE LINES OF JUNK AT THE END OF THE FILE SHOULD NOT BE INCLUDED IN THE TEXT FILE -- ONLY DATA!
### SO ... DELETE THESE LINES:
"*Below the confidence cut-off - The calculations for this site were performed on less than 6 non-gaped homologue sequences,"
"or the confidence interval for the estimated score is equal to- or larger than- 4 color grades."
### To run the converter: ./consurf_converter.sh [input file]
### After you running the converter, the converter put some double quotes in the column titles -- GET RID OF THEM.




#####################################################################
#####                   PYTHON CONSURF	                         #####
#####                       SCORER                              #####
#####################################################################
### Sample confsurf input format for python ###

POS,SEQ,3LATOM,SCORE(normalized),COLOR,CONFIDENCEINTERVAL,CONFIDENCEINTERVALCOLORS,MSADATA,RESIDUEVARIETY
1,"P","PRO1000:A","1.452","1","0.211,3.276","4,1","7/300","P,K,A,I,C,L"
2,"A","ALA1001:A","1.008",2*,"-0.087,1.817","5,1","5/300","A,S,T,I,K"
3,"D","ASP1002:A","0.845",3*,"-0.213,1.817","6,1","5/300","D,E,T,K"
4,"L","LEU1003:A","0.308",4*,"-0.698,0.891","7,3","4/300","L,I,N,M"
5,"E","GLU1004:A","-0.110",5*,"-0.921,0.396","7,4","4/300","E,S,N"
6,"D","ASP1005:A","-0.500",6*,"-1.342,0.053","9,5","1/300",D
7,"N","ASN1006:A","-0.229",6*,"-1.114,0.211","8,4","2/300","N,G"
8,"W","TRP1007:A","-0.376",6*,"-1.052,0.053","8,5","5/300","W,R,L"
9,"E","GLU1008:A","-0.584",7*,"-1.114,-0.326","8,6","5/300","E,D,N"

### The sitemap sites should be order in ascending order -- i.e. site1 first site5 last
### Script doesn't work if there are less than 5 sites in the sitemap input file
### The script is written assume the sites are in chain a; therefore the sitemap input file should look exactly like this:

Chain A: 2,3,4,5,6,7,8,9,10,11,12,26,29,33,81,84,85,88,89,90,91,102,105,106,109,110,113,156,159,160,164,175,176,177,178,179,180,181,183,187,190,191,193,194,197,198,200,201,202,204,205,209,210,250,254,257,258,260,261,262,264,265,268,271,272,274,275,276,278,280,281,282,284,285,286,288,289,292
Chain A: 60,63,64,119,122,123,126,127,137,221,224,228,235,236,237,238,239,240,242,243,246,301,302,303,305,306,307,308,309
Chain A: 3,6,7,167,168,169,170,175,179,180,181
Chain A: 59,118,121,122,125,132,137,138,141,142,145
Chain A: 114,117,118,121,149,152,212,213,216 
