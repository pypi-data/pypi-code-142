# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['prodigy_iaa']

package_data = \
{'': ['*']}

entry_points = \
{'prodigy_recipes': ['iaa.datasets = prodigy_iaa.recipe:iaa_datasets',
                     'iaa.jsonl = prodigy_iaa.recipe:iaa_jsonl',
                     'iaa.sessions = prodigy_iaa.recipe:iaa_jsonl']}

setup_kwargs = {
    'name': 'prodigy-iaa',
    'version': '0.1.0',
    'description': '',
    'long_description': '# ✨ Prodigy - Inter-Annotator Agreement Recipes 🤝\n\nThese recipes calculate [Inter-Annotator Agreement](https://en.wikipedia.org/wiki/Inter-rater_reliability) (aka Inter-Rater Reliability) measures for use with [Prodigy](https://prodi.gy/). The measures include Percent (Simple) Agreement, Krippendorff\'s `Alpha`, and Gwet\'s `AC2`. All calculations were derived using the equations in [this paper](https://agreestat.com/papers/onkrippendorffalpha_rev10052015.pdf)[^1], and this includes tests to match the values given on the datasets referenced in that paper. \n\nCurrently this package supports IAA metrics for binary classification, multiclass classification, and multilabel (binary per label) classification. Span-based IAA measures for NER and Span Categorization will be integrated in the future.\n\nNote that you can also use the measures included here w/o directly interfacing with Prodigy, see section on [other use cases](#other-use-cases--use-outside-prodigy).\n\n## Recipes\n\nRecipes depend the source data structure:\n- `iaa.datasets` will calculate measures assuming you have multiple datasets in prodigy, one dataset per annotator\n- `iaa.sessions` will calculate measures assuming you have multiple annotators, identified typically by `_session_id`, in a single dataset\n- `iaa.jsonl` operates the same as `iaa.sessions`, but on a file exported to JSONL with `prodigy db-out`.\n\nℹ️ **Get details on each recipe\'s arguments with `prodigy <recipe> --help`**\n\n## Example\n\nIn this toy example, the command calculates agreement using dataset `my-dataset`, which is a `multiclass` problem -- meaning it\'s data is generated using the `choice` interface, exclusive choices, storing choices in the "accept" key. In this example, there are 5 total examples, 4 of them have co-incident annotations (i.e. any overlap), and 3 unique annotators.\n\n```\n$ prodigy iaa.sessions my-dataset multiclass\n\nℹ Annotation Statistics\n\nAttribute                      Value\n----------------------------   -----\nExamples                           5\nCategories                         3\nCo-Incident Examples*              4\nSingle Annotation Examples         1\nAnnotators                         3\nAvg. Annotations per Example    2.60\n\n* (>1 annotation)\n\nℹ Agreement Statistics\n\nStatistic                     Value\n--------------------------   ------\nPercent (Simple) Agreement   0.4167\nKrippendorff\'s Alpha         0.1809\nGwet\'s AC2                   0.1640\n```\n\n## Validations & Practical Use\n\nAll recipes depend on examples being hashed uniquely and stored under `_task_hash` on the example. There are other validations involved as well:\n- Checks if `view_id` is the same for all examples\n- Checks if `label` is the same for all examples\n- Checks that each annotator has not double-annotated the same `_task_hash`\n\n**If any validations fail, or your data is unique in some way, `iaa.jsonl` is the recipe you want.** Export your data, identify any issues and remedy them, and then calculate your measures on the cleaned exported data.\n\n\n## Theory\n\nThere is no single measure across all datasets to give a reasonable measurement of agreement - often times the measures are conditional on qualities of the data. The metrics included in these recipes have nice properties that make them flexible to various annotation situations: they can handle missing values (i.e. incomplete overlap), scale to any number of annotators, scale to any number of categories, and can be customized with your own weighting functions. In addition, the choice of metrics available within this package follow the recommendations in the literature[^2][^3], plus theoretical analysis[^4] demonstrating when certain metrics might be most useful.\n\nTable 13 in [this paper](https://scholar.google.com/scholar?cluster=17269958574032994585&hl=en&as_sdt=0,34&as_vis=1)[^4] highlights systematic issues with each metric. They are as follows:\n\n- **When there is _low agreement_**: Percent (Simple) Agreement can produce high scores.\n  - Imagine a binary classification problem with a very low base rate. Annotators can often agree on the negative case, but rarely agree on the positive.\n- **When there are _highly uneven sizes of categories_**: `AC2` can produce low scores, `Alpha` can produce high scores.\n- **When there are _N < 20_ co-incident annotated examples**: `Alpha` can produce high scores.\n  - You probably shouldn\'t trust _N < 100_ generally.\n- **When there are _3 or more categories_**: `AC2` can produce high scores.\n\n**Summary**: Use simple agreement and `Alpha`. If simple agreement is high, and `Alpha` is low, verify with `AC2`[^3]. In general these numbers correlate, if you\'re getting contradictory or unclear information increase the number of examples and explore your data.\n\n## Other Use-Cases / Use Outside Prodigy\n\nIf you want to calculate these measures in a custom script on your own data, you can use `from prodigy_iaa.measures import calculate_agreement`. See tests in `tests/test_measures.py` for an example. The docstrings for each function should indicate the expected data structures.\n\nYou could also use this, for example, to print out some nice output during an `update` callback and get annotation statistics as each user submits examples.\n\nIf you want to calcualte more precise statistics, e.g. comparing two annotators pairwise, you could write a script to do that as well with these existing functions.\n\n\n## Tests\n\nTests require a working version of `prodigy`, so they are not run in CI and must be run locally. \n## References\n\n\n[^1]: K. L. Gwet, “On Krippendorff’s Alpha Coefficient,” p. 16, 2015.\n[^2]: J. Lovejoy, B. R. Watson, S. Lacy, and D. Riffe, “Three Decades of Reliability in Communication Content Analyses: Reporting of Reliability Statistics and Coefficient Levels in Three Top Journals,” p. 44.\n[^3]: S. Lacy, B. R. Watson, D. Riffe, and J. Lovejoy, “Issues and Best Practices in Content Analysis,” Journalism & Mass Communication Quarterly, vol. 92, no. 4, pp. 791–811, Dec. 2015, doi: 10.1177/1077699015607338.\n[^4]: X. Zhao, J. S. Liu, and K. Deng, “Assumptions Behind Intercoder Reliability Indices,” Communication Yearbook, p. 83.\n',
    'author': 'Peter Baumgartner',
    'author_email': '5107405+pmbaumgartner@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
