# -*- coding: utf-8 -*-
"""Release data for the IPython-extensions project."""

# This is the only place were the release number must be adjusted
_version_major = 0
_version_minor = 1
_version_patch = 0
_version_extra = 'dev'
# _version_extra = 'rc1'
_version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor, _version_patch]

__version__ = '.'.join(map(str, _ver))
if _version_extra:
    __version__ = __version__ + '-' + _version_extra

version_info = (_version_major, _version_minor, _version_patch, _version_extra)

