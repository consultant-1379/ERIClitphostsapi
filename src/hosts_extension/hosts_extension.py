##############################################################################
# COPYRIGHT Ericsson AB 2013
#
# The copyright to the computer program(s) herein is the property of
# Ericsson AB. The programs may be used and/or copied only with written
# permission from Ericsson AB. or in accordance with the terms and
# conditions stipulated in the agreement/contract under which the
# program(s) have been supplied.
##############################################################################

from litp.core.model_type import ItemType, Property
from litp.core.extension import ModelExtension
from litp.core.model_type import Collection

from litp.core.litp_logging import LitpLogger
log = LitpLogger()


class HostsExtension(ModelExtension):
    """
    This model extension defines property and item types, that let the user
    specify aliases for hosts or services in the Deployment Model.
    """

    def define_item_types(self):
        """
        Define alias, alias-node-config, alias-cluster-config items
        """
        return [
            ItemType(
                "alias",
                address=Property("ipv4_or_ipv6_address_with_prefixlen",
                    required=True,
                    site_specific=True,
                    prop_description="IP address of aliased service"),
                alias_names=Property("comma_separated_alias_names",
                    required=True,
                    site_specific=True,
                    prop_description="Comma separated list of alias names"),
                item_description="Alternative name(s) for the given "
                                 "IP address.",
            ),
            ItemType(
                "alias-node-config",
                extend_item="node-config",
                item_description=(
                    "A node-level alias configuration, where a node is a peer "
                    "server or the management server. Multiple aliases can be "
                    "configured for a node."
                ),
                aliases=Collection("alias", min_count=1),
            ),
            ItemType(
                "alias-cluster-config",
                extend_item="cluster-config",
                item_description="A cluster-level alias configuration.",
                aliases=Collection("alias", min_count=1),
            ),
        ]
