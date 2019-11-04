import pytest
from identity.mock_datastore import MockDatastore


def test_create_datastore():
    mds = MockDatastore()
    assert(isinstance(mds, object))


def test_create():
    mds = MockDatastore()
    assert(mds.create(1, {}) is True)


def test_read():
    mds = MockDatastore()
    mds.create(1, {})
    assert(mds.read(1) == {})


def test_update_existing():
    mds = MockDatastore()
    mds.create(1, {})
    mds.update(1, {})
    assert(mds.read(1) == {})


def test_update_nonexisting():
    mds = MockDatastore()
    mds.create(1, {})
    try:
        mds.update(2, {})
        assert False
    except KeyError:
        assert True

def test_delete_existing():
    mds = MockDatastore()
    mds.create(1, {})
    assert(mds.delete(1))

def test_delete_nonexisting():
    mds = MockDatastore()
    try:
        mds.delete(1)
        assert False
    except KeyError:
        assert True


def test_list_nothing():
    mds = MockDatastore()
    assert(len(mds.list()) == 0)


def test_list_3():
    mds = MockDatastore()
    mds.create(1, {})
    mds.create(2, {})
    mds.create(3, {})
    assert(len(mds.list()) == 3)
