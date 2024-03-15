from typing import List, Optional, Union

import numpy as np
import pandas as pd
from scipy.sparse import csr_array

from skfp.fingerprints.base import FingerprintTransformer


class RDKitFingerprint(FingerprintTransformer):
    def __init__(
        self,
        fp_size: int = 2048,
        min_path: int = 1,
        max_path: int = 7,
        use_hs: bool = True,
        use_bond_order: bool = True,
        num_bits_per_feature: int = 2,
        count: bool = False,
        sparse: bool = False,
        n_jobs: int = None,
        verbose: int = 0,
        random_state: int = 0,
    ):
        super().__init__(
            count=count,
            sparse=sparse,
            n_jobs=n_jobs,
            verbose=verbose,
            random_state=random_state,
        )
        self.fp_size = fp_size
        self.min_path = min_path
        self.max_path = max_path
        self.use_hs = use_hs
        self.use_bond_order = use_bond_order
        self.num_bits_per_feature = num_bits_per_feature

    def _get_generator(self):
        from rdkit.Chem.rdFingerprintGenerator import GetRDKitFPGenerator

        return GetRDKitFPGenerator(
            minPath=self.min_path,
            maxPath=self.max_path,
            useHs=self.use_hs,
            useBondOrder=self.use_bond_order,
            countSimulation=self.count,
            fpSize=self.fp_size,
            numBitsPerFeature=self.num_bits_per_feature,
        )

    def _calculate_fingerprint(
        self, X: Union[pd.DataFrame, np.ndarray, List[str]]
    ) -> Union[np.ndarray, csr_array]:
        X = self._validate_input(X)
        return self._generate_fingerprints(X)
