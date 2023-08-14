
import numpy as np
from statsmodels import robust

def d_func(v):
    a, b = v
    return a - b

def calculate_cv(data, probe):
    """
    Accept a pandas data frame with probe names as columns, PNs as rows.
    Each PN should occur twice
    Total assay CV is computed by randomizing the measurements before filtering to duplicate PNs.
    Returns CV based on the MAD estimator and the pairs of measurements for the PN
    Relative CV is defined as repeated CV / total CV
    """
    probe_data = data[['PN', probe]]
    pns_with_missing_data = probe_data[probe_data.isnull().any(axis=1)]['PN']
    subdata = data[~data['PN'].isin(pns_with_missing_data)][['PN', probe]]

    d = subdata.groupby('PN').agg(d_func)
    lib_mad = robust.mad(d, c=1)
    mad = lib_mad[0]

    val = 100 * np.sqrt(np.exp((np.log(2) * mad)**2) - 1)
    return val
