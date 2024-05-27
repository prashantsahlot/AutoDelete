#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "22894706"))
API_HASH     = os.environ.get("API_HASH", "13c8f765d49c935d2ffd9152f8430f7e")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "7148114178:AAEul_2P-hgnXKd7kR3bkaz-mbCRA3_Q_f4")
SESSION      = os.environ.get("SESSION", "BQFdWHIAHwcl7Y5qLoo7lpq4nJl2dVs7vd9d2lgF4B1spD3jy2ZBLn1D7AGauSPJ8daLZkacSJsYJTkYbsds0zTOfJEUs_neAa2E5v7oU-oswxbVhlrW02bJOqKSJwwmIK9qS0JabM024PZ6icKh9kfMWBGkxFq2A9LaqNMVFMmAnF0hC5Z8gwbLaYEy1qPSYEQsiyCvBZSAtfjQ5Uf1i6TfafDybY_9pGrsMCalRWM0Zzpopllv3OKZZ0IoON4FXQfAU4BpzVLWNIn_3NaaTgu1jC3exCCq13IHgMvb5EWy4NzsQb-cozoY2xpRNnl8n3kc5Xw7ciqLBlYJw-XFPPB0Qx2_YgAAAAGG_UuIAA")
TIME         = int(os.environ.get("TIME", 10))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1002001899357").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Kingrr:4qGUNmnLghYtCQRc@cluster0.s5ezh5y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
PORT         = os.environ.get("PORT", "8080")
