'''
## CDK Graph (`@aws-prototyping-sdk/cdk-graph`)

![experimental](https://img.shields.io/badge/stability-experimental-orange.svg)
![alpha](https://img.shields.io/badge/version-alpha-red.svg)
[![API Documetnation](https://img.shields.io/badge/view-API_Documentation-blue.svg)](https://aws.github.io/aws-prototyping-sdk/typescript/cdk-graph/index.html)
[![Source Code](https://img.shields.io/badge/view-Source_Code-blue.svg)](https://github.com/aws/aws-prototyping-sdk/tree/mainline/packages/cdk-graph)

> More comprehensive documentation to come as this package stabilizes

This package is the core framework for supporting additional cdk based automation and tooling, such as diagraming, cost modeling, security and compliance, in a holistic and comprehensive way.

This package provides the following functionality:

1. Synthesizes a serialized graph (nodes and edges) from CDK source code.
2. Provides runtime interface for interacting with the graph (in-memory database-like graph store).
3. Provides plugin framework for additional tooling to utilize and extend the graph.

The goal of this framework is to enable bespoke tooling to be built without having to first traverse the CDK Tree and Metadata to build a graph. Projects like [cdk-dia](https://github.com/pistazie/cdk-dia) generate a bespoke in-memory graph that is then utilized to generate diagrams; while the diagram generation is the core value it must first have a graph to act upon and currently is required to generate this undifferentiated graph to provide its diagrams. By standardizing on the graph interface necessary to build complex tooling, we can more rapidly build new tooling that focuses on its core value.

---


### Available Plugins

| Name | Description | Screenshot | Links |
|--- | --- | --- | --- |
| **Diagram** | Generate cloud infrastructure diagrams from cdk graph | <img src="https://github.com/aws/aws-prototyping-sdk/blob/mainline/packages/cdk-graph-plugin-diagram/docs/examples/default.png?raw=true" style="max-width:200px;max-height:200px" /> | [![API Documetnation](https://img.shields.io/badge/view-API_Documentation-blue.svg)](https://aws.github.io/aws-prototyping-sdk/typescript/cdk-graph/index.html) [![Source Code](https://img.shields.io/badge/view-Source_Code-blue.svg)](https://github.com/aws/aws-prototyping-sdk/tree/mainline/packages/cdk-graph) |

---


### Quick Start

#### Instrument CDK App with CdkGraph

```python
#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { MyStack } from "../lib/my-stack";

import { CdkGraph } from "@aws-prototyping-sdk/cdk-graph";

const app = new cdk.App();
new MyStack(app, "MyStack");

// Add CdkGraph after other construct added to app
new CdkGraph(app);
```

#### Using Plugins

```python
#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { MyStack } from "../lib/my-stack";

import { CdkGraph } from "@aws-prototyping-sdk/cdk-graph";
import { ExamplePlugin } from "@aws-prototyping-sdk/cdk-graph-plugin-example"; // does not exist, just example

const app = new cdk.App();
new MyStack(app, "MyStack");

// Add CdkGraph after other construct added to app
new CdkGraph(app, {
  plugins: [new ExamplePlugin()],
});
```

---


### Config

Configuration is supported through the `.cdkgraphrc.js` and depending on the plugin, through passing config to the plugin instance.

Config precedence follows 1) defaults, 2) cdkgraphrc, 3) instance.

```js
// .cdkgraphrc.js
module.exports = {
  // Defaults to "<cdk.out>/cdkgraph"
  outdir: "reports/graph",

  // plugin configuration
  example: {
    verbose: true,
    reportType: "csv",
  },
};
```

```python
#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { MyStack } from "../lib/my-stack";

import { CdkGraph } from "@aws-prototyping-sdk/cdk-graph";
import { ExamplePlugin } from "@aws-prototyping-sdk/cdk-graph-plugin-example"; // does not exist, just example

const app = new cdk.App();
new MyStack(app, "MyStack");

// Add CdkGraph after other construct added to app
new CdkGraph(app, {
  plugins: [
    new ExamplePlugin({
      // Will override .cdkgraphrc.js value
      verbose: false,
    }),
  ],
});
```

---


### Plugin Interface

```python
/** CdkGraph **Plugin** interface */
export interface ICdkGraphPlugin {
  /** Unique identifier for this plugin */
  readonly id: string;
  /** Plugin version */
  readonly version: Version;
  /** List of plugins this plugin depends on, including optional semver version (eg: ["foo", "bar@1.2"]) */
  readonly dependencies?: string[];

  /**
   * Binds the plugin to the CdkGraph instance. Enables plugins to receive base configs.
   */
  bind: IGraphPluginBindCallback;

  /**
   * Node visitor callback for construct tree traversal. This follows IAspect.visit pattern, but the order
   * of visitor traversal in managed by the CdkGraph.
   */
  inspect?: IGraphVisitorCallback;
  /**
   * Called during CDK synthesize to generate synchronous artifacts based on the in-memory graph passed
   * to the plugin. This is called in fifo order of plugins.
   */
  synthesize?: IGraphSynthesizeCallback;
  /**
   * Generate asynchronous reports based on the graph. This is not automatically called when synthesizing CDK.
   * Developer must explicitly add `await graphInstance.report()` to the CDK bin or invoke this outside
   * of the CDK synth. In either case, the plugin receives the in-memory graph interface when invoked, as the
   * CdkGraph will deserialize the graph prior to invoking the plugin report.
   */
  report?: IGraphReportCallback;
}
```

Plugin operations are automatically invoked by CdkGraph in the order they are defined in the `plugins` property. The invocation flow of plugins follows: 1) `bind`, 2) `inspect`, 3) `synthesize`, 4) `async report`.

### Asynchronous Plugins

Some plugins may requiring performing asynchronous requests, or may make expensive operations that are best left outside of the synthesis process.

CdkGraph support asynchronous operations through the `async report()` method of plugins. However, since CDK does not support asynchronous operations during synthesis, this must be wired up a bit differently.

```python
#!/usr/bin/env node
import * as cdk from "aws-cdk-lib";
import { MyStack } from "../lib/my-stack";

import { CdkGraph } from "@aws-prototyping-sdk/cdk-graph";
import { ExampleAsyncPlugin } from "@aws-prototyping-sdk/cdk-graph-plugin-async-example"; // does not exist, just example

(async () => {
  const app = new cdk.App();
  new MyStack(app, "MyStack");

  // Add CdkGraph after other construct added to app
  const graph = new CdkGraph(app, {
    plugins: [new ExampleAsyncPlugin()],
  });

  // invokes all plugin `report()` operations asynchronously (in order they are defined in `plugins` property)
  await graph.report();
})();
```

### Example Plugin Implementation

Very basic example of implementing a plugin. Once the first actual plugins have been published this will be updated to reference those as examples.

```python
import {
  CdkGraph,
  CdkGraphContext,
  ICdkGraphPlugin,
} from "@aws-prototyping-sdk/cdk-graph";

export class CdkGraphExamplePlugin implements ICdkGraphPlugin {
  static readonly ARTIFACT_NS = "EXAMPLE";
  static readonly ID = "example";
  static readonly VERSION = "0.0.0";

  get id(): string {
    return CdkGraphDiagramPlugin.ID;
  }
  get version(): string {
    return CdkGraphDiagramPlugin.VERSION;
  }

  readonly dependencies?: string[] = [];

  /** @internal */
  private _graph?: CdkGraph;

  bind(graph: CdkGraph): void {
    this._graph = graph;
  }

  synthesize(context: CdkGraphContext): void {
    const pluginConfig = this.config as Required<IPluginConfig>;

    // Get counts of all resources
    const cfnResourceCounts = context.store.counts.cfnResources;

    // Write plugin artifact
    context.writeArtifact(
      this,
      "EXAMPLE",
      "example.json",
      JSON.stringify(cfnResourceCounts, null, 2)
    );
  }

  async report(context: CdkGraphContext): void {
    // perform async operation here utilizing graph store
    const cfnResourceCounts = context.store.counts.cfnResources;
    const fetchedData = await fetch("https://example.com/data", {
      method: "POST",
      body: JSON.stringify(cfnResourceCounts),
    });

    // Write plugin artifact for fetched data
    context.writeArtifact(
      this,
      "EXAMPLE:FETCHED",
      "example-fetched.json",
      JSON.stringify(fetchedData, null, 2)
    );
  }
}
```

### Path to Stability

The below is a rough checklist of task necessary to elevate this from experimental to stable.

* [ ] Dynamic versioning and Semver enforcement (store, plugins, etc)
* [ ] Support running `async report()` method outside of CDK synthesis process
* [ ] Find alternative synthesis solution that doesn't utilize CDK internals
* [ ] Support custom Nodes and Edges
* [ ] Improve logging, bookkeeping, and debugging
* [ ] Implement store upgrade solution
* [ ] Battle test the implementation against several plugins
* [ ] Battle test the implementation in all target languages (currently tested in Typescript, but vended in all PDK supported languages)
* [ ] Receive community feedback to validate approach
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import constructs
from .graph import (
    IEdgePredicate as _IEdgePredicate_786afb09,
    INodePredicate as _INodePredicate_1dc8755a,
    Node as _Node_ddadac9d,
    Store as _Store_6b467276,
)
from .serialized_graph import (
    Attributes as _Attributes_b47661e3,
    Entity as _Entity_794b3e11,
    PlainObject as _PlainObject_c976ebcc,
    Tags as _Tags_cf30c388,
)


@jsii.enum(jsii_type="@aws-prototyping-sdk/cdk-graph.CdkConstructIds")
class CdkConstructIds(enum.Enum):
    '''(experimental) Common cdk construct ids.

    :stability: experimental
    '''

    DEFAULT = "DEFAULT"
    '''
    :stability: experimental
    '''
    RESOURCE = "RESOURCE"
    '''
    :stability: experimental
    '''
    EXPORTS = "EXPORTS"
    '''
    :stability: experimental
    '''


class CdkGraph(
    constructs.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.CdkGraph",
):
    '''(experimental) CdkGraph construct is the cdk-graph framework controller that is responsible for computing the graph, storing serialized graph, and instrumenting plugins per the plugin contract.

    :stability: experimental
    '''

    def __init__(
        self,
        root: constructs.Construct,
        props: typing.Optional["ICdkGraphProps"] = None,
    ) -> None:
        '''
        :param root: -
        :param props: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                root: constructs.Construct,
                props: typing.Optional[ICdkGraphProps] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument root", value=root, expected_type=type_hints["root"])
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        jsii.create(self.__class__, self, [root, props])

    @jsii.member(jsii_name="report")
    def report(self) -> None:
        '''(experimental) Asynchronous report generation. This operation enables running expensive and non-synchronous report generation by plugins post synthesis.

        If a given plugin requires performing asynchronous operations or is general expensive, it should
        utilize ``report`` rather than ``synthesize``.

        :stability: experimental
        '''
        return typing.cast(None, jsii.ainvoke(self, "report", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ID")
    def ID(cls) -> builtins.str:
        '''(experimental) Fixed CdkGraph construct id.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ID"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VERSION")
    def VERSION(cls) -> builtins.str:
        '''(experimental) Current CdkGraph semantic version.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VERSION"))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> "CdkGraphConfig":
        '''(experimental) Config.

        :stability: experimental
        '''
        return typing.cast("CdkGraphConfig", jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="plugins")
    def plugins(self) -> typing.List["ICdkGraphPlugin"]:
        '''(experimental) List of plugins registered with this instance.

        :stability: experimental
        '''
        return typing.cast(typing.List["ICdkGraphPlugin"], jsii.get(self, "plugins"))

    @builtins.property
    @jsii.member(jsii_name="root")
    def root(self) -> constructs.Construct:
        '''
        :stability: experimental
        '''
        return typing.cast(constructs.Construct, jsii.get(self, "root"))

    @builtins.property
    @jsii.member(jsii_name="graphContext")
    def graph_context(self) -> typing.Optional["CdkGraphContext"]:
        '''(experimental) Get the context for the graph instance.

        This will be ``undefined`` before construct synthesis has initiated.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["CdkGraphContext"], jsii.get(self, "graphContext"))


@jsii.data_type(
    jsii_type="@aws-prototyping-sdk/cdk-graph.CdkGraphArtifact",
    jsii_struct_bases=[],
    name_mapping={
        "filename": "filename",
        "filepath": "filepath",
        "id": "id",
        "source": "source",
        "description": "description",
    },
)
class CdkGraphArtifact:
    def __init__(
        self,
        *,
        filename: builtins.str,
        filepath: builtins.str,
        id: builtins.str,
        source: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) CdkGraph artifact definition.

        :param filename: (experimental) Filename of the artifact.
        :param filepath: (experimental) Full path where artifact is stored.
        :param id: (experimental) The unique type of the artifact.
        :param source: (experimental) The source of the artifact (such as plugin, or core system, etc).
        :param description: (experimental) Description of artifact.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                filename: builtins.str,
                filepath: builtins.str,
                id: builtins.str,
                source: builtins.str,
                description: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
            check_type(argname="argument filepath", value=filepath, expected_type=type_hints["filepath"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "filename": filename,
            "filepath": filepath,
            "id": id,
            "source": source,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def filename(self) -> builtins.str:
        '''(experimental) Filename of the artifact.

        :stability: experimental
        '''
        result = self._values.get("filename")
        assert result is not None, "Required property 'filename' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filepath(self) -> builtins.str:
        '''(experimental) Full path where artifact is stored.

        :stability: experimental
        '''
        result = self._values.get("filepath")
        assert result is not None, "Required property 'filepath' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> builtins.str:
        '''(experimental) The unique type of the artifact.

        :stability: experimental
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''(experimental) The source of the artifact (such as plugin, or core system, etc).

        :stability: experimental
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''(experimental) Description of artifact.

        :stability: experimental
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdkGraphArtifact(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-prototyping-sdk/cdk-graph.CdkGraphArtifacts")
class CdkGraphArtifacts(enum.Enum):
    '''(experimental) CdkGraph core artifacts.

    :stability: experimental
    '''

    GRAPH_METADATA = "GRAPH_METADATA"
    '''
    :stability: experimental
    '''
    GRAPH = "GRAPH"
    '''
    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="@aws-prototyping-sdk/cdk-graph.CdkGraphConfig",
    jsii_struct_bases=[],
    name_mapping={"outdir": "outdir"},
)
class CdkGraphConfig:
    def __init__(self, *, outdir: typing.Optional[builtins.str] = None) -> None:
        '''(experimental) CdkGraph configuration definition.

        :param outdir: (experimental) Directory where artifacts are written. The key ``<cdk.out>`` will be replaced with the synthesizer cdk ``outdir``. Relative paths not prefixed with ``<cdk.out>`` will be relative to ``process.cwd`` Default: "<cdk.out>/cdkgraph"

        :stability: experimental
        '''
        if __debug__:
            def stub(*, outdir: typing.Optional[builtins.str] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument outdir", value=outdir, expected_type=type_hints["outdir"])
        self._values: typing.Dict[str, typing.Any] = {}
        if outdir is not None:
            self._values["outdir"] = outdir

    @builtins.property
    def outdir(self) -> typing.Optional[builtins.str]:
        '''(experimental) Directory where artifacts are written.

        The key ``<cdk.out>`` will be replaced with the synthesizer cdk ``outdir``.

        Relative paths not prefixed with ``<cdk.out>`` will be relative to ``process.cwd``

        :default: "<cdk.out>/cdkgraph"

        :stability: experimental
        '''
        result = self._values.get("outdir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdkGraphConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdkGraphContext(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph.CdkGraphContext",
):
    '''(experimental) CdkGraph context.

    :stability: experimental
    '''

    def __init__(self, store: _Store_6b467276, outdir: builtins.str) -> None:
        '''
        :param store: -
        :param outdir: -

        :stability: experimental
        '''
        if __debug__:
            def stub(store: _Store_6b467276, outdir: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument store", value=store, expected_type=type_hints["store"])
            check_type(argname="argument outdir", value=outdir, expected_type=type_hints["outdir"])
        jsii.create(self.__class__, self, [store, outdir])

    @jsii.member(jsii_name="getArtifact")
    def get_artifact(self, id: builtins.str) -> CdkGraphArtifact:
        '''(experimental) Get CdkGraph artifact by id.

        :param id: -

        :stability: experimental
        :throws: Error is artifact does not exist
        '''
        if __debug__:
            def stub(id: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        return typing.cast(CdkGraphArtifact, jsii.invoke(self, "getArtifact", [id]))

    @jsii.member(jsii_name="hasArtifactFile")
    def has_artifact_file(self, filename: builtins.str) -> builtins.bool:
        '''(experimental) Indicates if context has an artifact with *filename* defined.

        :param filename: -

        :stability: experimental
        '''
        if __debug__:
            def stub(filename: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
        return typing.cast(builtins.bool, jsii.invoke(self, "hasArtifactFile", [filename]))

    @jsii.member(jsii_name="logArtifact")
    def log_artifact(
        self,
        source: typing.Union[CdkGraph, "ICdkGraphPlugin"],
        id: builtins.str,
        filepath: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> CdkGraphArtifact:
        '''(experimental) Logs an artifact entry.

        In general this should not be called directly, as ``writeArtifact`` should be utilized
        to perform writing and logging artifacts. However some plugins utilize other tools that generate the artifacts,
        in which case the plugin would call this method to log the entry.

        :param source: The source of the artifact, such as the name of plugin.
        :param id: Unique id of the artifact.
        :param filepath: Full path where the artifact is stored.
        :param description: Description of the artifact.

        :stability: experimental
        :throws: Error is artifact id or filename already exists
        '''
        if __debug__:
            def stub(
                source: typing.Union[CdkGraph, ICdkGraphPlugin],
                id: builtins.str,
                filepath: builtins.str,
                description: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument filepath", value=filepath, expected_type=type_hints["filepath"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        return typing.cast(CdkGraphArtifact, jsii.invoke(self, "logArtifact", [source, id, filepath, description]))

    @jsii.member(jsii_name="writeArtifact")
    def write_artifact(
        self,
        source: typing.Union[CdkGraph, "ICdkGraphPlugin"],
        id: builtins.str,
        filename: builtins.str,
        data: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> CdkGraphArtifact:
        '''(experimental) Writes artifact data to outdir and logs the entry.

        :param source: The source of the artifact, such as the name of plugin.
        :param id: Unique id of the artifact.
        :param filename: Relative name of the file.
        :param data: -
        :param description: Description of the artifact.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                source: typing.Union[CdkGraph, ICdkGraphPlugin],
                id: builtins.str,
                filename: builtins.str,
                data: builtins.str,
                description: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument filename", value=filename, expected_type=type_hints["filename"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        return typing.cast(CdkGraphArtifact, jsii.invoke(self, "writeArtifact", [source, id, filename, data, description]))

    @builtins.property
    @jsii.member(jsii_name="artifacts")
    def artifacts(self) -> typing.Mapping[builtins.str, CdkGraphArtifact]:
        '''(experimental) Get record of all graph artifacts keyed by artifact id.

        :stability: experimental
        '''
        return typing.cast(typing.Mapping[builtins.str, CdkGraphArtifact], jsii.get(self, "artifacts"))

    @builtins.property
    @jsii.member(jsii_name="graphJson")
    def graph_json(self) -> CdkGraphArtifact:
        '''(experimental) Get CdkGraph core ``graph.json`` artifact.

        :stability: experimental
        '''
        return typing.cast(CdkGraphArtifact, jsii.get(self, "graphJson"))

    @builtins.property
    @jsii.member(jsii_name="outdir")
    def outdir(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "outdir"))

    @builtins.property
    @jsii.member(jsii_name="store")
    def store(self) -> _Store_6b467276:
        '''
        :stability: experimental
        '''
        return typing.cast(_Store_6b467276, jsii.get(self, "store"))


@jsii.enum(jsii_type="@aws-prototyping-sdk/cdk-graph.CfnAttributesEnum")
class CfnAttributesEnum(enum.Enum):
    '''(experimental) Common cfn attribute keys.

    :stability: experimental
    '''

    TYPE = "TYPE"
    '''
    :stability: experimental
    '''
    PROPS = "PROPS"
    '''
    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="@aws-prototyping-sdk/cdk-graph.ConstructInfo",
    jsii_struct_bases=[],
    name_mapping={"fqn": "fqn", "version": "version"},
)
class ConstructInfo:
    def __init__(self, *, fqn: builtins.str, version: builtins.str) -> None:
        '''(experimental) Source information on a construct (class fqn and version).

        :param fqn: 
        :param version: 

        :see: https://github.com/aws/aws-cdk/blob/cea1039e3664fdfa89c6f00cdaeb1a0185a12678/packages/%40aws-cdk/core/lib/private/runtime-info.ts#L22
        :stability: experimental
        '''
        if __debug__:
            def stub(*, fqn: builtins.str, version: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument fqn", value=fqn, expected_type=type_hints["fqn"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {
            "fqn": fqn,
            "version": version,
        }

    @builtins.property
    def fqn(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("fqn")
        assert result is not None, "Required property 'fqn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConstructInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-prototyping-sdk/cdk-graph.ConstructInfoFqnEnum")
class ConstructInfoFqnEnum(enum.Enum):
    '''(experimental) Commonly used cdk construct info fqn (jsii fully-qualified ids).

    :stability: experimental
    '''

    APP = "APP"
    '''
    :stability: experimental
    '''
    STAGE = "STAGE"
    '''
    :stability: experimental
    '''
    STACK = "STACK"
    '''
    :stability: experimental
    '''
    NESTED_STACK = "NESTED_STACK"
    '''
    :stability: experimental
    '''
    CFN_STACK = "CFN_STACK"
    '''
    :stability: experimental
    '''
    CFN_OUTPUT = "CFN_OUTPUT"
    '''
    :stability: experimental
    '''
    CFN_PARAMETER = "CFN_PARAMETER"
    '''
    :stability: experimental
    '''
    CUSTOM_RESOURCE = "CUSTOM_RESOURCE"
    '''
    :stability: experimental
    '''
    AWS_CUSTOM_RESOURCE = "AWS_CUSTOM_RESOURCE"
    '''
    :stability: experimental
    '''
    CUSTOM_RESOURCE_PROVIDER = "CUSTOM_RESOURCE_PROVIDER"
    '''
    :stability: experimental
    '''
    CUSTOM_RESOURCE_PROVIDER_2 = "CUSTOM_RESOURCE_PROVIDER_2"
    '''
    :stability: experimental
    '''
    LAMBDA = "LAMBDA"
    '''
    :stability: experimental
    '''
    CFN_LAMBDA = "CFN_LAMBDA"
    '''
    :stability: experimental
    '''
    LAMBDA_LAYER_VERSION = "LAMBDA_LAYER_VERSION"
    '''
    :stability: experimental
    '''
    CFN_LAMBDA_LAYER_VERSION = "CFN_LAMBDA_LAYER_VERSION"
    '''
    :stability: experimental
    '''
    LAMBDA_ALIAS = "LAMBDA_ALIAS"
    '''
    :stability: experimental
    '''
    CFN_LAMBDA_ALIAS = "CFN_LAMBDA_ALIAS"
    '''
    :stability: experimental
    '''
    LAMBDA_BASE = "LAMBDA_BASE"
    '''
    :stability: experimental
    '''
    ASSET_STAGING = "ASSET_STAGING"
    '''
    :stability: experimental
    '''
    S3_ASSET = "S3_ASSET"
    '''
    :stability: experimental
    '''
    ECR_TARBALL_ASSET = "ECR_TARBALL_ASSET"
    '''
    :stability: experimental
    '''
    EC2_INSTANCE = "EC2_INSTANCE"
    '''
    :stability: experimental
    '''
    CFN_EC2_INSTANCE = "CFN_EC2_INSTANCE"
    '''
    :stability: experimental
    '''
    SECURITY_GROUP = "SECURITY_GROUP"
    '''
    :stability: experimental
    '''
    CFN_SECURITY_GROUP = "CFN_SECURITY_GROUP"
    '''
    :stability: experimental
    '''
    VPC = "VPC"
    '''
    :stability: experimental
    '''
    CFN_VPC = "CFN_VPC"
    '''
    :stability: experimental
    '''
    PRIVATE_SUBNET = "PRIVATE_SUBNET"
    '''
    :stability: experimental
    '''
    CFN_PRIVATE_SUBNET = "CFN_PRIVATE_SUBNET"
    '''
    :stability: experimental
    '''
    PUBLIC_SUBNET = "PUBLIC_SUBNET"
    '''
    :stability: experimental
    '''
    CFN_PUBLIC_SUBNET = "CFN_PUBLIC_SUBNET"
    '''
    :stability: experimental
    '''


@jsii.enum(jsii_type="@aws-prototyping-sdk/cdk-graph.EdgeDirectionEnum")
class EdgeDirectionEnum(enum.Enum):
    '''(experimental) EdgeDirection specifies in which direction the edge is directed or if it is undirected.

    :stability: experimental
    '''

    NONE = "NONE"
    '''(experimental) Indicates that edge is *undirected*;

    meaning there is no directional relationship between the **source** and **target**.

    :stability: experimental
    '''
    FORWARD = "FORWARD"
    '''(experimental) Indicates the edge is *directed* from the **source** to the **target**.

    :stability: experimental
    '''
    BACK = "BACK"
    '''(experimental) Indicates the edge is *directed* from the **target** to the **source**.

    :stability: experimental
    '''
    BOTH = "BOTH"
    '''(experimental) Indicates the edge is *bi-directional*.

    :stability: experimental
    '''


@jsii.enum(jsii_type="@aws-prototyping-sdk/cdk-graph.EdgeTypeEnum")
class EdgeTypeEnum(enum.Enum):
    '''(experimental) Edge types handles by the graph.

    :stability: experimental
    '''

    CUSTOM = "CUSTOM"
    '''(experimental) Custom edge.

    :stability: experimental
    '''
    REFERENCE = "REFERENCE"
    '''(experimental) Reference edge (Ref, Fn::GetAtt, Fn::ImportValue).

    :stability: experimental
    '''
    DEPENDENCY = "DEPENDENCY"
    '''(experimental) CloudFormation dependency edge.

    :stability: experimental
    '''


@jsii.enum(jsii_type="@aws-prototyping-sdk/cdk-graph.FilterPreset")
class FilterPreset(enum.Enum):
    '''(experimental) Filter presets.

    :stability: experimental
    '''

    COMPACT = "COMPACT"
    '''(experimental) Collapses extraneous nodes to parent and cdk created nodes on themselves, and prunes extraneous edges.

    This most closely represents the developers code for the current application
    and reduces the noise one expects.

    :stability: experimental
    '''
    NON_EXTRANEOUS = "NON_EXTRANEOUS"
    '''(experimental) Collapses extraneous nodes to parent and prunes extraneous edges.

    :stability: experimental
    '''


@jsii.enum(jsii_type="@aws-prototyping-sdk/cdk-graph.FilterStrategy")
class FilterStrategy(enum.Enum):
    '''(experimental) Filter strategy to apply to filter matches.

    :stability: experimental
    '''

    PRUNE = "PRUNE"
    '''(experimental) Remove filtered entity and all its edges.

    :stability: experimental
    '''
    COLLAPSE = "COLLAPSE"
    '''(experimental) Collapse all child entities of filtered entity into filtered entity;

    and hoist all edges.

    :stability: experimental
    '''
    COLLAPSE_TO_PARENT = "COLLAPSE_TO_PARENT"
    '''(experimental) Collapse all filtered entities into their parent entity;

    and hoist its edges to parent.

    :stability: experimental
    '''


@jsii.enum(jsii_type="@aws-prototyping-sdk/cdk-graph.FlagEnum")
class FlagEnum(enum.Enum):
    '''(experimental) Graph flags.

    :stability: experimental
    '''

    CLUSTER = "CLUSTER"
    '''(experimental) Indicates that node is a cluster (container) and treated like an emphasized subgraph.

    :stability: experimental
    '''
    GRAPH_CONTAINER = "GRAPH_CONTAINER"
    '''(experimental) Indicates that node is non-resource container (Root, App) and used for structural purpose in the graph only.

    :stability: experimental
    '''
    EXTRANEOUS = "EXTRANEOUS"
    '''(experimental) Indicates that the entity is extraneous and considered collapsible to parent without impact of intent.

    :stability: experimental
    '''
    RESOURCE_WRAPPER = "RESOURCE_WRAPPER"
    '''(experimental) Indicates node is a simple CfnResource wrapper and can be collapsed without change of intent;

    Determined by only containing a single child of "Default" or "Resource"

    :stability: experimental
    '''
    ASSET = "ASSET"
    '''(experimental) Indicates node is considered a CDK Asset (Lambda Code, Docker Image, etc).

    :stability: experimental
    '''
    CDK_OWNED = "CDK_OWNED"
    '''(experimental) Indicates that node was created by CDK (``construct.node.defaultChild === CfnResource``).

    :stability: experimental
    '''
    CLOSED_EDGE = "CLOSED_EDGE"
    '''(experimental) Indicates that edge is closed;

    meaning ``source === target``. This flag only gets applied on creation of edge, not during mutations to maintain initial intent.

    :stability: experimental
    '''
    MUTATED = "MUTATED"
    '''(experimental) Indicates that entity was mutated;

    meaning a mutation was performed to change originally computed graph value.

    :stability: experimental
    '''
    WRAPPED_CFN_RESOURCE = "WRAPPED_CFN_RESOURCE"
    '''(experimental) Indicates that cfn resource has equivalent cdk resource wrapper.

    (eg: Lambda => CfnLambda)

    :stability: experimental
    '''


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.ICdkGraphPlugin")
class ICdkGraphPlugin(typing_extensions.Protocol):
    '''(experimental) CdkGraph **Plugin** interface.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''(experimental) Unique identifier for this plugin.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''(experimental) Plugin version.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="dependencies")
    def dependencies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) List of plugins this plugin depends on, including optional semver version (eg: ["foo", "bar@1.2"]).

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="bind")
    def bind(self) -> "IGraphPluginBindCallback":
        '''(experimental) Binds the plugin to the CdkGraph instance.

        Enables plugins to receive base configs.

        :stability: experimental
        '''
        ...

    @bind.setter
    def bind(self, value: "IGraphPluginBindCallback") -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="inspect")
    def inspect(self) -> typing.Optional["IGraphVisitorCallback"]:
        '''(experimental) Node visitor callback for construct tree traversal.

        This follows IAspect.visit pattern, but the order
        of visitor traversal in managed by the CdkGraph.

        :stability: experimental
        '''
        ...

    @inspect.setter
    def inspect(self, value: typing.Optional["IGraphVisitorCallback"]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="report")
    def report(self) -> typing.Optional["IGraphReportCallback"]:
        '''(experimental) Generate asynchronous reports based on the graph.

        This is not automatically called when synthesizing CDK.
        Developer must explicitly add ``await graphInstance.report()`` to the CDK bin or invoke this outside
        of the CDK synth. In either case, the plugin receives the in-memory graph interface when invoked, as the
        CdkGraph will deserialize the graph prior to invoking the plugin report.

        :stability: experimental
        '''
        ...

    @report.setter
    def report(self, value: typing.Optional["IGraphReportCallback"]) -> None:
        ...

    @builtins.property
    @jsii.member(jsii_name="synthesize")
    def synthesize(self) -> typing.Optional["IGraphSynthesizeCallback"]:
        '''(experimental) Called during CDK synthesize to generate synchronous artifacts based on the in-memory graph passed to the plugin.

        This is called in fifo order of plugins.

        :stability: experimental
        '''
        ...

    @synthesize.setter
    def synthesize(self, value: typing.Optional["IGraphSynthesizeCallback"]) -> None:
        ...


