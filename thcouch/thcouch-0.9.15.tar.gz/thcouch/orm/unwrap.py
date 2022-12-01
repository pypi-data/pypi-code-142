__all__ = ['CouchDocument', 'CouchAttachment', 'CouchClient', 'CouchDatabase', 'CouchIndex']

import thcouch.orm

from thresult import auto_unwrap


CouchDocument = auto_unwrap(thcouch.orm.CouchDocument)

CouchAttachment = auto_unwrap(thcouch.orm.CouchAttachment)

CouchClient = auto_unwrap(thcouch.orm.CouchClient)
CouchDatabase = auto_unwrap(thcouch.orm.CouchDatabase)
CouchIndex = auto_unwrap(thcouch.orm.CouchIndex)
