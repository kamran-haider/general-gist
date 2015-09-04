
import numpy as np
import mdtraj as md
import parmed as pmd


prmtop_filename = "/microwayhome/kamran/validation_simulations/amber/Abl_kinase/prod/kh.58991/abl.prmtop"
traj_filename = "/microwayhome/kamran/validation_simulations/amber/Abl_kinase/prod/kh.58991/md10.nc"


prmtop = pmd.load_file(prmtop_filename)

#first_frame = md.load_frame(traj_filename, 0, top=prmtop_filename)
#top = first_frame.topology


traj = md.load(traj_filename, top=prmtop_filename)
print traj