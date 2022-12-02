search_keys = { 
    "keyword"           : "",

    # View
    # URL param: view
    # values: simple, detailed
    # Titles: Simple, Detailed Search with mask
    "view"              : "simple",

    # The number of pages
    # URL param: res
    "page_num"          : 1,

    # Search in fields
    # URL param: column
    # values: def, title, author, series, publisher, year, identifier, language, md5, tags, extension
    # Titles: The column set default, Title, Author(s), Series, Publisher, Year, ISBN, Language, MD5, Tags, Extension
    "search_field"      : "title",

    # Sort by
    # URL param: sort
    # values: id, author, title, publisher, year, pages, language, filesize, extension
    # Titles: ID, Author(s), Title, Publisher, Year, Pages, Language, Size, Extension
    "sort"              : "year",

    # Sort mode
    # URL param: sortmode
    # values: ASC, DESC
    "sortmode"          : "DESC",

    # Download path
    "download"          : ""
}

param_values = {
    "view": ["simple", "detailed"],
    "page_num": [25, 50, 100],
    "search_field": ["def", "title", "author", "series", "publisher", "year", "identifier", "language", "md5", "tags", "extension"],
    "sort": ["id", "author", "title", "publisher", "year", "pages", "language", "filesize", "extension"],
    "sortmode": ["ASC", "DESC"]
}