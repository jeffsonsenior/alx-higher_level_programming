#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of an objects available atbts."""
    return (dir(obj))

