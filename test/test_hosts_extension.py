##############################################################################
# COPYRIGHT Ericsson AB 2013
#
# The copyright to the computer program(s) herein is the property of
# Ericsson AB. The programs may be used and/or copied only with written
# permission from Ericsson AB. or in accordance with the terms and
# conditions stipulated in the agreement/contract under which the
# program(s) have been supplied.
##############################################################################


import unittest
from hosts_extension.hosts_extension import HostsExtension


class TestHostsExtension(unittest.TestCase):

    def setUp(self):
        self.ext = HostsExtension()

    def test_item_types_registered(self):
        # Assert that only extension's item types
        # are defined.
        item_types_expected = ['alias', 'alias-node-config',
            'alias-cluster-config']
        item_types = [it.item_type_id for it in
                      self.ext.define_item_types()]
        self.assertEquals(item_types_expected, item_types)

if __name__ == '__main__':
    unittest.main()
