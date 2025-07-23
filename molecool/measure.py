"""
Functions for Measurements
"""
import numpy as np

def calculate_angle(rA:np.array, rB:np.array, rC:np.array, degrees=False):
    """Calculates angle subtended by three points

    Parameters
    ----------
    rA : np.array
        Point 1
    rB : np.array
        Point 2
    rC : np.array
        Point 3
    degrees : bool, optional
        In Degrees or Radians?, by default False

    Returns
    -------
    float
        Angle
    """
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta

def calculate_distance(rA, rB):
    # This function calculates the distance between two points given as numpy arrays.
    d=(rA-rB)
    dist=np.linalg.norm(d)
    return dist
