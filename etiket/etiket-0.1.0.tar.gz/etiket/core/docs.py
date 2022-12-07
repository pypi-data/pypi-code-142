from etiket.core.config import settings

title = settings.ETIKET_NAME

tags_metadata = [
    {
        "name": "access",
        "description": "Authenticate to get access and refresh tokens. Possible to refresh token when access token has expired.",
    },
    {"name": "datasets", "description": "Manage datasets"},
    {"name": "files", "description": "Manage and download files in datasets"},
    {"name": "collections", "description": "Organize datasets into collections."},
    {
        "name": "meta",
        "description": "Annotate datasets with JSON metadata. Currently, key-value pairs are allowed where values can be lists of strings.",
    },
    {"name": "scope", "description": "Manage scopes and users within scopes"},
    {"name": "user", "description": "Manage users"},
    {
        "name": "tus",
        "description": "Resumable upload of files in datasets. Protocol as described by tus.io is used.",
    },
]


description = """
etiket is a dataset management service developed at QuTech to manage scientific dataset from experiments and simulations performed at QuTech.
It serves as a common data layer for various research labs which makes datasets easier to manage (irrespective of file size), provenance of datasets is less error prone and is useful foundation for other applications.

## Datasets

Datasets are the primary abstraction for etiket and are a set of data files which are intrinsically linked.
A dataset is uniquely identified by a scope and a UUID and can be described with additional metadata:
- name, a human understandable alphanumerical identifier for the dataset
- description
- administrative metadata such as dates created and modified
- ranking, which can normal, favourite or suppressed indicating how valuable a dataset is deemed
- additional user defined metadata in JSON format

A dataset is always part of a scope.
Datasets can be grouped into one or multiple collections.

No one can delete datasets, users can only suppress datasets if they don't want them to show up in queries by default.
Files of datasets can only be deleted if they are not uploaded yet.


## Collections

Collections can contain one or more datasets.
This can be used to group datasets used for a certain research initiative, presentation at a conference, a paper or for any reason why a user wants to group a certain number of datasets.
They resemble folders with the distinction that they are not hierarchical, but act more like a descriptive tag.
A dataset can be part of multiple collections (whereas files/folders can always only be part of a single folder)
Collections have a name, and a description, can not be deleted, need to be part of a scope, can not group other collections and can not be moved between scopes.
Collections are uniquely indentified by scope and a name.


## Files

Data is physically stored in files; files are also the smallest operational unit of data in etiket.
Sub-file operations are currently not possible.
Files are always grouped into datasets (a named set of files) and can only ever be part of one dataset.
Files can have a tag associated to describe the type of file:
- raw file which comes 'directly' from the measurement or simulation.
- derived file which is typically derived from a raw file
- source code used during acquisition or analysis of data
- configuration file necessary for a source code file for acquisition or analysis
- preview file which can either be a plot or figure which graphically represents (a part of) the dataset.
Files (will) have a status tag indicating whether the file is already uploaded:
- 'pending' means that the is created in the database, but is not (yet) uploaded.
- 'available' means the file is created and uploaded correctly

Upload and download of files need to be requested via the API, but are subsequently handled directly the with the storage facility. 


## Metadata of datasets

Additional metadata can be added to datasets in the form of JSON fields.
Dataset metadata is limited to a dictionary key/value pairs where keys are strings, and values can be a string or a list of strings.
The keys and values can be freely chosen within limits (2>length>20)


## Scope and user administration

Scopes are the administrative entity grouping users together with datasets (and files, collections, metadata).
Scopes are research initiatives that typically have an end date.
Only users part of a scope can add resources (collections, datasets, files, metadata etc) to that scope.
Users can be part of one or multiple scopes.
Only if users are part of a scope can they alter resources from said scope
Users part of scope X can invite other existing users to scope X
Users can not create other users, only the admin can create new users for now. 
"""
