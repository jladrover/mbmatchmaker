import numpy as np
from scipy.spatial.distance import cosine

def cosine_similarity(vector1, vector2):
    return 1 - cosine(vector1, vector2)