class _ICdkGraphPluginProxy:
    '''(experimental) CdkGraph **Plugin** interface.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.ICdkGraphPlugin"

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''(experimental) Unique identifier for this plugin.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''(experimental) Plugin version.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="dependencies")
    def dependencies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) List of plugins this plugin depends on, including optional semver version (eg: ["foo", "bar@1.2"]).

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dependencies"))

    @builtins.property
    @jsii.member(jsii_name="bind")
    def bind(self) -> "IGraphPluginBindCallback":
        '''(experimental) Binds the plugin to the CdkGraph instance.

        Enables plugins to receive base configs.

        :stability: experimental
        '''
        return typing.cast("IGraphPluginBindCallback", jsii.get(self, "bind"))

    @bind.setter
    def bind(self, value: "IGraphPluginBindCallback") -> None:
        if __debug__:
            def stub(value: IGraphPluginBindCallback) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bind", value)

    @builtins.property
    @jsii.member(jsii_name="inspect")
    def inspect(self) -> typing.Optional["IGraphVisitorCallback"]:
        '''(experimental) Node visitor callback for construct tree traversal.

        This follows IAspect.visit pattern, but the order
        of visitor traversal in managed by the CdkGraph.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["IGraphVisitorCallback"], jsii.get(self, "inspect"))

    @inspect.setter
    def inspect(self, value: typing.Optional["IGraphVisitorCallback"]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IGraphVisitorCallback]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inspect", value)

    @builtins.property
    @jsii.member(jsii_name="report")
    def report(self) -> typing.Optional["IGraphReportCallback"]:
        '''(experimental) Generate asynchronous reports based on the graph.

        This is not automatically called when synthesizing CDK.
        Developer must explicitly add ``await graphInstance.report()`` to the CDK bin or invoke this outside
        of the CDK synth. In either case, the plugin receives the in-memory graph interface when invoked, as the
        CdkGraph will deserialize the graph prior to invoking the plugin report.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["IGraphReportCallback"], jsii.get(self, "report"))

    @report.setter
    def report(self, value: typing.Optional["IGraphReportCallback"]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IGraphReportCallback]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "report", value)

    @builtins.property
    @jsii.member(jsii_name="synthesize")
    def synthesize(self) -> typing.Optional["IGraphSynthesizeCallback"]:
        '''(experimental) Called during CDK synthesize to generate synchronous artifacts based on the in-memory graph passed to the plugin.

        This is called in fifo order of plugins.

        :stability: experimental
        '''
        return typing.cast(typing.Optional["IGraphSynthesizeCallback"], jsii.get(self, "synthesize"))

    @synthesize.setter
    def synthesize(self, value: typing.Optional["IGraphSynthesizeCallback"]) -> None:
        if __debug__:
            def stub(value: typing.Optional[IGraphSynthesizeCallback]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "synthesize", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICdkGraphPlugin).__jsii_proxy_class__ = lambda : _ICdkGraphPluginProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.ICdkGraphProps")
class ICdkGraphProps(typing_extensions.Protocol):
    '''(experimental) {@link CdkGraph} props.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="plugins")
    def plugins(self) -> typing.Optional[typing.List[ICdkGraphPlugin]]:
        '''(experimental) List of plugins to extends the graph.

        Plugins are invoked at each phases in fifo order.

        :stability: experimental
        '''
        ...

    @plugins.setter
    def plugins(self, value: typing.Optional[typing.List[ICdkGraphPlugin]]) -> None:
        ...


