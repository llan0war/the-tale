# coding: utf-8

from rels.django_staff import DjangoEnum


class MARKUP_METHOD(DjangoEnum):
    _records = ( ('POSTMARKUP', 0, 'bb-code'),
                 ('MARKDOWN', 1, 'markdown') )


class POST_REMOVED_BY(DjangoEnum):
    _records = ( ('AUTHOR', 0, u'удалён автором'),
                 ('THREAD_OWNER', 1, u'удалён владельцем темы'),
                 ('MODERATOR', 2, u'удалён модератором') )


class POST_STATE(DjangoEnum):
    _records = ( ('DEFAULT', 0, u'видим'),
                 ('REMOVED', 1, u'удалён') )
