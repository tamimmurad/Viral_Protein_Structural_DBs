# Viral Protein Structural Database Using Foldseek

## Description
This repository contains the following:
- Method of acquiring and curating PDB and AlphaFold existing structures.
- Building a searchable Foldseek Structural database for Viral Proteins. The proteins in the database are cluster representatives of previously obtained cluster representatives of viral proteins. The structures are as follows:

    - 1,014 PDB determined protein structures. 
    
    - 30 Alphafold predicted structures (already in AFDB)
    
    - 8,818 predicted structures with Alphafold done by our team.
    
A total of 9,826 structures are used to build a searchable foldseek Viral Protein Structural Database. 


## Methodology

### Files Preparation

As the clustering results produced PDB cluster reps on the chain level, it is required to download theses pdb structures and get the chain structures and not the whole thing. Below are the steps:

- Get all required PDB IDs without chain identifier and use the batch download command to get the structures(pdb ids must be in a csv file):
    
        $./batch_download.sh -f pdb_to_fetch.csv -o ./pdbF -c The results are cif.gz files. 
        $gunzip *
        
For the batch download refer to : https://www.rcsb.org/docs/programmatic-access/batch-downloads-with-shell-script

- Using the script 'prepare_pdb.py' extract the required chains into new 'cif' files.

For the AFDB structures, below are the steps:

- From the previously produced file of top clusters reps, get the AFDB ACCNs with the following command:

        $cat top_viral_protein_cluster_reps.tsv |awk '{print $4}'| grep tr >AF_predicted_vp.tsv
    
- Using the curl command, download the files directly from alphafold:

        $cat AF_predicted_vp.tsv | tr '_' '\t'| awk '{print $2}'| while read line; do wget https://alphafold.ebi.ac.uk/files/AF-$line-F1-model_v4.pdb ;done
    
### Databases 

Three structural databases were built to compare results of the searches as follow:

    - PDB_downloaded: This is available PDB database with foldseek.
    
    - AF_viralDB_inhouse: This comprises of the 9,826 top viral protein clusters as above.
    
    - ESM_viralDB_inhouse: 8,899 comprises both PDB and Alfaphold available structures in addition to 7855 ESM folded structures. These are top cluster reps structures folded with ESM using the curl command. Note that the curl command only accepts sequences less than 400 aa in length.

Details on DB creation can be found in https://github.com/steineggerlab/foldseek#databases

### Search Results

3 viral protein structures were downloaded from PDB. One is computer structure model and the other two are experimental structures.
They are used as queries against the 3 databases with foldseek. Below are links to the chosen proteins and the results can be found in the results folder.

https://www.rcsb.org/structure/MA_MAASFVASFVG156

https://www.rcsb.org/structure/5MU4

https://www.rcsb.org/structure/5H3A