class _ICdkGraphPropsProxy:
    '''(experimental) {@link CdkGraph} props.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.ICdkGraphProps"

    @builtins.property
    @jsii.member(jsii_name="plugins")
    def plugins(self) -> typing.Optional[typing.List[ICdkGraphPlugin]]:
        '''(experimental) List of plugins to extends the graph.

        Plugins are invoked at each phases in fifo order.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[ICdkGraphPlugin]], jsii.get(self, "plugins"))

    @plugins.setter
    def plugins(self, value: typing.Optional[typing.List[ICdkGraphPlugin]]) -> None:
        if __debug__:
            def stub(value: typing.Optional[typing.List[ICdkGraphPlugin]]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "plugins", value)

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICdkGraphProps).__jsii_proxy_class__ = lambda : _ICdkGraphPropsProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.ICounterRecord")
class ICounterRecord(typing_extensions.Protocol):
    '''(experimental) ICounterRecord is record of keyed counts from {@link Counters}.

    The record is a mapping of ``key => count`` values.

    :stability: experimental
    '''

    pass


class _ICounterRecordProxy:
    '''(experimental) ICounterRecord is record of keyed counts from {@link Counters}.

    The record is a mapping of ``key => count`` values.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.ICounterRecord"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICounterRecord).__jsii_proxy_class__ = lambda : _ICounterRecordProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.IFilterFocusCallback")
class IFilterFocusCallback(typing_extensions.Protocol):
    '''(experimental) Determines focus node of filter plan.

    :stability: experimental
    '''

    pass


class _IFilterFocusCallbackProxy:
    '''(experimental) Determines focus node of filter plan.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.IFilterFocusCallback"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFilterFocusCallback).__jsii_proxy_class__ = lambda : _IFilterFocusCallbackProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.IGraphFilter")
