import pandas as pd
import pytest
from rdkit.Chem import MolFromSmiles, Mol


@pytest.fixture(scope="session")
def smiles_list() -> list[str]:
    smiles = pd.read_csv("tests/hiv_mol.csv.zip")["smiles"]
    return smiles.tolist()[:100]


@pytest.fixture(scope="session")
def smiles_list_short() -> list[str]:
    # shorter list of small molecules, for computationally demanding fingerprints
    smiles = pd.read_csv("tests/hiv_mol.csv.zip")["smiles"]
    smiles = smiles.sort_values(by=lambda smi: len(smi))
    return smiles.tolist()[:100]


@pytest.fixture(scope="session")
def mols_list(smiles_list) -> list[Mol]:
    return [MolFromSmiles(smi) for smi in smiles_list]
