import stevedore
from nova.openstack.common import log as logging

LOG = logging.getLogger(__name__)

filters = stevedore.extension.ExtensionManager(
    'nova.filters.domxml',
    invoke_on_load=True,
)


def filter_domain_xml(xml,
                      instance=None,
                      context=None):

    '''Filter the XML content in 'xml' through any filters registered in
    the nova.filters.domxml namespace.'''

    revised = xml
    for filter in filters:
        LOG.debug('filtering xml with filter %s',
                  filter.name)
        revised = filter.obj.filter(revised,
                                    instance=instance,
                                    context=context
                                    )

    return revised
