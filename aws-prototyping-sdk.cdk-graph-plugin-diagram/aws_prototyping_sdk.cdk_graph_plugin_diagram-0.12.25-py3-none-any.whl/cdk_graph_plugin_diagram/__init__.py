'''
## Diagram Plugin - Cdk Graph

`@aws-prototyping-skd/cdk-graph-plugin-diagram`

![experimental](https://img.shields.io/badge/stability-experimental-orange.svg)
![alpha](https://img.shields.io/badge/version-alpha-red.svg) \
[![API Documentation](https://img.shields.io/badge/view-API_Documentation-blue.svg)](https://aws.github.io/aws-prototyping-sdk/typescript/cdk-graph-plugin-diagram/index.html)
[![Source Code](https://img.shields.io/badge/view-Source_Code-blue.svg)](https://github.com/aws/aws-prototyping-sdk/tree/mainline/packages/cdk-graph-plugin-diagram)

This plugin generates diagrams utilizing the [cdk-graph](https://aws.github.io/aws-prototyping-sdk/typescript/cdk-graph/index.html) framework.

> More comprehensive documentation to come as this package stabilizes.

> **Disclaimer:** This is the first **cdk graph** plugin, it is highly *experimental*, and subject to major refactors as we gain feedback from the community.

| | |
| --- | --- |
| <img src="docs/examples/default.png" width="300" /> | <img src="docs/examples/dark.png" width="300" /> |

### Quick Start

```python
// bin/app.ts

// Must wrap cdk app with async IIFE function to enable async cdk-graph report
(async () => {
  const app = new App();
  // ... add stacks, etc
  const graph = new CdkGraph(app, {
    plugins: [new CdkGraphDiagramPlugin()],
  });

  app.synth();

  // async cdk-graph reporting hook
  await graph.report();
})

// => cdk.out/diagram.dot
// => cdk.out/diagram.svg
// => cdk.out/diagram.png
```

> This plugin currently only supports `async report()` generation following the above example. **Make sure to wrap the cdk app with *async IIFE*.**

### Supported Formats

| Format | Status | Extends | Provider |
| --- | --- | --- | --- |
| [DOT](https://graphviz.org/docs/outputs/canon/) | ![beta](https://img.shields.io/badge/status-beta-cyan.svg) | - | [Graphviz](docs/graphviz/README.md)
| [SVG](https://graphviz.org/docs/outputs/svg/) | ![beta](https://img.shields.io/badge/status-beta-cyan.svg) | [DOT](https://graphviz.org/docs/outputs/canon/) | [Graphviz](docs/graphviz/README.md)
| [PNG](https://graphviz.org/docs/outputs/png/) | ![beta](https://img.shields.io/badge/status-beta-cyan.svg) | [SVG](https://graphviz.org/docs/outputs/canon/) | [Graphviz](docs/graphviz/README.md)

---


### Diagram Providers

| Provider | Status | Formats |
| --- | --- | --- |
| [Graphviz](docs/graphviz/README.md) | ![alpha](https://img.shields.io/badge/status-alpha-orange.svg) | [DOT](https://graphviz.org/docs/outputs/canon/), [SVG](https://graphviz.org/docs/outputs/svg/), [PNG](https://graphviz.org/docs/outputs/png/) |
| [Drawio](docs/drawio/README.md) | ![design](https://img.shields.io/badge/status-design-tan.svg) | *TBD: very early stage design and development* |

---


### Configuration

See [API Documentation](https://aws.github.io/aws-prototyping-sdk/typescript/cdk-graph-plugin-diagram/index.html) for details, and look in [unit tests](https://github.com/aws/aws-prototyping-sdk/tree/mainline/packages/cdk-graph-plugin-diagram/test/graphviz) for more examples.

#### Example Configurations (expand below)

##### **Presets**

<details>
<summary>Preset: compact</summary>

[<img src="docs/examples/compact.png" height="200" />](docs/examples/compact.png)

```python
{
  name: "compact",
  title: "Compact Diagram",
  filterPlan: {
    preset: FilterPreset.COMPACT,
  },
},
```

</details><details>
<summary>Preset: verbose</summary>

[<img src="docs/examples/verbose.png" height="200" />](docs/examples/verbose.png)

```python
{
  name: "verbose",
  title: "Verbose Diagram",
  format: DiagramFormat.PNG,
  ignoreDefaults: true,
},
```

</details>

##### **Focus**

<details>
<summary>Focus: hoist</summary>

[<img src="docs/examples/focus.png" height="200" />](docs/examples/focus.png)

```python
{
  name: "focus",
  title: "Focus Lambda Diagram (non-extraneous)",
  filterPlan: {
    focus: (store) =>
      store.getNode(getConstructUUID(app.stack.lambda)),
    preset: FilterPreset.NON_EXTRANEOUS,
  },
  ignoreDefaults: true,
},
```

</details><details>
<summary>Focus: no hoist</summary>

[<img src="docs/examples/focus-nohoist.png" height="200" />](docs/examples/focus-nohoist.png)

```python
{
  name: "focus-nohoist",
  title: "Focus WebServer Diagram (noHoist, verbose)",
  filterPlan: {
    focus: {
      node: (store) =>
        store.getNode(getConstructUUID(app.stack.webServer)),
      noHoist: true,
    },
  },
  ignoreDefaults: true,
},
```

</details>

##### **Filters**

<details>
<summary>Filter: Include specific cfn resource types</summary>

[<img src="docs/examples/filter-cfntype-include.png" height="200" />](docs/examples/filter-cfntype-include.png)

```python
{
  name: "includeCfnType",
  title: "Include CfnType Diagram (filter)",
  filterPlan: {
    filters: [
      Filters.includeCfnType([
        aws_arch.CfnSpec.ServiceResourceDictionary.EC2.Instance,
        /AWS::Lambda::Function.*/,
        "AWS::IAM::Role",
      ]),
      Filters.compact(),
    ],
  },
},
```

</details><details>
<summary>Filter: Exclude specific cfn resource types</summary>

[<img src="docs/examples/filter-cfntype-exclude.png" height="200" />](docs/examples/filter-cfntype-exclude.png)

```python
{
  name: "excludeCfnType",
  title: "Exclude CfnType Diagram (filter)",
  filterPlan: {
    filters: [
      Filters.excludeCfnType([
        /AWS::EC2::VPC.*/,
        aws_arch.CfnSpec.ServiceResourceDictionary.IAM.Role,
      ]),
      Filters.compact(),
    ],
  },
},
```

</details><details>
<summary>Filter: Include specific graph node types</summary>

[<img src="docs/examples/filter-nodetype-include.png" height="200" />](docs/examples/filter-nodetype-include.png)

```python
{
  name: "includeNodeType",
  title: "Include NodeType Diagram (filter)",
  filterPlan: {
    filters: [
      Filters.includeNodeType([
        NodeTypeEnum.STACK,
        NodeTypeEnum.RESOURCE,
      ]),
      Filters.compact(),
    ],
  },
},
```

</details><details>
<summary>Filter: Include specific graph node types</summary>

[<img src="docs/examples/filter-nodetype-include.png" height="200" />](docs/examples/filter-nodetype-include.png)

```python
{
  name: "includeNodeType",
  title: "Include NodeType Diagram (filter)",
  filterPlan: {
    filters: [
      Filters.includeNodeType([
        NodeTypeEnum.STACK,
        NodeTypeEnum.RESOURCE,
      ]),
      Filters.compact(),
    ],
  },
},
```

</details><details>
<summary>Filter: Exclude specific graph node types</summary>

[<img src="docs/examples/filter-nodetype-exclude.png" height="200" />](docs/examples/filter-nodetype-exclude.png)

```python
{
  name: "excludeNodeType",
  title: "Exclude NodeType Diagram (filter)",
  filterPlan: {
    filters: [
      Filters.excludeNodeType([
        NodeTypeEnum.NESTED_STACK,
        NodeTypeEnum.CFN_RESOURCE,
        NodeTypeEnum.OUTPUT,
        NodeTypeEnum.PARAMETER,
      ]),
      Filters.compact(),
    ],
  },
},
```

</details>

##### **Themes**

<details>
<summary>Theme: Dark</summary>

[<img src="docs/examples/dark.png" height="200" />](docs/examples/dark.png)

```python
{
  name: "Dark",
  title: "Dark Theme Diagram",
  theme: theme,
},
```

</details><details>
<summary>Theme: Dark - render service icons</summary>

[<img src="docs/examples/dark-services.png" height="200" />](docs/examples/dark-services.png)

```python
{
  name: "dark-services",
  title: "Dark Theme Custom Diagram",
  theme: {
    theme: theme,
    rendering: {
      resourceIconMin: GraphThemeRenderingIconTarget.SERVICE,
      resourceIconMax: GraphThemeRenderingIconTarget.CATEGORY,
      cfnResourceIconMin: GraphThemeRenderingIconTarget.DATA,
      cfnResourceIconMax: GraphThemeRenderingIconTarget.RESOURCE,
    },
  },
},
```

</details>
<details>
<summary>Theme: Dark - verbose</summary>

[<img src="docs/examples/dark-verbose.png" height="200" />](docs/examples/dark-verbose.png)

```python
{
  name: "dark-verbose",
  title: "Dark Theme Verbose Diagram",
  ignoreDefaults: true,
  theme: theme,
},
```

</details>---


### Next Steps

* [ ] Battle test in the wild and get community feedback
* [ ] Improve image coverage and non-image node rendering
* [ ] Add drawio support
* [ ] Add common filter patterns and helpers
* [ ] Enable generating diagrams outside of synthesis process (maybe CLI)
* [ ] Implement interactive diagram, with potential for dynamic filtering and config generation
* [ ] Support using interactive diagram as config generator for other plugins (or as separate plugin that depends on this)

---


Inspired by [cdk-dia](https://github.com/pistazie/cdk-dia) and [cfn-dia](https://github.com/mhlabs/cfn-diagram) with ❤️
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

import aws_prototyping_sdk.cdk_graph


@jsii.implements(aws_prototyping_sdk.cdk_graph.ICdkGraphPlugin)
class CdkGraphDiagramPlugin(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-prototyping-sdk/cdk-graph-plugin-diagram.CdkGraphDiagramPlugin",
):
    '''(experimental) CdkGraphDiagramPlugin is a {@link ICdkGraphPlugin CdkGraph Plugin} implementation for generating diagram artifacts from the {@link CdkGraph} framework.

    :stability: experimental
    '''

    def __init__(self, config: typing.Optional["IPluginConfig"] = None) -> None:
        '''
        :param config: -

        :stability: experimental
        '''
        if __debug__:
            def stub(config: typing.Optional[IPluginConfig] = None) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument config", value=config, expected_type=type_hints["config"])
        jsii.create(self.__class__, self, [config])

    @jsii.member(jsii_name="artifactFilename")
    @builtins.classmethod
    def artifact_filename(
        cls,
        name: builtins.str,
        format: "DiagramFormat",
    ) -> builtins.str:
        '''(experimental) Get standardized artifact file name for diagram artifacts.

        :param name: -
        :param format: -

        :stability: experimental
        '''
        if __debug__:
            def stub(name: builtins.str, format: DiagramFormat) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "artifactFilename", [name, format]))

    @jsii.member(jsii_name="artifactId")
    @builtins.classmethod
    def artifact_id(cls, name: builtins.str, format: "DiagramFormat") -> builtins.str:
        '''(experimental) Get standardized artifact id for diagram artifacts.

        :param name: -
        :param format: -

        :stability: experimental
        '''
        if __debug__:
            def stub(name: builtins.str, format: DiagramFormat) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "artifactId", [name, format]))

    @jsii.member(jsii_name="getDiagramArtifact")
    def get_diagram_artifact(
        self,
        name: builtins.str,
        format: "DiagramFormat",
    ) -> typing.Optional[aws_prototyping_sdk.cdk_graph.CdkGraphArtifact]:
        '''(experimental) Get diagram artifact for a given name and format.

        :param name: -
        :param format: -

        :stability: experimental
        '''
        if __debug__:
            def stub(name: builtins.str, format: DiagramFormat) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
        return typing.cast(typing.Optional[aws_prototyping_sdk.cdk_graph.CdkGraphArtifact], jsii.invoke(self, "getDiagramArtifact", [name, format]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ARTIFACT_NS")
    def ARTIFACT_NS(cls) -> builtins.str:
        '''(experimental) Namespace for artifacts of the diagram plugin.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ARTIFACT_NS"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ID")
    def ID(cls) -> builtins.str:
        '''(experimental) Fixed id of the diagram plugin.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "ID"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="VERSION")
    def VERSION(cls) -> builtins.str:
        '''(experimental) Current semantic version of the diagram plugin.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "VERSION"))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> "IPluginConfig":
        '''(experimental) Get diagram plugin config.

        :stability: experimental
        '''
        return typing.cast("IPluginConfig", jsii.get(self, "config"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        '''(experimental) Unique identifier for this plugin.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''(experimental) Plugin version.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="defaultDotArtifact")
    def default_dot_artifact(
        self,
    ) -> typing.Optional[aws_prototyping_sdk.cdk_graph.CdkGraphArtifact]:
        '''(experimental) Get default dot artifact.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_prototyping_sdk.cdk_graph.CdkGraphArtifact], jsii.get(self, "defaultDotArtifact"))

    @builtins.property
    @jsii.member(jsii_name="defaultPngArtifact")
    def default_png_artifact(
        self,
    ) -> typing.Optional[aws_prototyping_sdk.cdk_graph.CdkGraphArtifact]:
        '''(experimental) Get default PNG artifact.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_prototyping_sdk.cdk_graph.CdkGraphArtifact], jsii.get(self, "defaultPngArtifact"))

    @builtins.property
    @jsii.member(jsii_name="dependencies")
    def dependencies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) List of plugins this plugin depends on, including optional semver version (eg: ["foo", "bar@1.2"]).

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dependencies"))

    @builtins.property
    @jsii.member(jsii_name="bind")
    def bind(self) -> aws_prototyping_sdk.cdk_graph.IGraphPluginBindCallback:
        '''(experimental) Binds the plugin to the CdkGraph instance.

        Enables plugins to receive base configs.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(aws_prototyping_sdk.cdk_graph.IGraphPluginBindCallback, jsii.get(self, "bind"))

    @bind.setter
    def bind(
        self,
        value: aws_prototyping_sdk.cdk_graph.IGraphPluginBindCallback,
    ) -> None:
        if __debug__:
            def stub(
                value: aws_prototyping_sdk.cdk_graph.IGraphPluginBindCallback,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bind", value)

    @builtins.property
    @jsii.member(jsii_name="report")
    def report(
        self,
    ) -> typing.Optional[aws_prototyping_sdk.cdk_graph.IGraphReportCallback]:
        '''(experimental) Generate asynchronous reports based on the graph.

        This is not automatically called when synthesizing CDK.
        Developer must explicitly add ``await graphInstance.report()`` to the CDK bin or invoke this outside
        of the CDK synth. In either case, the plugin receives the in-memory graph interface when invoked, as the
        CdkGraph will deserialize the graph prior to invoking the plugin report.

        :stability: experimental
        :inheritdoc: true
        '''
        return typing.cast(typing.Optional[aws_prototyping_sdk.cdk_graph.IGraphReportCallback], jsii.get(self, "report"))

    @report.setter
    def report(
        self,
        value: typing.Optional[aws_prototyping_sdk.cdk_graph.IGraphReportCallback],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[aws_prototyping_sdk.cdk_graph.IGraphReportCallback],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "report", value)


@jsii.enum(jsii_type="@aws-prototyping-sdk/cdk-graph-plugin-diagram.DiagramFormat")
class DiagramFormat(enum.Enum):
    '''(experimental) Supported diagram formats that can be generated.

    Extended formats are automatically generated, for example if you generate "png" which extends
    "svg" which extends "dot", the resulting generated files will be all aforementioned.

    :stability: experimental
    '''

    DOT = "DOT"
    '''(experimental) Graphviz `DOT Language <https://graphviz.org/doc/info/lang.html>`_.

    :stability: experimental
    '''
    SVG = "SVG"
    '''(experimental) `SVG <https://developer.mozilla.org/en-US/docs/Web/SVG>`_ generated using `dot-wasm <https://hpcc-systems.github.io/hpcc-js-wasm/classes/graphviz.Graphviz.html>`_ from {@link DiagramFormat.DOT} file.

    :stability: experimental
    :extends: DiagramFormat.DOT
    '''
    PNG = "PNG"
    '''(experimental) `PNG <https://en.wikipedia.org/wiki/Portable_Network_Graphics>`_ generated using `sharp <https://sharp.pixelplumbing.com/api-output#png>`_ from {@link DiagramFormat.SVG} file.

    :stability: experimental
    :extends: DiagramFormat.SVG
    '''


@jsii.data_type(
    jsii_type="@aws-prototyping-sdk/cdk-graph-plugin-diagram.DiagramOptions",
    jsii_struct_bases=[],
    name_mapping={"title": "title", "preset": "preset", "theme": "theme"},
)
class DiagramOptions:
    def __init__(
        self,
        *,
        title: builtins.str,
        preset: typing.Optional[aws_prototyping_sdk.cdk_graph.FilterPreset] = None,
        theme: typing.Optional[typing.Union[builtins.str, "IGraphThemeConfigAlt"]] = None,
    ) -> None:
        '''(experimental) Options for diagrams.

        :param title: 
        :param preset: 
        :param theme: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                title: builtins.str,
                preset: typing.Optional[aws_prototyping_sdk.cdk_graph.FilterPreset] = None,
                theme: typing.Optional[typing.Union[builtins.str, IGraphThemeConfigAlt]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument preset", value=preset, expected_type=type_hints["preset"])
            check_type(argname="argument theme", value=theme, expected_type=type_hints["theme"])
        self._values: typing.Dict[str, typing.Any] = {
            "title": title,
        }
        if preset is not None:
            self._values["preset"] = preset
        if theme is not None:
            self._values["theme"] = theme

    @builtins.property
    def title(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def preset(self) -> typing.Optional[aws_prototyping_sdk.cdk_graph.FilterPreset]:
        '''
        :stability: experimental
        '''
        result = self._values.get("preset")
        return typing.cast(typing.Optional[aws_prototyping_sdk.cdk_graph.FilterPreset], result)

    @builtins.property
    def theme(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, "IGraphThemeConfigAlt"]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("theme")
        return typing.cast(typing.Optional[typing.Union[builtins.str, "IGraphThemeConfigAlt"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiagramOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@aws-prototyping-sdk/cdk-graph-plugin-diagram.GraphThemeRenderingIconTarget"
)
class GraphThemeRenderingIconTarget(enum.Enum):
    '''(experimental) Icon rendering target options for GraphTheme.

    :stability: experimental
    '''

    DATA = "DATA"
    '''(experimental) Data icon (eg: EC2 instance type icon, T2).

    Resolution precedence: ``data => resource => general => service => category``

    :stability: experimental
    '''
    RESOURCE = "RESOURCE"
    '''(experimental) Resource icon.

    Resolution precedence: ``resource => general => service => category``

    :stability: experimental
    '''
    GENERAL = "GENERAL"
    '''(experimental) General icon.

    Resolution precedence: ``resource => general => service => category``

    :stability: experimental
    '''
    SERVICE = "SERVICE"
    '''(experimental) Service icon.

    Resolution precedence: ``service => category``

    :stability: experimental
    '''
    CATEGORY = "CATEGORY"
    '''(experimental) Category icon.

    Resolution precedence: ``category``

    :stability: experimental
    '''


@jsii.interface(
    jsii_type="@aws-prototyping-sdk/cdk-graph-plugin-diagram.IDiagramConfigBase"
)
class IDiagramConfigBase(typing_extensions.Protocol):
    '''(experimental) Base config to specific a unique diagram to be generated.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="filterPlan")
    def filter_plan(
        self,
    ) -> typing.Optional[aws_prototyping_sdk.cdk_graph.IGraphFilterPlan]:
        '''(experimental) Graph {@link IGraphFilterPlan Filter Plan}  used to generate a unique diagram.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(
        self,
    ) -> typing.Optional[typing.Union[DiagramFormat, typing.List[DiagramFormat]]]:
        '''(experimental) The output format(s) to generated.

        :default: ``DiagramFormat.PNG`` - which will through extension also generate ``DiagramFormat.SVG`` and ``DiagramFormat.DOT``

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="theme")
    def theme(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, "IGraphThemeConfigAlt"]]:
        '''(experimental) Config for graph theme.

        :stability: experimental
        '''
        ...


