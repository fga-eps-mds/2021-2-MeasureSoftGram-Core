from src.core.weighting import weighting_operation
import pytest

from src.util.exceptions import ValuesAndWeightsOfDifferentSizes


VALID_WEIGHTING_OPERATION = [
    ([0.30, 0.32, 0.12], [0.30, 0.45, 0.25], [0.09, 0.144, 0.03]),
    ([0.40, 0.50, 0.10], [0.30, 0.45, 0.25], [0.12, 0.225, 0.025]),
    ([0.20, 0.30, 0.50], [0.25, 0.40, 0.35], [0.05, 0.12, 0.175])
]


INVALID_SIZES = [
    ([0.30], [0.30, 0.70]),
    ([0.30, 0.45], [1.00]),
    ([0.30, 0.32], [0.30, 0.45, 0.25]),
    ([0.30, 0.32, 0.12], [0.30, 0.70]),
    ([0.30, 0.32, 0.02], [0.30, 0.45, 0.15, 0.10]),
    ([0.30, 0.32, 0.02, 0.10], [0.30, 0.45, 0.25])
]


@pytest.mark.parametrize("values, weights, res", VALID_WEIGHTING_OPERATION)
def test_valid_weighting_operation(values, weights, res):
    """
    Test cases in which the weighting operation should return a valid result
    """

    result = weighting_operation(values, weights)
    assert pytest.approx(result.tolist()) == res


@pytest.mark.parametrize("values, weights", INVALID_SIZES)
def test_different_sizes(values, weights):
    """
    Test cases in which the size of the weight and values are not the same
    """

    with pytest.raises(ValuesAndWeightsOfDifferentSizes):
        weighting_operation(values, weights)