class IGraphFilter(typing_extensions.Protocol):
    '''(experimental) Graph filter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="allNodes")
    def all_nodes(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates that all nodes will be filtered, rather than just Resource and CfnResource nodes.

        By enabling this, all Stages, Stacks, and structural construct boundaries will be filtered as well.
        In general, most users intent is to operate against resources and desire to preserve structural groupings,
        which is common in most Cfn/Cdk based filtering where inputs are "include" lists.

        Defaults to value of containing {@link IGraphFilterPlan.allNodes}

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="edge")
    def edge(self) -> typing.Optional[_IEdgePredicate_786afb09]:
        '''(experimental) Predicate to match edges.

        Edges are evaluated after nodes are filtered.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="inverse")
    def inverse(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates that matches will be filtered, as opposed to non-matches.

        The default follows common `Javascript Array.filter <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter>`_
        precedence of preserving matches during filtering, while pruning non-matches.

        :default: false - Preserve matches, and filter out non-matches.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="node")
    def node(self) -> typing.Optional[_INodePredicate_1dc8755a]:
        '''(experimental) Predicate to match nodes.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> typing.Optional[FilterStrategy]:
        '''(experimental) Filter strategy to apply to matching nodes.

        Edges do not have a strategy, they are always pruned.

        :default: {FilterStrategy.PRUNE}

        :stability: experimental
        '''
        ...


class _IGraphFilterProxy:
    '''(experimental) Graph filter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.IGraphFilter"

    @builtins.property
    @jsii.member(jsii_name="allNodes")
    def all_nodes(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates that all nodes will be filtered, rather than just Resource and CfnResource nodes.

        By enabling this, all Stages, Stacks, and structural construct boundaries will be filtered as well.
        In general, most users intent is to operate against resources and desire to preserve structural groupings,
        which is common in most Cfn/Cdk based filtering where inputs are "include" lists.

        Defaults to value of containing {@link IGraphFilterPlan.allNodes}

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "allNodes"))

    @builtins.property
    @jsii.member(jsii_name="edge")
    def edge(self) -> typing.Optional[_IEdgePredicate_786afb09]:
        '''(experimental) Predicate to match edges.

        Edges are evaluated after nodes are filtered.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_IEdgePredicate_786afb09], jsii.get(self, "edge"))

    @builtins.property
    @jsii.member(jsii_name="inverse")
    def inverse(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates that matches will be filtered, as opposed to non-matches.

        The default follows common `Javascript Array.filter <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter>`_
        precedence of preserving matches during filtering, while pruning non-matches.

        :default: false - Preserve matches, and filter out non-matches.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "inverse"))

    @builtins.property
    @jsii.member(jsii_name="node")
    def node(self) -> typing.Optional[_INodePredicate_1dc8755a]:
        '''(experimental) Predicate to match nodes.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[_INodePredicate_1dc8755a], jsii.get(self, "node"))

    @builtins.property
    @jsii.member(jsii_name="strategy")
    def strategy(self) -> typing.Optional[FilterStrategy]:
        '''(experimental) Filter strategy to apply to matching nodes.

        Edges do not have a strategy, they are always pruned.

        :default: {FilterStrategy.PRUNE}

        :stability: experimental
        '''
        return typing.cast(typing.Optional[FilterStrategy], jsii.get(self, "strategy"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphFilter).__jsii_proxy_class__ = lambda : _IGraphFilterProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.IGraphFilterPlan")
class IGraphFilterPlan(typing_extensions.Protocol):
    '''(experimental) Graph filter plan.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="allNodes")
    def all_nodes(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates that all nodes will be filtered, rather than just Resource and CfnResource nodes.

        By enabling this, all Stages, Stacks, and structural construct boundaries will be filtered as well.
        In general, most users intent is to operate against resources and desire to preserve structural groupings,
        which is common in most Cfn/Cdk based filtering where inputs are "include" lists.

        :default: false By default only Resource and CfnResource nodes are filtered.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="filters")
    def filters(
        self,
    ) -> typing.Optional[typing.List[typing.Union[IGraphFilter, "IGraphStoreFilter"]]]:
        '''(experimental) Ordered list of {@link IGraphFilter} and {@link IGraphStoreFilter} filters to apply to the store.

        - Filters are applied *after* the preset filtering is applied if present.
        - Filters are applied sequentially against all nodes, as opposed to IAspect.visitor pattern
          which are sequentially applied per node.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="focus")
    def focus(
        self,
    ) -> typing.Optional[typing.Union[_Node_ddadac9d, IFilterFocusCallback, "IGraphFilterPlanFocusConfig"]]:
        '''(experimental) Config to focus the graph on specific node.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> typing.Optional[constructs.ConstructOrder]:
        '''(experimental) The order to visit nodes and edges during filtering.

        :default: {ConstructOrder.PREORDER}

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="preset")
    def preset(self) -> typing.Optional[FilterPreset]:
        '''(experimental) Optional preset filter to apply before other filters.

        :stability: experimental
        '''
        ...