class _IDiagramConfigBaseProxy:
    '''(experimental) Base config to specific a unique diagram to be generated.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph-plugin-diagram.IDiagramConfigBase"

    @builtins.property
    @jsii.member(jsii_name="filterPlan")
    def filter_plan(
        self,
    ) -> typing.Optional[aws_prototyping_sdk.cdk_graph.IGraphFilterPlan]:
        '''(experimental) Graph {@link IGraphFilterPlan Filter Plan}  used to generate a unique diagram.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[aws_prototyping_sdk.cdk_graph.IGraphFilterPlan], jsii.get(self, "filterPlan"))

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(
        self,
    ) -> typing.Optional[typing.Union[DiagramFormat, typing.List[DiagramFormat]]]:
        '''(experimental) The output format(s) to generated.

        :default: ``DiagramFormat.PNG`` - which will through extension also generate ``DiagramFormat.SVG`` and ``DiagramFormat.DOT``

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Union[DiagramFormat, typing.List[DiagramFormat]]], jsii.get(self, "format"))

    @builtins.property
    @jsii.member(jsii_name="theme")
    def theme(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, "IGraphThemeConfigAlt"]]:
        '''(experimental) Config for graph theme.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.Union[builtins.str, "IGraphThemeConfigAlt"]], jsii.get(self, "theme"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDiagramConfigBase).__jsii_proxy_class__ = lambda : _IDiagramConfigBaseProxy


