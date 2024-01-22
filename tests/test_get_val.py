import pytest

from utils.dicts import get_val


@pytest.mark.parametrize('data, key, default, expected', [
    ({"vcs": "mercurial"}, "vcs", None, 'mercurial'),
    ({"vcs": "mercurial"}, "vcs", "git", 'mercurial'),
    ({}, "vcs", "git", 'git'),
    ({}, "vcs", "bazaar", 'bazaar')
])
def test_get_val(data, key, default, expected):
    assert get_val(data, key, default) == expected
