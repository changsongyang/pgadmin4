##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2017, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
##########################################################################

from flask_babel import gettext
from pgadmin.browser.server_groups.servers.types import ServerType


class GPDB(ServerType):
    UTILITY_PATH_LABEL = gettext("Greenplum Database Binary Path")
    UTILITY_PATH_HELP = gettext(
        "Path to the directory containing the Greenplum Database utility"
        " programs (pg_dump, pg_restore etc)."
    )

    def instanceOf(self, ver):
        return "Greenplum Database" in ver


# Default Server Type
GPDB('gpdb', gettext("Greenplum Database"), 3)
