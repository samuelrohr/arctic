import getpass

import pytest

from arctic.scripts import arctic_delete_library
from ...util import run_as_main


@pytest.fixture(scope='function')
def library_name():
    return 'user.library'


@pytest.fixture(scope='function')
def user_library_name():
    return "{}.library".format(getpass.getuser().replace(".", ""))


def test_delete_library(mongo_host, arctic, library, user_library):
    assert 'user.library' in arctic.list_libraries()
    assert '%s.library' % getpass.getuser().replace(".", "") in arctic.list_libraries()
    run_as_main(arctic_delete_library.main, '--host', mongo_host,
                '--library', 'user.library')
    assert 'user.library' not in arctic.list_libraries()
    assert '%s.library' % getpass.getuser().replace(".", "") in arctic.list_libraries()


def test_delete_library1(mongo_host, arctic, library, user_library):
    assert 'user.library' in arctic.list_libraries()
    assert '%s.library' % getpass.getuser().replace(".", "") in arctic.list_libraries()
    run_as_main(arctic_delete_library.main, '--host', mongo_host,
                '--library', 'arctic_user.library')
    assert 'user.library' not in arctic.list_libraries()
    assert '%s.library' % getpass.getuser().replace(".", "") in arctic.list_libraries()


def test_delete_library2(mongo_host, arctic, library, user_library):
    assert 'user.library' in arctic.list_libraries()
    assert '%s.library' % getpass.getuser().replace(".", "") in arctic.list_libraries()
    run_as_main(arctic_delete_library.main, '--host', mongo_host,
                '--library', 'arctic_%s.library' % getpass.getuser().replace(".", ""))
    assert 'user.library' in arctic.list_libraries()
    assert '%s.library' % getpass.getuser().replace(".", "") not in arctic.list_libraries()


def test_delete_library3(mongo_host, arctic, library, user_library):
    assert 'user.library' in arctic.list_libraries()
    assert '%s.library' % getpass.getuser().replace(".", "") in arctic.list_libraries()
    run_as_main(arctic_delete_library.main, '--host', mongo_host,
                '--library', '%s.library' % getpass.getuser().replace(".", ""))
    assert 'user.library' in arctic.list_libraries()
    assert '%s.library' % getpass.getuser().replace(".", "") not in arctic.list_libraries()


def test_delete_library_doesnt_exist(mongo_host, arctic, library, user_library):
    assert 'user.library' in arctic.list_libraries()
    assert '%s.library' % getpass.getuser().replace(".", "") in arctic.list_libraries()
    run_as_main(arctic_delete_library.main, '--host', mongo_host,
                '--library', 'arctic_nosuchlibrary.missing')
    assert 'user.library' in arctic.list_libraries()
    assert '%s.library' % getpass.getuser().replace(".", "") in arctic.list_libraries()
