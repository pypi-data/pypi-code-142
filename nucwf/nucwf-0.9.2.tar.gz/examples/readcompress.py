from nucwf import access
import os

tolerance=1E-6 
printlevel=3 

# script to 3N read file, compress it and read it in again 
file_in="/Users/andreasnogga/work/3n-wf/he3-vsrg-chsms-n4lo+-cut=04-lam=7.00-pCoul-n2lo-combine-Lam=550.000-c1=-1.230-c3=-4.650-c4=3.280-cd=-3.62570-ce=-0.41022.1+P.V-E=search-j12mx=6-lmx=8-tau3mx=3_2-j12mx3nf=6.npt=44+20-np12=44+12-np3=52+12-ne=20+10-nx=16.wave.h5"
file_out="/Users/andreasnogga/work/3n-wf/he3-vsrg-chsms-n4lo+-cut=04-lam=7.00-pCoul-n2lo-combine-Lam=550.000-c1=-1.230-c3=-4.650-c4=3.280-cd=-3.62570-ce=-0.41022.1+P.V-E=search-j12mx=6-lmx=8-tau3mx=3_2-j12mx3nf=6.npt=44+20-np12=44+12-np3=52+12-ne=20+10-nx=16.cpr.h5"


wfa3=access.wavefa3(file_in,printlevel)

wfa3.compress(file_out,tolerance,printlevel)

size_in=float(os.path.getsize(file_in))
size_out=float(os.path.getsize(file_out))
ratio=size_in/size_out 

wfa3comp=access.wavefa3(file_out,1)


print("Compression ratio: {0:6.2f}".format(ratio)) 



# script to 4N read file, compress it and read it in again 
file_in="/Users/andreasnogga/work/4n-wf/he4-vsrgNN-vsrg-chsms-n4lo+-cut=03-lam=7.00-pCoul-n2lo-combine-Lam=500.000-c1=-1.230-c3=-4.650-c4=3.280-cd=-1.27880-ce=-0.38214.1+P.V-E=search-j12mx=5-lmx=6-lsummx=10-tau4mx=0-j3mx3nf=13_2.npt=44+20-np1234=32+12-np3=44+12-nq4q=40+8-ne=15+5-nx=16.wave.h5"
file_out="/Users/andreasnogga/work/4n-wf/he4-vsrgNN-vsrg-chsms-n4lo+-cut=03-lam=7.00-pCoul-n2lo-combine-Lam=500.000-c1=-1.230-c3=-4.650-c4=3.280-cd=-1.27880-ce=-0.38214.1+P.V-E=search-j12mx=5-lmx=6-lsummx=10-tau4mx=0-j3mx3nf=13_2.npt=44+20-np1234=32+12-np3=44+12-nq4q=40+8-ne=15+5-nx=16.cpr.h5"


wfa4=access.wavefa4(file_in,printlevel)

wfa4.compress(file_out,tolerance,printlevel)

size_in=float(os.path.getsize(file_in))
size_out=float(os.path.getsize(file_out))
ratio=size_in/size_out 

wfa4comp=access.wavefa4(file_out,1)


print("Compression ratio: {0:6.2f}".format(ratio)) 
