from helixfold.data.pipeline_parallel import make_msa_features
from helixfold.data import parsers
import os

def get_text(p):
    with open(p, 'r') as f:
        return f.read()

def try_creating_msa_features(folder):
    uniref90_msa = parsers.parse_stockholm(get_text(os.path.join(folder, 'uniref90_hits.sto')))
    mgnify_msa = parsers.parse_stockholm(get_text(os.path.join(folder, 'mgnify_hits.sto')))
    bfd_msa = parsers.parse_stockholm(get_text(os.path.join(folder, 'small_bfd_hits.sto')))
    msa_features = make_msa_features((uniref90_msa, bfd_msa, mgnify_msa))

if __name__ == '__main__':
    # internal_xtal_folder = "/home/anindit/paddle-helix-fork/apps/protein_folding/helixfold3/output/row-0/msas/protein_A/A"
    posebuster_folder = "/home/anindit/deep-affinity/experimental/users/anindit/posebuster_5SAK_ZRY/sto"
    msa_features = try_creating_msa_features(posebuster_folder)
    
    
