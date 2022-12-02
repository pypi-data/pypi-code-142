def print_whats_new():
    print("""
### New features in 2.3.1
    * Added `git ws whatsnew`
        * Show similar listing as the readme for new features in different versions
    * Retry git clone
      * `git ws clone` now has retries for each git clone operation as well as a retry interval. These are hard coded for now, but will be configurable in the future
      * Defaults are:
        * retry count: 5
        * retry interval: 5 seconds
    * Support for multiple gitlab personal access tokens
      * API URL is used as an identifier.
    * EXPERIMENTAL: Support custom certificates
      * new field in the configuration under `remote`: `custom_certificate`. This is the absolute path to the file used for verification.
      * The `custom_certificate` field overrides the `insecure` field
    * EXPERIMENTAL: autocompletion for `git-ws` command
      * Does not work with `git ws`. See help (`git-ws` or `git ws`) for details.
    """)