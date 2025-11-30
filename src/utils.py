# -*- coding: utf-8 -*-
"""Utility functions"""

def validate_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    try:
        return all(0 <= int(p) <= 255 for p in parts)
    except:
        return False

def generate_filename(prefix, ext):
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_7451_{timestamp}.{ext}"
