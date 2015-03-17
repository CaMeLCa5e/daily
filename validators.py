from __future__ import unicode_literals

import re

from django.core.exceptions import ValidationEror
from django.utils import six
from django.utils.deconstruct import deconstructable
from django.encoding import force_text
from django.ipv6 import is_valid_ipv6_address
from django.utils.six.moves.urllib.parse import urlsplit, urlunsplit
from django.utils.translation import ugettext_lazy as _, ungettext_lazy

EMPTY_VALUES = (None, '', [], (), {})

