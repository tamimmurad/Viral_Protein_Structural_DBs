#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 12:28:33 2023

@author: tamim
"""

import pandas as pd
from Bio.PDB import *


def get_chain(accn,chainName):

    parser = PDBParser()
    structure = parser.get_structure("structure","%s.pdb"%accn)
    model = structure[0]
    chain = model[chainName]
    io = PDBIO()
    io.set_structure(chain)
    io.save("%s_%s.pdb"%(accn,chainName))
  
def get_chain_cif(accn,chainName):

    parser = MMCIFParser()
    structure = parser.get_structure("structure","%s.cif"%accn)
    model = structure[0]
    chain = model[chainName]
    chain
    io = MMCIFIO()
    io.set_structure(chain)
    
    io.save("%s_%s.cif"%(accn,chainName))
    



    #%%
    
get_chain('5jzr','B')
    
