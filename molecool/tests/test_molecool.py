"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import molecool
from molecool.measure import calculate_angle

import numpy as np
from molecool.molecule import build_bond_list

def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "molecool" in sys.modules

def test_angle():
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 0, 0])
    r3 = np.array([1, 0, 0])
    expected_value = 90
    assert calculate_angle(r1, r2, r3, degrees=True) == expected_value

def test_bond_list():
    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4]
    ])
    bonds = build_bond_list(coordinates)
    assert len(bonds) == 4
    for bond_length in bonds.values():
        assert np.allclose(bond_length, 1.4)


def test_bond_list_failure():
    coordinates = np.array([
        [1, 1, 1],
        [2.4, 1, 1],
        [-0.4, 1, 1],
        [1, 1, 2.4],
        [1, 1, -0.4]
    ])
    with pytest.raises(ValueError):
        bonds = build_bond_list(coordinates, min_bond=-1)