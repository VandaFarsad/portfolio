from portfolio.views import BaseView


def test_split_into_blocks():
    view = BaseView()
    assert view._split_into_blocks([1, 1, 2, 2, 3, 3], 2) == [[1, 1], [2, 2], [3, 3]]
    assert view._split_into_blocks([1, 1, 2, 2, 3, 3]) == [[1, 1, 2], [2, 3, 3]]