class _IGraphFilterPlanProxy:
    '''(experimental) Graph filter plan.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.IGraphFilterPlan"

    @builtins.property
    @jsii.member(jsii_name="allNodes")
    def all_nodes(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates that all nodes will be filtered, rather than just Resource and CfnResource nodes.

        By enabling this, all Stages, Stacks, and structural construct boundaries will be filtered as well.
        In general, most users intent is to operate against resources and desire to preserve structural groupings,
        which is common in most Cfn/Cdk based filtering where inputs are "include" lists.

        :default: false By default only Resource and CfnResource nodes are filtered.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "allNodes"))

    @builtins.property
    @jsii.member(jsii_name="filters")
    def filters(
        self,
    ) -> typing.Optional[typing.List[typing.Union[IGraphFilter, "IGraphStoreFilter"]]]:
        '''(experimental) Ordered list of {@link IGraphFilter} and {@link IGraphStoreFilter} filters to apply to the store.

        - Filters are applied *after* the preset filtering is applied if present.
        - Filters are applied sequentially against all nodes, as opposed to IAspect.visitor pattern
          which are sequentially applied per node.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List[typing.Union[IGraphFilter, "IGraphStoreFilter"]]], jsii.get(self, "filters"))

    @builtins.property
    @jsii.member(jsii_name="focus")
    def focus(
        self,
    ) -> typing.Optional[typing.Union[_Node_ddadac9d, IFilterFocusCallback, "IGraphFilterPlanFocusConfig"]]:
        '''(experimental) Config to focus the graph on specific node.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Union[_Node_ddadac9d, IFilterFocusCallback, "IGraphFilterPlanFocusConfig"]], jsii.get(self, "focus"))

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> typing.Optional[constructs.ConstructOrder]:
        '''(experimental) The order to visit nodes and edges during filtering.

        :default: {ConstructOrder.PREORDER}

        :stability: experimental
        '''
        return typing.cast(typing.Optional[constructs.ConstructOrder], jsii.get(self, "order"))

    @builtins.property
    @jsii.member(jsii_name="preset")
    def preset(self) -> typing.Optional[FilterPreset]:
        '''(experimental) Optional preset filter to apply before other filters.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[FilterPreset], jsii.get(self, "preset"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphFilterPlan).__jsii_proxy_class__ = lambda : _IGraphFilterPlanProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.IGraphFilterPlanFocusConfig")