@jsii.interface(
    jsii_type="@aws-prototyping-sdk/cdk-graph-plugin-diagram.IGraphThemeConfigAlt"
)
class IGraphThemeConfigAlt(typing_extensions.Protocol):
    '''(experimental) GraphThemeConfigAlt is simplified definition of theme to apply.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="rendering")
    def rendering(self) -> typing.Optional["IGraphThemeRendering"]:
        '''
        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="theme")
    def theme(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        ...


class _IGraphThemeConfigAltProxy:
    '''(experimental) GraphThemeConfigAlt is simplified definition of theme to apply.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph-plugin-diagram.IGraphThemeConfigAlt"

    @builtins.property
    @jsii.member(jsii_name="rendering")
    def rendering(self) -> typing.Optional["IGraphThemeRendering"]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional["IGraphThemeRendering"], jsii.get(self, "rendering"))

    @builtins.property
    @jsii.member(jsii_name="theme")
    def theme(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "theme"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphThemeConfigAlt).__jsii_proxy_class__ = lambda : _IGraphThemeConfigAltProxy


@jsii.interface(
    jsii_type="@aws-prototyping-sdk/cdk-graph-plugin-diagram.IGraphThemeRendering"
)
class IGraphThemeRendering(typing_extensions.Protocol):
    '''(experimental) Rending settings for GraphTheme.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cfnResourceIconMax")
    def cfn_resource_icon_max(self) -> GraphThemeRenderingIconTarget:
        '''(experimental) Highest Graph.CfnResourceNode icon to render.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="cfnResourceIconMin")
    def cfn_resource_icon_min(self) -> GraphThemeRenderingIconTarget:
        '''(experimental) Lowest Graph.CfnResourceNode icon to render.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="resourceIconMax")
    def resource_icon_max(self) -> GraphThemeRenderingIconTarget:
        '''(experimental) Highest Graph.ResourceNode icon to render.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="resourceIconMin")
    def resource_icon_min(self) -> GraphThemeRenderingIconTarget:
        '''(experimental) Lowest Graph.ResourceNode icon to render.

        :stability: experimental
        '''
        ...


class _IGraphThemeRenderingProxy:
    '''(experimental) Rending settings for GraphTheme.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph-plugin-diagram.IGraphThemeRendering"

    @builtins.property
    @jsii.member(jsii_name="cfnResourceIconMax")
    def cfn_resource_icon_max(self) -> GraphThemeRenderingIconTarget:
        '''(experimental) Highest Graph.CfnResourceNode icon to render.

        :stability: experimental
        '''
        return typing.cast(GraphThemeRenderingIconTarget, jsii.get(self, "cfnResourceIconMax"))

    @builtins.property
    @jsii.member(jsii_name="cfnResourceIconMin")
    def cfn_resource_icon_min(self) -> GraphThemeRenderingIconTarget:
        '''(experimental) Lowest Graph.CfnResourceNode icon to render.

        :stability: experimental
        '''
        return typing.cast(GraphThemeRenderingIconTarget, jsii.get(self, "cfnResourceIconMin"))

    @builtins.property
    @jsii.member(jsii_name="resourceIconMax")
    def resource_icon_max(self) -> GraphThemeRenderingIconTarget:
        '''(experimental) Highest Graph.ResourceNode icon to render.

        :stability: experimental
        '''
        return typing.cast(GraphThemeRenderingIconTarget, jsii.get(self, "resourceIconMax"))

    @builtins.property
    @jsii.member(jsii_name="resourceIconMin")
    def resource_icon_min(self) -> GraphThemeRenderingIconTarget:
        '''(experimental) Lowest Graph.ResourceNode icon to render.

        :stability: experimental
        '''
        return typing.cast(GraphThemeRenderingIconTarget, jsii.get(self, "resourceIconMin"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphThemeRendering).__jsii_proxy_class__ = lambda : _IGraphThemeRenderingProxy


@jsii.interface(
    jsii_type="@aws-prototyping-sdk/cdk-graph-plugin-diagram.IPluginConfig"
)
class IPluginConfig(typing_extensions.Protocol):
    '''(experimental) Plugin configuration for diagram plugin.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="defaults")
    def defaults(self) -> typing.Optional[IDiagramConfigBase]:
        '''(experimental) Default configuration to apply to all diagrams.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="diagrams")
    def diagrams(self) -> typing.Optional[typing.List["IDiagramConfig"]]:
        '''(experimental) List of diagram configurations to generate diagrams.

        :stability: experimental
        '''
        ...


