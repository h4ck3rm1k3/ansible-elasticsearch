# test the jina templateo

from ansible.utils import template
#import ansible.utils as utils

basedir="templates"
term = "elasticsearch.yml.j2"

inject = {
    'elasticsearch_cluster_name' : 'mycluster',
    'elasticsearch_bind_host' : 'myhost',
    'elasticsearch_tcp_port' : '9300',
    'elasticsearch_http_port' : '9200',

}
x = template.template_from_file(basedir, term, inject)

print x