class IGraphFilterPlanFocusConfig(typing_extensions.Protocol):
    '''
    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="node")
    def node(self) -> typing.Union[_Node_ddadac9d, IFilterFocusCallback]:
        '''(experimental) The node or resolver to determine the node to focus on.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="noHoist")
    def no_hoist(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates if ancestral containers are preserved (eg: Stages, Stack).

        If ``false``, the "focused node" will be hoisted to the graph root and all ancestors will be pruned.
        If ``true``, the "focused" will be left in-place, while all siblings and non-scope ancestors will be pruned.

        :default: true

        :stability: experimental
        '''
        ...


class _IGraphFilterPlanFocusConfigProxy:
    '''
    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.IGraphFilterPlanFocusConfig"

    @builtins.property
    @jsii.member(jsii_name="node")
    def node(self) -> typing.Union[_Node_ddadac9d, IFilterFocusCallback]:
        '''(experimental) The node or resolver to determine the node to focus on.

        :stability: experimental
        '''
        return typing.cast(typing.Union[_Node_ddadac9d, IFilterFocusCallback], jsii.get(self, "node"))

    @builtins.property
    @jsii.member(jsii_name="noHoist")
    def no_hoist(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates if ancestral containers are preserved (eg: Stages, Stack).

        If ``false``, the "focused node" will be hoisted to the graph root and all ancestors will be pruned.
        If ``true``, the "focused" will be left in-place, while all siblings and non-scope ancestors will be pruned.

        :default: true

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "noHoist"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphFilterPlanFocusConfig).__jsii_proxy_class__ = lambda : _IGraphFilterPlanFocusConfigProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.IGraphPluginBindCallback")
class IGraphPluginBindCallback(typing_extensions.Protocol):
    '''(experimental) Callback signature for graph ``Plugin.bind`` operation.

    :stability: experimental
    '''

    pass


class _IGraphPluginBindCallbackProxy:
    '''(experimental) Callback signature for graph ``Plugin.bind`` operation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.IGraphPluginBindCallback"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphPluginBindCallback).__jsii_proxy_class__ = lambda : _IGraphPluginBindCallbackProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.IGraphReportCallback")
class IGraphReportCallback(typing_extensions.Protocol):
    '''(experimental) Callback signature for graph ``Plugin.report`` operation.

    :stability: experimental
    '''

    pass


class _IGraphReportCallbackProxy:
    '''(experimental) Callback signature for graph ``Plugin.report`` operation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.IGraphReportCallback"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphReportCallback).__jsii_proxy_class__ = lambda : _IGraphReportCallbackProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.IGraphStoreFilter")
