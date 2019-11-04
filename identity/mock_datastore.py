"""Simple in Memory database for testing."""


class MockDatastore(object):
    """Mock storage."""

    def __init__(self):
        """Initialise in memory storage."""
        self._datastore = dict()

    def create(self, key, val):
        """Create a key if it doesn't exist."""
        if key not in self._datastore:
            self._datastore[key] = val
            return True
        else:
            raise KeyError(
                "Tried to create a record for an existing key"
            )

    def read(self, key):
        """Read a key."""
        if key in self._datastore:
            return self._datastore[key]
        else:
            raise KeyError(
                "Tried to read a non existing record"
            )

    def update(self, key, val):
        """Update a key if it exists."""
        if key in self._datastore:
            self._datastore[key] = val
            return True
        else:
            raise KeyError(
                "Tried to update a non existing record"
            )

    def delete(self, key):
        """Delete a key if it exists."""
        if key in self._datastore:
            del self._datastore[key]
            return True
        else:
            raise KeyError(
                "Tried to delete a non existing record"
            )

    def list(self):
        """List all keys."""
        return self._datastore


if __name__ == '__main__':
    pass
