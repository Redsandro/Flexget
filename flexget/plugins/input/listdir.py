"""Plugin for filesystem tasks."""
from __future__ import unicode_literals, division, absolute_import
import os
import logging
from flexget.plugin import register_plugin
from flexget.entry import Entry

log = logging.getLogger('listdir')


class Listdir(object):
    """
    Uses local path content as an input.

    Example::

      listdir: /storage/movies/
    """

    def validator(self):
        from flexget import validator
        root = validator.factory()
        root.accept('path')
        bundle = root.accept('list')
        bundle.accept('path')
        return root

    def on_task_input(self, task, config):
        # If only a single path is passed turn it into a 1 element list
        if isinstance(config, basestring):
            config = [config]
        entries = []
        for path in config:
            path = os.path.expanduser(path)
            for name in os.listdir(unicode(path)):
                e = Entry()
                e['title'] = name
                filepath = os.path.join(path, name)
                # Windows paths need an extra / preceded to them
                if not filepath.startswith('/'):
                    filepath = '/' + filepath
                e['url'] = 'file://%s' % filepath
                e['location'] = os.path.join(path, name)
                e['filename'] = name
                entries.append(e)
        return entries


register_plugin(Listdir, 'listdir', api_ver=2)