class _IPluginConfigProxy:
    '''(experimental) Plugin configuration for diagram plugin.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph-plugin-diagram.IPluginConfig"

    @builtins.property
    @jsii.member(jsii_name="defaults")
    def defaults(self) -> typing.Optional[IDiagramConfigBase]:
        '''(experimental) Default configuration to apply to all diagrams.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[IDiagramConfigBase], jsii.get(self, "defaults"))

    @builtins.property
    @jsii.member(jsii_name="diagrams")
    def diagrams(self) -> typing.Optional[typing.List["IDiagramConfig"]]:
        '''(experimental) List of diagram configurations to generate diagrams.

        :stability: experimental
        '''
        return typing.cast(typing.Optional[typing.List["IDiagramConfig"]], jsii.get(self, "diagrams"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPluginConfig).__jsii_proxy_class__ = lambda : _IPluginConfigProxy


@jsii.interface(
    jsii_type="@aws-prototyping-sdk/cdk-graph-plugin-diagram.IDiagramConfig"
)
class IDiagramConfig(IDiagramConfigBase, typing_extensions.Protocol):
    '''(experimental) Diagram configuration definition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) Name of the diagram.

        Used as the basename of the generated file(s) which gets the extension appended.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        '''(experimental) The title of the diagram.

        :stability: experimental
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="ignoreDefaults")
    def ignore_defaults(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates if default diagram config is applied as defaults to this config.

        :default: false

        :stability: experimental
        '''
        ...


class _IDiagramConfigProxy(
    jsii.proxy_for(IDiagramConfigBase), # type: ignore[misc]
):
    '''(experimental) Diagram configuration definition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "@aws-prototyping-sdk/cdk-graph-plugin-diagram.IDiagramConfig"

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(experimental) Name of the diagram.

        Used as the basename of the generated file(s) which gets the extension appended.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        '''(experimental) The title of the diagram.

        :stability: experimental
        '''
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @builtins.property
    @jsii.member(jsii_name="ignoreDefaults")
    def ignore_defaults(self) -> typing.Optional[builtins.bool]:
        '''(experimental) Indicates if default diagram config is applied as defaults to this config.

        :default: false

        :stability: experimental
        '''
        return typing.cast(typing.Optional[builtins.bool], jsii.get(self, "ignoreDefaults"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDiagramConfig).__jsii_proxy_class__ = lambda : _IDiagramConfigProxy


__all__ = [
    "CdkGraphDiagramPlugin",
    "DiagramFormat",
    "DiagramOptions",
    "GraphThemeRenderingIconTarget",
    "IDiagramConfig",
    "IDiagramConfigBase",
    "IGraphThemeConfigAlt",
    "IGraphThemeRendering",
    "IPluginConfig",
]

publication.publish()
