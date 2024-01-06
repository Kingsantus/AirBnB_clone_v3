#!/usr/bin/python3
"""Getting the information of states using api"""
def to_dict(obj):
    return obj.to_dict() if hasattr(obj, 'to_dict') else None
