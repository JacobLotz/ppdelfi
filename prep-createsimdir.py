import os
import numpy as np
import subprocess

def CreateDir(name_):
	os.mkdir(name_)

def DirName(dname_, n_):
	return dname_ + str(n_).zfill(3)

def CreateRunFile(n_, dname_, name_, k_, mname_):

	dirname = DirName(dname_, n_)
	CreateDir(dirname)

	fn = dirname+"/"+name_
	f = open(fn, "w")

	f.write("#!/bin/bash\n")
	f.write("#\n")
	f.write("#SBATCH --job-name=R" + str(n_).zfill(3)+"\n")
	f.write("#SBATCH --partition=compute\n")
	f.write("#SBATCH --account=research-3me-mtt\n")
	f.write("#SBATCH --output=log\n")
	f.write("#SBATCH --error=error.err\n")
	f.write("#SBATCH --ntasks=32\n")
	f.write("#SBATCH --cpus-per-task=1\n")
	f.write("#SBATCH --nodes=1\n")
	f.write("#SBATCH --mem-per-cpu=4G\n")
	f.write("#SBATCH --time=5-00:0:0\n")

	f.write("\n")
	f.write("srun ~/delfi/build/delfi  \\\n")
	f.write("   --physics SpTiNavStoPSPG \\\n")
	f.write("   -b spacetime.bcs           \\\n")
	f.write("   -dt 1                  \\\n")
	f.write("   -tf 3000               \\\n")
	f.write("   -fb 5                  \\\n")
	f.write("   -ptc 1e-5              \\\n")
	f.write("   -o 2                   \\\n")
	f.write("   -r 0                   \\\n")
	f.write("   -li 2000               \\\n")
	f.write("   -lt 0.01               \\\n")
	f.write("   -nt 0.01               \\\n")
	f.write("   -ni 5                  \\\n")
	f.write("   --offline              \\\n")
	f.write("   -ht 1                  \\\n")
	f.write("   -id " + str(n_) + " \\\n")
	f.write("   -m " + mname_ + ".mesh \\\n")
	f.write("   -k " + str(k_) + " \\\n")

	f.close()

def KappaRange(re_min_, re_max_, n_):
	re = np.linspace(re_min_, re_max_, n_)
	return 1/re

def MeshRange(mn_base_, n_):
	names = [None]*n_

	for i in range(0, n_):
		names[i] = mn_base_ + str(i).zfill(3)

	return names

def CreateMesh(extr_, mn_):
	# NCP of the mesh
	nbnd  = 68; 
	ntip  = 28; 
	ntail = 48; 
	nwake = 79;
	ntime = 49;

	# Other settings
	tf   = 0.1;
	b    = 8.0;
	w    = b;
	extr = extr_
	ha   = 0.5;
	aoa  = 0.0;

	# Mesh stretches
	sbnd = 3.0;
	stip = 1.2;
	stail = 1.2;
	sw   = 1.2;

	# Create mesh
	script = "/home/jelotz/prog/delfi/build/navierstokes/nacast/mesher2"

	subprocess.run([script, "-tf", str(tf), "-b", str(b), "-w", str(w)
		, "-sbnd", str(sbnd), "-stip", str(stip), "-sw" , str(sw), "-stail" , str(stail)
		,"-nbnd", str(nbnd),  "-ntip", str(ntip), "-ntail"
		, str(ntail), "-nwake", str(nwake),"-m", mn_, "-aoa", str(aoa),
		"-ntime", str(ntime),"-ha", str(ha)])



# Input
maindirname = "simulations"
dirname = "run"

filename = "run"
meshnamebase = "naca-cmesh"
re_min = 200
re_max = 800
n_runs = 30

T_min = 4
T_max = 8


CreateDir(maindirname)
dirname = maindirname + "/" + dirname

kr      = KappaRange(re_min, re_max, n_runs)
mnr     = MeshRange(meshnamebase, n_runs)
periodr = np.linspace(T_min, T_max, n_runs)

for i in range(0, n_runs):
	k = kr[i]
	mn = mnr[i]
	CreateRunFile(i, dirname, filename, k, mn)

	mn = os.getcwd() + "/" + DirName(dirname, i) + "/" + mn;

	period = 8
	CreateMesh(period, mn)
