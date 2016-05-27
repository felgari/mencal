# -*- coding: utf-8 -*-

# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

# Constants.

# Length of the sequence of operations
MENCAL_LENGTH = 5

# Operations to use: SUB, SUB, MULT, DIV.
MENCAL_OPS = 3

# Size of the numbers to take into account for each operation.
MENCAL_SIZE = [ 2, 1, 1, 1 ]

# Delay between operations.
MENCAL_DELAY = [ 1, 2, 3, 4 ]

# String to show for each operation.
MENCAL_OP_STR = [ '+', '-', '*', '/' ]
