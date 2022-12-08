# api usage helpers
apidocs = {}

# selection field combinations
apidocs['examples'] = [
    ['user', 'limit'],
    ['tags', 'type', 'limit'],
    ['playlist'],
    ['remixes', 'limit'],
    ['lic', 'search', 'limit', 'search_type'],
]

# field value descriptions
apidocs['values'] = {}
apidocs['values']['lic'] = {
    "by": "Attribution",
    "nc": "NonCommercial",
    "sa": "Share-Alike",
    "nod": "NoDerives",
    "byncsa": "NonCommercial ShareAlike",
    "byncnd": "NonCommercial NoDerives",
    "s": "Sampling",
    "splus": "Sampling+",
    "ncsplus": "NonCommercial Sampling+",
    "pd": "Public Domain"
}

# allowed paramaters
apidocs['parameters'] = {
    # "beforeu": {"desc": "Unix time", "val": [], "type": []},
    # "befored": {"desc": "Date string (see php's strtodate)", "val": [], "type": []},
    # "chop": {"desc": "Several of the embedding HTML templates will chop long names to this value.", "val": [], "type": []},
    "collab": {"desc": "Return files belonging to a given collaboration project."
                       " Value is a numeric id of the project.", "val": [], "type": []},
    # "datasource": {"desc": "Set to topics with format=rss to get topics related feeds. (See type parameter.)", "val": [], "type": []},
    # "dataview": {"desc": "(see Data View section)", "val": [], "type": []},
    # "format": {"desc": "(see Formats section)", "val": [], "type": []},
    "ids": {"desc": "Comma-separated numeric ids", "val": [], "type": []},
    "lic": {"desc": "(See License Values)", "val": [], "type": []},
    "limit": {"desc": "This will tell the QAPI to return no more than a certain number of records. "
                      "Valid values are: numeric value, page, feed, query, default", "val": [], "type": []},
    # "match": {"desc": "Template specific, for example "
    #                   "t=review_upload&match=%upload_id% and t=topic_thread&match=%thread_id%", "val": [], "type": []},
    # "nosort": {"desc": "Used with param ids to honor the order of ids passed in.", "val": [], "type": []},
    # "offset": {"desc": "Combine with limit to page through results.", "val": [], "type": []},
    # "paging": {"desc": "Used with formats page and html to include prev/next buttons. Valid values are on and off "
    #                    "The default for page is on, for html is off", "val": [], "type": []},
    "playlist": {"desc": "Return records belonging to a specific playlist. Value is the numeric playlist id",
                 "val": [], "type": []},
    # "rand": {"desc": "Set to 1 to return records in a random order", "val": [], "type": []},
    # "reccby": {"desc": "Return records ecommended by a user at the site. Value is the login name of the user.", "val": [], "type": []},
    "remixes": {"desc": "Request for remixes of a given upload id", "val": [], "type": []},
    "remixesof": {"desc": "Request for remixes of a given user (value is login name)", "val": [], "type": []},
    # "remixmax": {"desc": "Uploads that have been remixed no more than remixmax times", "val": [], "type": []},
    # "remixmin": {"desc": "Uploads that have been rmeixed no less than remixmin times", "val": [], "type": []},
    # "reqtags": {"desc": "These tags must be included in upload", "val": [], "type": []},
    # "reviewee": {"desc": "Review topics authored by reviewee", "val": [], "type": []},
    # "score": {"desc": "Uploads that have at least score number of ratings", "val": [], "type": []},
    # "search": {"desc": "Search for text words or a phrase.", "val": [], "type": []},
    # "search_type": {"desc": "Valid values are match for an exact phrase, any for matches of any of the terms, "
    #                         "all for matches of all of the terms.", "val": [], "type": []},
    # "sinceu": {"desc": "Unix time", "val": [], "type": []},
    # "sinced": {"desc": "Date string (see php's strtodate)", "val": [], "type": []},
    # "sort": {"desc": "(See Valid Sorts)", "val": [], "type": []},
    "ord": {"desc": "Order of score. Valid values are ASC and DESC.", "val": [], "type": []},
    "sources": {"desc": "Sources of a given remix", "val": [], "type": []},
    "tags": {"desc": "Return uploads with the tags (separated by '+'). For multiple tags set the type parameter to "
                     "either all to see records with all tags or any to see "
                     "records that have any of the tags.", "val": [], "type": []},
    # "template": {"desc": "(See Templates Appendix)", "val": [], "type": []},
    # "thread": {"desc": "Used with forum related templates to specify the "
    #                    "topics associated with a given thread.", "val": [], "type": []},
    # "title": {"desc": "Used with format=page and some feed formats to display a title at the top of the page"
    #                   " or XML file.", "val": [], "type": []},
    "type": {"desc": "When data source is uploads this is a modifier for the tags parameter. When data source is"
                     " topics this restricts the returning records to topics of that type (e.g. forum, review, "
                     "artist_qa, etc.) The exact types available are site specific.", "val": [], "type": []},
    "user": {"desc": "Return records that were uploaded by a certain user. "
                     "Value is the login name.", "val": [], "type": []}
}
