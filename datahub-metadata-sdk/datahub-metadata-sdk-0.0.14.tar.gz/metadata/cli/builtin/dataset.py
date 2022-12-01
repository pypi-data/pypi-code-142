# -*- coding: utf-8 -*-

import os
from os.path import dirname, join, exists
from argparse import Namespace
from typing import Mapping, Any
from jsonpath_ng import parse

from metadata.utils.format import gen_tree_files, dict2json, dict2yaml
from metadata.entity.dataset import Dataset
from metadata.context import MetadataContext
from metadata.cli.builtin.entity import IEntity
from metadata.client.client import Client


class IDataset(IEntity):

    name = 'dataset'
    candidate_names = ['ds']
    container_type = 'element'

    @classmethod
    def get_property_keys(cls):
        return super().get_property_keys() + ['uri']

    @classmethod
    def get_one_func(cls, client: Client):
        return client.get_dataset

    @classmethod
    def get_multi_func(cls, client: Client):
        def wraps(*args, **kwargs):
            return [client.get_dataset(urn) for urn in client.get_datasets_by_facts(*args, **kwargs)]
        return wraps

    @classmethod
    def delete_one_func(cls, client: Client):
        return client.delete_dataset

    @classmethod
    def create_one(cls, client: Client, dt: Mapping[str, Any]):
        dt.pop('entity_type', None)
        dataset = Dataset(**dt)
        return client.create_dataset(dataset)

    @classmethod
    def update_one(cls, client: Client, dt: Mapping[str, Any]):
        dataset = Dataset(**dt)
        return client.update_dataset(dataset)

    @classmethod
    def do_download(cls, context: MetadataContext, args: Namespace, urn: str):
        dest = args.dest
        if not exists(dest):
            os.makedirs(dest)
        client = context.client
        client.download_dataset(urn, dest, args.sub_paths)

    @classmethod
    def do_upload(cls, context: MetadataContext, args: Namespace):
        client = context.client
        uri = client.upload_artifact(args.storage_prefix, args.path_prefix, args.file)
        sc = context.storage_client
        urn = Dataset.gen_urn(context, sc.get_name(), args.name)
        entity = Dataset(
                urn=urn,
                display_name=args.display_name,
                uri=uri,
        )
        client.create_dataset(entity)
        print(f'Uploaded as {entity}')

    @classmethod
    def do_upload_partial(cls, context: MetadataContext, args: Namespace):
        client = context.client
        dataset = client.get_dataset(args.urn)
        client.upload_artifact(dataset.uri, args.path_prefix, args.file)

    @classmethod
    def do_describe(cls, context: MetadataContext, args: Namespace, urn: str):
        cilent = context.client
        dataset = cilent.get_dataset(urn)
        paths = context.storage_client.list(dataset.uri, recursive=True)
        if not paths:
            print('[]')
            return
        paths = [i[len(dataset.uri) + 1:] for i in paths]
        files = gen_tree_files(paths)
        if args.output and args.output == 'yaml':
            print(dict2yaml(files))
        else:
            if args.jsonpath:
                jsonpath_expression = parse(args.jsonpath)
                for match in jsonpath_expression.find(files):
                    print(match.value)
            else:
                print(dict2json(files))