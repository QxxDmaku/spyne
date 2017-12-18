
#
# spyne - Copyright (C) Spyne contributors.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#

"""The ``spyne.interface`` package contains implementations of various interface
definition document standards along with the
:class:`spyne.interface.Interface` class which holds all the information needed
to generate those documents.
"""

from __future__ import print_function

from spyne.interface._base import Interface
from spyne.interface._base import InterfaceDocumentBase
from spyne.interface._base import AllYourInterfaceDocuments

try:
    from spyne.interface.wsdl.wsdl11 import Wsdl11
    HAS_WSDL = True
except ImportError as e:
    if e.args in ('No module named lxml', "No module named 'lxml'"):
        HAS_WSDL = False
    else:
        raise