class IGraphStoreFilter(typing_extensions.Protocol):
    '''(experimental) Store filter callback interface used to perform filtering operations directly against the store, as opposed to using {@link IGraphFilter} definitions.

    :stability: experimental
    '''

    pass


class _IGraphStoreFilterProxy:
    '''(experimental) Store filter callback interface used to perform filtering operations directly against the store, as opposed to using {@link IGraphFilter} definitions.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.IGraphStoreFilter"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphStoreFilter).__jsii_proxy_class__ = lambda : _IGraphStoreFilterProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.IGraphSynthesizeCallback")
class IGraphSynthesizeCallback(typing_extensions.Protocol):
    '''(experimental) Callback signature for graph ``Plugin.synthesize`` operation.

    :stability: experimental
    '''

    pass


class _IGraphSynthesizeCallbackProxy:
    '''(experimental) Callback signature for graph ``Plugin.synthesize`` operation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.IGraphSynthesizeCallback"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphSynthesizeCallback).__jsii_proxy_class__ = lambda : _IGraphSynthesizeCallbackProxy


@jsii.interface(jsii_type="@aws-prototyping-sdk/cdk-graph.IGraphVisitorCallback")
class IGraphVisitorCallback(typing_extensions.Protocol):
    '''(experimental) Callback signature for graph ``Plugin.inspect`` operation.

    :stability: experimental
    '''

    pass


