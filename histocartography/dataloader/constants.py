import dgl
import torch

NORMALIZATION_FACTORS = {
    'cell_graph': {'mean': torch.tensor([9.3564e+01, 6.4326e+01, 4.2089e+02, 6.0968e-01, 4.3258e+00, 2.0927e+03,
                                         4.0686e+01, 1.7329e+01, 3.8951e+02, 7.1562e-01, 2.5981e+02, 2.2306e+01,
                                         1.3914e+01, 6.1413e+01, 9.4021e-01, 8.7411e+01]),
                   'std': torch.tensor([1.5778e+01, 2.2866e+01, 2.4106e+02, 4.6837e-01, 1.2226e-01, 1.2184e+03,
                                        2.6063e+01, 5.9187e+00, 2.9949e+02, 1.5391e-01, 1.4410e+02, 8.3460e+00,
                                        4.2261e+00, 1.8914e+01, 4.6122e-02, 5.4640e+01])},
    'superpx_graph': {'mean': torch.tensor([9.8782e+03,  1.3999e+04,  6.8630e-01,  1.0130e+02,  9.9361e-01,
                                            6.1730e-01,  1.0056e+04,  1.4098e+02,  8.8163e+01, -8.1380e-03,
                                            5.2410e+02,  8.0428e-01,  4.1889e-05,  6.9453e-03,  4.7210e-02,
                                            9.2762e-02,  1.2938e-01,  1.7160e-01,  1.9835e-01,  3.5371e-01,
                                            1.9154e+02,  4.2511e+01,  1.9685e+02, -6.2980e-01,  9.2006e+01,
                                            1.6873e-03,  5.7667e-02,  1.4617e-01,  2.0471e-01,  2.1555e-01,
                                            1.5971e-01,  9.5827e-02,  1.1867e-01,  1.4530e+02,  4.3219e+01,
                                            1.4403e+02,  1.6516e-01,  1.0076e+02,  7.9969e-08,  2.6933e-04,
                                            1.9439e-02,  1.2013e-01,  2.5082e-01,  2.9203e-01,  1.7079e-01,
                                            1.4653e-01,  1.7362e+02,  3.2325e+01,  1.7330e+02,  6.1347e-02,
                                            1.0140e+02,  4.2272e+00,  2.1136e+02,  1.0233e+01,  1.4269e-01,
                                            3.7047e-02,  4.2254e-03]),
                      'std': torch.tensor([2.6445e+04, 5.4092e+04, 1.7531e-01, 4.1159e+01, 1.1517e-01, 1.2963e-01,
                                           2.9681e+04, 9.5053e+01, 3.8658e+01, 8.9850e-01, 5.7983e+02, 9.9265e-02,
                                           3.2537e-04, 1.1022e-02, 6.4484e-02, 9.0346e-02, 7.3688e-02, 6.2088e-02,
                                           7.6974e-02, 2.2294e-01, 2.9977e+01, 9.5090e+00, 3.6593e+01, 9.3088e-01,
                                           1.6831e+01, 4.2219e-03, 8.2087e-02, 1.2135e-01, 8.9812e-02, 9.5390e-02,
                                           8.9910e-02, 6.7493e-02, 1.6975e-01, 3.4042e+01, 9.4136e+00, 4.0184e+01,
                                           7.7200e-01, 1.1815e+01, 8.7333e-07, 1.4743e-03, 3.3034e-02, 1.3060e-01,
                                           1.2300e-01, 1.2893e-01, 1.0258e-01, 1.8401e-01, 2.5695e+01, 7.1470e+00,
                                           2.9613e+01, 7.4068e-01, 1.3201e+01, 3.8910e-01, 7.8849e+01, 2.2950e+00,
                                           9.0690e-02, 6.4540e-02, 2.9741e-02])}
    }


COLLATE_FN = {
    'DGLGraph': lambda x: dgl.batch(x),
    'Tensor': lambda x: x,
    'PngImageFile': lambda x: x,
    'str': lambda x: x
}


# tumor type to 4. Currently UDH, ADH, FEA and DCIS are grouped under the same label
TUMOR_TYPE_TO_LABEL = {
    'benign': 0,
    'pathological_benign': 1,
    'dcis': 2,
    'malignant': 3,
    'udh': 4,
    'adh': 4,
    'fea': 4
}


# List of classes to discard for training
DATASET_BLACKLIST = ['adh', 'fea', 'udh']

DATASET_TO_TUMOR_TYPE = {
    '0_benign': 'benign',
    '1_pathological_benign': 'pathological_benign',
    '2_udh': 'udh',
    '3_adh': 'adh',
    '4_fea': 'fea',
    '5_dcis': 'dcis',
    '6_malignant': 'malignant'
}