class _IGraphVisitorCallbackProxy:
    '''(experimental) Callback signature for graph ``Plugin.inspect`` operation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph.IGraphVisitorCallback"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphVisitorCallback).__jsii_proxy_class__ = lambda : _IGraphVisitorCallbackProxy


@jsii.data_type(
    jsii_type="@aws-prototyping-sdk/cdk-graph.InferredNodeProps",
    jsii_struct_bases=[_Entity_794b3e11],
    name_mapping={
        "uuid": "uuid",
        "attributes": "attributes",
        "flags": "flags",
        "metadata": "metadata",
        "tags": "tags",
        "dependencies": "dependencies",
        "unresolved_references": "unresolvedReferences",
        "cfn_type": "cfnType",
        "construct_info": "constructInfo",
        "logical_id": "logicalId",
    },
)
class InferredNodeProps(_Entity_794b3e11):
    def __init__(
        self,
        *,
        uuid: builtins.str,
        attributes: typing.Optional[typing.Union[_Attributes_b47661e3, typing.Dict[str, typing.Any]]] = None,
        flags: typing.Optional[typing.Sequence[FlagEnum]] = None,
        metadata: typing.Optional[typing.Sequence[typing.Union[constructs.MetadataEntry, typing.Dict[str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Union[_Tags_cf30c388, typing.Dict[str, typing.Any]]] = None,
        dependencies: typing.Sequence[builtins.str],
        unresolved_references: typing.Sequence[typing.Union["UnresolvedReference", typing.Dict[str, typing.Any]]],
        cfn_type: typing.Optional[builtins.str] = None,
        construct_info: typing.Optional[typing.Union[ConstructInfo, typing.Dict[str, typing.Any]]] = None,
        logical_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Inferred node props.

        :param uuid: (experimental) Universally unique identity.
        :param attributes: (experimental) Serializable entity attributes.
        :param flags: (experimental) Serializable entity flags.
        :param metadata: (experimental) Serializable entity metadata.
        :param tags: (experimental) Serializable entity tags.
        :param dependencies: 
        :param unresolved_references: 
        :param cfn_type: 
        :param construct_info: 
        :param logical_id: 

        :stability: experimental
        '''
        if isinstance(attributes, dict):
            attributes = _Attributes_b47661e3(**attributes)
        if isinstance(tags, dict):
            tags = _Tags_cf30c388(**tags)
        if isinstance(construct_info, dict):
            construct_info = ConstructInfo(**construct_info)
        if __debug__:
            def stub(
                *,
                uuid: builtins.str,
                attributes: typing.Optional[typing.Union[_Attributes_b47661e3, typing.Dict[str, typing.Any]]] = None,
                flags: typing.Optional[typing.Sequence[FlagEnum]] = None,
                metadata: typing.Optional[typing.Sequence[typing.Union[constructs.MetadataEntry, typing.Dict[str, typing.Any]]]] = None,
                tags: typing.Optional[typing.Union[_Tags_cf30c388, typing.Dict[str, typing.Any]]] = None,
                dependencies: typing.Sequence[builtins.str],
                unresolved_references: typing.Sequence[typing.Union[UnresolvedReference, typing.Dict[str, typing.Any]]],
                cfn_type: typing.Optional[builtins.str] = None,
                construct_info: typing.Optional[typing.Union[ConstructInfo, typing.Dict[str, typing.Any]]] = None,
                logical_id: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument uuid", value=uuid, expected_type=type_hints["uuid"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument flags", value=flags, expected_type=type_hints["flags"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument dependencies", value=dependencies, expected_type=type_hints["dependencies"])
            check_type(argname="argument unresolved_references", value=unresolved_references, expected_type=type_hints["unresolved_references"])
            check_type(argname="argument cfn_type", value=cfn_type, expected_type=type_hints["cfn_type"])
            check_type(argname="argument construct_info", value=construct_info, expected_type=type_hints["construct_info"])
            check_type(argname="argument logical_id", value=logical_id, expected_type=type_hints["logical_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "uuid": uuid,
            "dependencies": dependencies,
            "unresolved_references": unresolved_references,
        }
        if attributes is not None:
            self._values["attributes"] = attributes
        if flags is not None:
            self._values["flags"] = flags
        if metadata is not None:
            self._values["metadata"] = metadata
        if tags is not None:
            self._values["tags"] = tags
        if cfn_type is not None:
            self._values["cfn_type"] = cfn_type
        if construct_info is not None:
            self._values["construct_info"] = construct_info
        if logical_id is not None:
            self._values["logical_id"] = logical_id

    @builtins.property
    def uuid(self) -> builtins.str:
        '''(experimental) Universally unique identity.

        :stability: experimental
        '''
        result = self._values.get("uuid")
        assert result is not None, "Required property 'uuid' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(self) -> typing.Optional[_Attributes_b47661e3]:
        '''(experimental) Serializable entity attributes.

        :see: {@link Attributes}
        :stability: experimental
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[_Attributes_b47661e3], result)

    @builtins.property
    def flags(self) -> typing.Optional[typing.List[FlagEnum]]:
        '''(experimental) Serializable entity flags.

        :see: {@link FlagEnum}
        :stability: experimental
        '''
        result = self._values.get("flags")
        return typing.cast(typing.Optional[typing.List[FlagEnum]], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.List[constructs.MetadataEntry]]:
        '''(experimental) Serializable entity metadata.

        :see: {@link Metadata}
        :stability: experimental
        '''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.List[constructs.MetadataEntry]], result)

    @builtins.property
    def tags(self) -> typing.Optional[_Tags_cf30c388]:
        '''(experimental) Serializable entity tags.

        :see: {@link Tags}
        :stability: experimental
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[_Tags_cf30c388], result)

    @builtins.property
    def dependencies(self) -> typing.List[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("dependencies")
        assert result is not None, "Required property 'dependencies' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def unresolved_references(self) -> typing.List["UnresolvedReference"]:
        '''
        :stability: experimental
        '''
        result = self._values.get("unresolved_references")
        assert result is not None, "Required property 'unresolved_references' is missing"
        return typing.cast(typing.List["UnresolvedReference"], result)

    @builtins.property
    def cfn_type(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cfn_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def construct_info(self) -> typing.Optional[ConstructInfo]:
        '''
        :stability: experimental
        '''
        result = self._values.get("construct_info")
        return typing.cast(typing.Optional[ConstructInfo], result)

    @builtins.property
    def logical_id(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("logical_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InferredNodeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-prototyping-sdk/cdk-graph.MetadataTypeEnum")
class MetadataTypeEnum(enum.Enum):
    '''(experimental) Common cdk metadata types.

    :stability: experimental
    '''

    LOGICAL_ID = "LOGICAL_ID"
    '''
    :stability: experimental
    '''


@jsii.enum(jsii_type="@aws-prototyping-sdk/cdk-graph.NodeTypeEnum")
class NodeTypeEnum(enum.Enum):
    '''(experimental) Node types handled by the graph.

    :stability: experimental
    '''

    DEFAULT = "DEFAULT"
    '''(experimental) Default node type - used for all nodes that don't have explicit type defined.

    :stability: experimental
    '''
    CFN_RESOURCE = "CFN_RESOURCE"
    '''(experimental) L1 cfn resource node.

    :stability: experimental
    '''
    RESOURCE = "RESOURCE"
    '''(experimental) L2 cdk resource node.

    :stability: experimental
    '''
    CUSTOM_RESOURCE = "CUSTOM_RESOURCE"
    '''(experimental) Cdk customer resource node.

    :stability: experimental
    '''
    ROOT = "ROOT"
    '''(experimental) Graph root node.

    :stability: experimental
    '''
    APP = "APP"
    '''(experimental) Cdk App node.

    :stability: experimental
    '''
    STAGE = "STAGE"
    '''(experimental) Cdk Stage node.

    :stability: experimental
    '''
    STACK = "STACK"
    '''(experimental) Cdk Stack node.

    :stability: experimental
    '''
    NESTED_STACK = "NESTED_STACK"
    '''(experimental) Cdk NestedStack node.

    :stability: experimental
    '''
    OUTPUT = "OUTPUT"
    '''(experimental) CfnOutput node.

    :stability: experimental
    '''
    PARAMETER = "PARAMETER"
    '''(experimental) CfnParameter node.

    :stability: experimental
    '''
    ASSET = "ASSET"
    '''(experimental) Cdk asset node.

    :stability: experimental
    '''


@jsii.enum(jsii_type="@aws-prototyping-sdk/cdk-graph.ReferenceTypeEnum")
class ReferenceTypeEnum(enum.Enum):
    '''(experimental) Reference edge types.

    :stability: experimental
    '''

    REF = "REF"
    '''(experimental) CloudFormation **Ref** reference.

    :stability: experimental
    '''
    ATTRIBUTE = "ATTRIBUTE"
    '''(experimental) CloudFormation **Fn::GetAtt** reference.

    :stability: experimental
    '''
    IMPORT = "IMPORT"
    '''(experimental) CloudFormation **Fn::ImportValue** reference.

    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="@aws-prototyping-sdk/cdk-graph.UnresolvedReference",
    jsii_struct_bases=[],
    name_mapping={
        "reference_type": "referenceType",
        "source": "source",
        "target": "target",
        "value": "value",
    },
)
class UnresolvedReference:
    def __init__(
        self,
        *,
        reference_type: ReferenceTypeEnum,
        source: builtins.str,
        target: builtins.str,
        value: typing.Optional[typing.Union[builtins.str, jsii.Number, builtins.bool, typing.Union[_PlainObject_c976ebcc, typing.Dict[str, typing.Any]], typing.Sequence[typing.Union[builtins.str, jsii.Number, builtins.bool, typing.Union[_PlainObject_c976ebcc, typing.Dict[str, typing.Any]]]]]] = None,
    ) -> None:
        '''(experimental) Unresolved reference struct.

        During graph computation references are unresolved and stored in this struct.

        :param reference_type: 
        :param source: 
        :param target: 
        :param value: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                reference_type: ReferenceTypeEnum,
                source: builtins.str,
                target: builtins.str,
                value: typing.Optional[typing.Union[builtins.str, jsii.Number, builtins.bool, typing.Union[_PlainObject_c976ebcc, typing.Dict[str, typing.Any]], typing.Sequence[typing.Union[builtins.str, jsii.Number, builtins.bool, typing.Union[_PlainObject_c976ebcc, typing.Dict[str, typing.Any]]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument reference_type", value=reference_type, expected_type=type_hints["reference_type"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "reference_type": reference_type,
            "source": source,
            "target": target,
        }
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def reference_type(self) -> ReferenceTypeEnum:
        '''
        :stability: experimental
        '''
        result = self._values.get("reference_type")
        assert result is not None, "Required property 'reference_type' is missing"
        return typing.cast(ReferenceTypeEnum, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc, typing.List[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc]]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc, typing.List[typing.Union[builtins.str, jsii.Number, builtins.bool, _PlainObject_c976ebcc]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UnresolvedReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CdkConstructIds",
    "CdkGraph",
    "CdkGraphArtifact",
    "CdkGraphArtifacts",
    "CdkGraphConfig",
    "CdkGraphContext",
    "CfnAttributesEnum",
    "ConstructInfo",
    "ConstructInfoFqnEnum",
    "EdgeDirectionEnum",
    "EdgeTypeEnum",
    "FilterPreset",
    "FilterStrategy",
    "FlagEnum",
    "ICdkGraphPlugin",
    "ICdkGraphProps",
    "ICounterRecord",
    "IFilterFocusCallback",
    "IGraphFilter",
    "IGraphFilterPlan",
    "IGraphFilterPlanFocusConfig",
    "IGraphPluginBindCallback",
    "IGraphReportCallback",
    "IGraphStoreFilter",
    "IGraphSynthesizeCallback",
    "IGraphVisitorCallback",
    "InferredNodeProps",
    "MetadataTypeEnum",
    "NodeTypeEnum",
    "ReferenceTypeEnum",
    "UnresolvedReference",
    "graph",
    "serialized_graph",
]

publication.publish()

# Loading modules to ensure their types are registered with the jsii runtime library
from . import graph
from . import serialized_graph
