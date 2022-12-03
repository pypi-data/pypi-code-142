'''
# `aws_elastictranscoder_preset`

Refer to the Terraform Registory for docs: [`aws_elastictranscoder_preset`](https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset).
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

from .._jsii import *

import cdktf
import constructs


class ElastictranscoderPreset(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoderPreset.ElastictranscoderPreset",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset aws_elastictranscoder_preset}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        container: builtins.str,
        audio: typing.Optional[typing.Union["ElastictranscoderPresetAudio", typing.Dict[str, typing.Any]]] = None,
        audio_codec_options: typing.Optional[typing.Union["ElastictranscoderPresetAudioCodecOptions", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        thumbnails: typing.Optional[typing.Union["ElastictranscoderPresetThumbnails", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        video: typing.Optional[typing.Union["ElastictranscoderPresetVideo", typing.Dict[str, typing.Any]]] = None,
        video_codec_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        video_watermarks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPresetVideoWatermarks", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset aws_elastictranscoder_preset} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#container ElastictranscoderPreset#container}.
        :param audio: audio block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio ElastictranscoderPreset#audio}
        :param audio_codec_options: audio_codec_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_codec_options ElastictranscoderPreset#audio_codec_options}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#description ElastictranscoderPreset#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#name ElastictranscoderPreset#name}.
        :param thumbnails: thumbnails block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#thumbnails ElastictranscoderPreset#thumbnails}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#type ElastictranscoderPreset#type}.
        :param video: video block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video ElastictranscoderPreset#video}
        :param video_codec_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_codec_options ElastictranscoderPreset#video_codec_options}.
        :param video_watermarks: video_watermarks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_watermarks ElastictranscoderPreset#video_watermarks}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            def stub(
                scope: constructs.Construct,
                id_: builtins.str,
                *,
                container: builtins.str,
                audio: typing.Optional[typing.Union[ElastictranscoderPresetAudio, typing.Dict[str, typing.Any]]] = None,
                audio_codec_options: typing.Optional[typing.Union[ElastictranscoderPresetAudioCodecOptions, typing.Dict[str, typing.Any]]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                thumbnails: typing.Optional[typing.Union[ElastictranscoderPresetThumbnails, typing.Dict[str, typing.Any]]] = None,
                type: typing.Optional[builtins.str] = None,
                video: typing.Optional[typing.Union[ElastictranscoderPresetVideo, typing.Dict[str, typing.Any]]] = None,
                video_codec_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                video_watermarks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastictranscoderPresetVideoWatermarks, typing.Dict[str, typing.Any]]]]] = None,
                connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
                count: typing.Optional[jsii.Number] = None,
                depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
                for_each: typing.Optional[cdktf.ITerraformIterator] = None,
                lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
                provider: typing.Optional[cdktf.TerraformProvider] = None,
                provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ElastictranscoderPresetConfig(
            container=container,
            audio=audio,
            audio_codec_options=audio_codec_options,
            description=description,
            id=id,
            name=name,
            thumbnails=thumbnails,
            type=type,
            video=video,
            video_codec_options=video_codec_options,
            video_watermarks=video_watermarks,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAudio")
    def put_audio(
        self,
        *,
        audio_packing_mode: typing.Optional[builtins.str] = None,
        bit_rate: typing.Optional[builtins.str] = None,
        channels: typing.Optional[builtins.str] = None,
        codec: typing.Optional[builtins.str] = None,
        sample_rate: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audio_packing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_packing_mode ElastictranscoderPreset#audio_packing_mode}.
        :param bit_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.
        :param channels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#channels ElastictranscoderPreset#channels}.
        :param codec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.
        :param sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sample_rate ElastictranscoderPreset#sample_rate}.
        '''
        value = ElastictranscoderPresetAudio(
            audio_packing_mode=audio_packing_mode,
            bit_rate=bit_rate,
            channels=channels,
            codec=codec,
            sample_rate=sample_rate,
        )

        return typing.cast(None, jsii.invoke(self, "putAudio", [value]))

    @jsii.member(jsii_name="putAudioCodecOptions")
    def put_audio_codec_options(
        self,
        *,
        bit_depth: typing.Optional[builtins.str] = None,
        bit_order: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        signed: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bit_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_depth ElastictranscoderPreset#bit_depth}.
        :param bit_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_order ElastictranscoderPreset#bit_order}.
        :param profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#profile ElastictranscoderPreset#profile}.
        :param signed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#signed ElastictranscoderPreset#signed}.
        '''
        value = ElastictranscoderPresetAudioCodecOptions(
            bit_depth=bit_depth, bit_order=bit_order, profile=profile, signed=signed
        )

        return typing.cast(None, jsii.invoke(self, "putAudioCodecOptions", [value]))

    @jsii.member(jsii_name="putThumbnails")
    def put_thumbnails(
        self,
        *,
        aspect_ratio: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
        interval: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        padding_policy: typing.Optional[builtins.str] = None,
        resolution: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#format ElastictranscoderPreset#format}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#interval ElastictranscoderPreset#interval}.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param padding_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.
        :param resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        '''
        value = ElastictranscoderPresetThumbnails(
            aspect_ratio=aspect_ratio,
            format=format,
            interval=interval,
            max_height=max_height,
            max_width=max_width,
            padding_policy=padding_policy,
            resolution=resolution,
            sizing_policy=sizing_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putThumbnails", [value]))

    @jsii.member(jsii_name="putVideo")
    def put_video(
        self,
        *,
        aspect_ratio: typing.Optional[builtins.str] = None,
        bit_rate: typing.Optional[builtins.str] = None,
        codec: typing.Optional[builtins.str] = None,
        display_aspect_ratio: typing.Optional[builtins.str] = None,
        fixed_gop: typing.Optional[builtins.str] = None,
        frame_rate: typing.Optional[builtins.str] = None,
        keyframes_max_dist: typing.Optional[builtins.str] = None,
        max_frame_rate: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        padding_policy: typing.Optional[builtins.str] = None,
        resolution: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.
        :param bit_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.
        :param codec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.
        :param display_aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#display_aspect_ratio ElastictranscoderPreset#display_aspect_ratio}.
        :param fixed_gop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#fixed_gop ElastictranscoderPreset#fixed_gop}.
        :param frame_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#frame_rate ElastictranscoderPreset#frame_rate}.
        :param keyframes_max_dist: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#keyframes_max_dist ElastictranscoderPreset#keyframes_max_dist}.
        :param max_frame_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_frame_rate ElastictranscoderPreset#max_frame_rate}.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param padding_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.
        :param resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        '''
        value = ElastictranscoderPresetVideo(
            aspect_ratio=aspect_ratio,
            bit_rate=bit_rate,
            codec=codec,
            display_aspect_ratio=display_aspect_ratio,
            fixed_gop=fixed_gop,
            frame_rate=frame_rate,
            keyframes_max_dist=keyframes_max_dist,
            max_frame_rate=max_frame_rate,
            max_height=max_height,
            max_width=max_width,
            padding_policy=padding_policy,
            resolution=resolution,
            sizing_policy=sizing_policy,
        )

        return typing.cast(None, jsii.invoke(self, "putVideo", [value]))

    @jsii.member(jsii_name="putVideoWatermarks")
    def put_video_watermarks(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPresetVideoWatermarks", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastictranscoderPresetVideoWatermarks, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putVideoWatermarks", [value]))

    @jsii.member(jsii_name="resetAudio")
    def reset_audio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudio", []))

    @jsii.member(jsii_name="resetAudioCodecOptions")
    def reset_audio_codec_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudioCodecOptions", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetThumbnails")
    def reset_thumbnails(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThumbnails", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetVideo")
    def reset_video(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideo", []))

    @jsii.member(jsii_name="resetVideoCodecOptions")
    def reset_video_codec_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideoCodecOptions", []))

    @jsii.member(jsii_name="resetVideoWatermarks")
    def reset_video_watermarks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVideoWatermarks", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="audio")
    def audio(self) -> "ElastictranscoderPresetAudioOutputReference":
        return typing.cast("ElastictranscoderPresetAudioOutputReference", jsii.get(self, "audio"))

    @builtins.property
    @jsii.member(jsii_name="audioCodecOptions")
    def audio_codec_options(
        self,
    ) -> "ElastictranscoderPresetAudioCodecOptionsOutputReference":
        return typing.cast("ElastictranscoderPresetAudioCodecOptionsOutputReference", jsii.get(self, "audioCodecOptions"))

    @builtins.property
    @jsii.member(jsii_name="thumbnails")
    def thumbnails(self) -> "ElastictranscoderPresetThumbnailsOutputReference":
        return typing.cast("ElastictranscoderPresetThumbnailsOutputReference", jsii.get(self, "thumbnails"))

    @builtins.property
    @jsii.member(jsii_name="video")
    def video(self) -> "ElastictranscoderPresetVideoOutputReference":
        return typing.cast("ElastictranscoderPresetVideoOutputReference", jsii.get(self, "video"))

    @builtins.property
    @jsii.member(jsii_name="videoWatermarks")
    def video_watermarks(self) -> "ElastictranscoderPresetVideoWatermarksList":
        return typing.cast("ElastictranscoderPresetVideoWatermarksList", jsii.get(self, "videoWatermarks"))

    @builtins.property
    @jsii.member(jsii_name="audioCodecOptionsInput")
    def audio_codec_options_input(
        self,
    ) -> typing.Optional["ElastictranscoderPresetAudioCodecOptions"]:
        return typing.cast(typing.Optional["ElastictranscoderPresetAudioCodecOptions"], jsii.get(self, "audioCodecOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="audioInput")
    def audio_input(self) -> typing.Optional["ElastictranscoderPresetAudio"]:
        return typing.cast(typing.Optional["ElastictranscoderPresetAudio"], jsii.get(self, "audioInput"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="thumbnailsInput")
    def thumbnails_input(self) -> typing.Optional["ElastictranscoderPresetThumbnails"]:
        return typing.cast(typing.Optional["ElastictranscoderPresetThumbnails"], jsii.get(self, "thumbnailsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="videoCodecOptionsInput")
    def video_codec_options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "videoCodecOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="videoInput")
    def video_input(self) -> typing.Optional["ElastictranscoderPresetVideo"]:
        return typing.cast(typing.Optional["ElastictranscoderPresetVideo"], jsii.get(self, "videoInput"))

    @builtins.property
    @jsii.member(jsii_name="videoWatermarksInput")
    def video_watermarks_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPresetVideoWatermarks"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPresetVideoWatermarks"]]], jsii.get(self, "videoWatermarksInput"))

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "container"))

    @container.setter
    def container(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "container", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="videoCodecOptions")
    def video_codec_options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "videoCodecOptions"))

    @video_codec_options.setter
    def video_codec_options(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            def stub(value: typing.Mapping[builtins.str, builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "videoCodecOptions", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoderPreset.ElastictranscoderPresetAudio",
    jsii_struct_bases=[],
    name_mapping={
        "audio_packing_mode": "audioPackingMode",
        "bit_rate": "bitRate",
        "channels": "channels",
        "codec": "codec",
        "sample_rate": "sampleRate",
    },
)
class ElastictranscoderPresetAudio:
    def __init__(
        self,
        *,
        audio_packing_mode: typing.Optional[builtins.str] = None,
        bit_rate: typing.Optional[builtins.str] = None,
        channels: typing.Optional[builtins.str] = None,
        codec: typing.Optional[builtins.str] = None,
        sample_rate: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param audio_packing_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_packing_mode ElastictranscoderPreset#audio_packing_mode}.
        :param bit_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.
        :param channels: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#channels ElastictranscoderPreset#channels}.
        :param codec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.
        :param sample_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sample_rate ElastictranscoderPreset#sample_rate}.
        '''
        if __debug__:
            def stub(
                *,
                audio_packing_mode: typing.Optional[builtins.str] = None,
                bit_rate: typing.Optional[builtins.str] = None,
                channels: typing.Optional[builtins.str] = None,
                codec: typing.Optional[builtins.str] = None,
                sample_rate: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument audio_packing_mode", value=audio_packing_mode, expected_type=type_hints["audio_packing_mode"])
            check_type(argname="argument bit_rate", value=bit_rate, expected_type=type_hints["bit_rate"])
            check_type(argname="argument channels", value=channels, expected_type=type_hints["channels"])
            check_type(argname="argument codec", value=codec, expected_type=type_hints["codec"])
            check_type(argname="argument sample_rate", value=sample_rate, expected_type=type_hints["sample_rate"])
        self._values: typing.Dict[str, typing.Any] = {}
        if audio_packing_mode is not None:
            self._values["audio_packing_mode"] = audio_packing_mode
        if bit_rate is not None:
            self._values["bit_rate"] = bit_rate
        if channels is not None:
            self._values["channels"] = channels
        if codec is not None:
            self._values["codec"] = codec
        if sample_rate is not None:
            self._values["sample_rate"] = sample_rate

    @builtins.property
    def audio_packing_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_packing_mode ElastictranscoderPreset#audio_packing_mode}.'''
        result = self._values.get("audio_packing_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bit_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.'''
        result = self._values.get("bit_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def channels(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#channels ElastictranscoderPreset#channels}.'''
        result = self._values.get("channels")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codec(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.'''
        result = self._values.get("codec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sample_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sample_rate ElastictranscoderPreset#sample_rate}.'''
        result = self._values.get("sample_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetAudio(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoderPreset.ElastictranscoderPresetAudioCodecOptions",
    jsii_struct_bases=[],
    name_mapping={
        "bit_depth": "bitDepth",
        "bit_order": "bitOrder",
        "profile": "profile",
        "signed": "signed",
    },
)
class ElastictranscoderPresetAudioCodecOptions:
    def __init__(
        self,
        *,
        bit_depth: typing.Optional[builtins.str] = None,
        bit_order: typing.Optional[builtins.str] = None,
        profile: typing.Optional[builtins.str] = None,
        signed: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bit_depth: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_depth ElastictranscoderPreset#bit_depth}.
        :param bit_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_order ElastictranscoderPreset#bit_order}.
        :param profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#profile ElastictranscoderPreset#profile}.
        :param signed: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#signed ElastictranscoderPreset#signed}.
        '''
        if __debug__:
            def stub(
                *,
                bit_depth: typing.Optional[builtins.str] = None,
                bit_order: typing.Optional[builtins.str] = None,
                profile: typing.Optional[builtins.str] = None,
                signed: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument bit_depth", value=bit_depth, expected_type=type_hints["bit_depth"])
            check_type(argname="argument bit_order", value=bit_order, expected_type=type_hints["bit_order"])
            check_type(argname="argument profile", value=profile, expected_type=type_hints["profile"])
            check_type(argname="argument signed", value=signed, expected_type=type_hints["signed"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bit_depth is not None:
            self._values["bit_depth"] = bit_depth
        if bit_order is not None:
            self._values["bit_order"] = bit_order
        if profile is not None:
            self._values["profile"] = profile
        if signed is not None:
            self._values["signed"] = signed

    @builtins.property
    def bit_depth(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_depth ElastictranscoderPreset#bit_depth}.'''
        result = self._values.get("bit_depth")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bit_order(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_order ElastictranscoderPreset#bit_order}.'''
        result = self._values.get("bit_order")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#profile ElastictranscoderPreset#profile}.'''
        result = self._values.get("profile")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signed(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#signed ElastictranscoderPreset#signed}.'''
        result = self._values.get("signed")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetAudioCodecOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPresetAudioCodecOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoderPreset.ElastictranscoderPresetAudioCodecOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBitDepth")
    def reset_bit_depth(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBitDepth", []))

    @jsii.member(jsii_name="resetBitOrder")
    def reset_bit_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBitOrder", []))

    @jsii.member(jsii_name="resetProfile")
    def reset_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProfile", []))

    @jsii.member(jsii_name="resetSigned")
    def reset_signed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSigned", []))

    @builtins.property
    @jsii.member(jsii_name="bitDepthInput")
    def bit_depth_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bitDepthInput"))

    @builtins.property
    @jsii.member(jsii_name="bitOrderInput")
    def bit_order_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bitOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="profileInput")
    def profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileInput"))

    @builtins.property
    @jsii.member(jsii_name="signedInput")
    def signed_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signedInput"))

    @builtins.property
    @jsii.member(jsii_name="bitDepth")
    def bit_depth(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bitDepth"))

    @bit_depth.setter
    def bit_depth(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bitDepth", value)

    @builtins.property
    @jsii.member(jsii_name="bitOrder")
    def bit_order(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bitOrder"))

    @bit_order.setter
    def bit_order(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bitOrder", value)

    @builtins.property
    @jsii.member(jsii_name="profile")
    def profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "profile"))

    @profile.setter
    def profile(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profile", value)

    @builtins.property
    @jsii.member(jsii_name="signed")
    def signed(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signed"))

    @signed.setter
    def signed(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signed", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ElastictranscoderPresetAudioCodecOptions]:
        return typing.cast(typing.Optional[ElastictranscoderPresetAudioCodecOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPresetAudioCodecOptions],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[ElastictranscoderPresetAudioCodecOptions],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastictranscoderPresetAudioOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoderPreset.ElastictranscoderPresetAudioOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAudioPackingMode")
    def reset_audio_packing_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAudioPackingMode", []))

    @jsii.member(jsii_name="resetBitRate")
    def reset_bit_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBitRate", []))

    @jsii.member(jsii_name="resetChannels")
    def reset_channels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetChannels", []))

    @jsii.member(jsii_name="resetCodec")
    def reset_codec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodec", []))

    @jsii.member(jsii_name="resetSampleRate")
    def reset_sample_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleRate", []))

    @builtins.property
    @jsii.member(jsii_name="audioPackingModeInput")
    def audio_packing_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "audioPackingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="bitRateInput")
    def bit_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bitRateInput"))

    @builtins.property
    @jsii.member(jsii_name="channelsInput")
    def channels_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "channelsInput"))

    @builtins.property
    @jsii.member(jsii_name="codecInput")
    def codec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codecInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleRateInput")
    def sample_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sampleRateInput"))

    @builtins.property
    @jsii.member(jsii_name="audioPackingMode")
    def audio_packing_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "audioPackingMode"))

    @audio_packing_mode.setter
    def audio_packing_mode(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "audioPackingMode", value)

    @builtins.property
    @jsii.member(jsii_name="bitRate")
    def bit_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bitRate"))

    @bit_rate.setter
    def bit_rate(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bitRate", value)

    @builtins.property
    @jsii.member(jsii_name="channels")
    def channels(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "channels"))

    @channels.setter
    def channels(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "channels", value)

    @builtins.property
    @jsii.member(jsii_name="codec")
    def codec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "codec"))

    @codec.setter
    def codec(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codec", value)

    @builtins.property
    @jsii.member(jsii_name="sampleRate")
    def sample_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sampleRate"))

    @sample_rate.setter
    def sample_rate(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleRate", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastictranscoderPresetAudio]:
        return typing.cast(typing.Optional[ElastictranscoderPresetAudio], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPresetAudio],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[ElastictranscoderPresetAudio]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoderPreset.ElastictranscoderPresetConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "container": "container",
        "audio": "audio",
        "audio_codec_options": "audioCodecOptions",
        "description": "description",
        "id": "id",
        "name": "name",
        "thumbnails": "thumbnails",
        "type": "type",
        "video": "video",
        "video_codec_options": "videoCodecOptions",
        "video_watermarks": "videoWatermarks",
    },
)
class ElastictranscoderPresetConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        container: builtins.str,
        audio: typing.Optional[typing.Union[ElastictranscoderPresetAudio, typing.Dict[str, typing.Any]]] = None,
        audio_codec_options: typing.Optional[typing.Union[ElastictranscoderPresetAudioCodecOptions, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        thumbnails: typing.Optional[typing.Union["ElastictranscoderPresetThumbnails", typing.Dict[str, typing.Any]]] = None,
        type: typing.Optional[builtins.str] = None,
        video: typing.Optional[typing.Union["ElastictranscoderPresetVideo", typing.Dict[str, typing.Any]]] = None,
        video_codec_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        video_watermarks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ElastictranscoderPresetVideoWatermarks", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param container: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#container ElastictranscoderPreset#container}.
        :param audio: audio block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio ElastictranscoderPreset#audio}
        :param audio_codec_options: audio_codec_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_codec_options ElastictranscoderPreset#audio_codec_options}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#description ElastictranscoderPreset#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#name ElastictranscoderPreset#name}.
        :param thumbnails: thumbnails block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#thumbnails ElastictranscoderPreset#thumbnails}
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#type ElastictranscoderPreset#type}.
        :param video: video block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video ElastictranscoderPreset#video}
        :param video_codec_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_codec_options ElastictranscoderPreset#video_codec_options}.
        :param video_watermarks: video_watermarks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_watermarks ElastictranscoderPreset#video_watermarks}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(audio, dict):
            audio = ElastictranscoderPresetAudio(**audio)
        if isinstance(audio_codec_options, dict):
            audio_codec_options = ElastictranscoderPresetAudioCodecOptions(**audio_codec_options)
        if isinstance(thumbnails, dict):
            thumbnails = ElastictranscoderPresetThumbnails(**thumbnails)
        if isinstance(video, dict):
            video = ElastictranscoderPresetVideo(**video)
        if __debug__:
            def stub(
                *,
                connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
                count: typing.Optional[jsii.Number] = None,
                depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
                for_each: typing.Optional[cdktf.ITerraformIterator] = None,
                lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
                provider: typing.Optional[cdktf.TerraformProvider] = None,
                provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
                container: builtins.str,
                audio: typing.Optional[typing.Union[ElastictranscoderPresetAudio, typing.Dict[str, typing.Any]]] = None,
                audio_codec_options: typing.Optional[typing.Union[ElastictranscoderPresetAudioCodecOptions, typing.Dict[str, typing.Any]]] = None,
                description: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                name: typing.Optional[builtins.str] = None,
                thumbnails: typing.Optional[typing.Union[ElastictranscoderPresetThumbnails, typing.Dict[str, typing.Any]]] = None,
                type: typing.Optional[builtins.str] = None,
                video: typing.Optional[typing.Union[ElastictranscoderPresetVideo, typing.Dict[str, typing.Any]]] = None,
                video_codec_options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
                video_watermarks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ElastictranscoderPresetVideoWatermarks, typing.Dict[str, typing.Any]]]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument audio", value=audio, expected_type=type_hints["audio"])
            check_type(argname="argument audio_codec_options", value=audio_codec_options, expected_type=type_hints["audio_codec_options"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument thumbnails", value=thumbnails, expected_type=type_hints["thumbnails"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument video", value=video, expected_type=type_hints["video"])
            check_type(argname="argument video_codec_options", value=video_codec_options, expected_type=type_hints["video_codec_options"])
            check_type(argname="argument video_watermarks", value=video_watermarks, expected_type=type_hints["video_watermarks"])
        self._values: typing.Dict[str, typing.Any] = {
            "container": container,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if audio is not None:
            self._values["audio"] = audio
        if audio_codec_options is not None:
            self._values["audio_codec_options"] = audio_codec_options
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if thumbnails is not None:
            self._values["thumbnails"] = thumbnails
        if type is not None:
            self._values["type"] = type
        if video is not None:
            self._values["video"] = video
        if video_codec_options is not None:
            self._values["video_codec_options"] = video_codec_options
        if video_watermarks is not None:
            self._values["video_watermarks"] = video_watermarks

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def container(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#container ElastictranscoderPreset#container}.'''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def audio(self) -> typing.Optional[ElastictranscoderPresetAudio]:
        '''audio block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio ElastictranscoderPreset#audio}
        '''
        result = self._values.get("audio")
        return typing.cast(typing.Optional[ElastictranscoderPresetAudio], result)

    @builtins.property
    def audio_codec_options(
        self,
    ) -> typing.Optional[ElastictranscoderPresetAudioCodecOptions]:
        '''audio_codec_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#audio_codec_options ElastictranscoderPreset#audio_codec_options}
        '''
        result = self._values.get("audio_codec_options")
        return typing.cast(typing.Optional[ElastictranscoderPresetAudioCodecOptions], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#description ElastictranscoderPreset#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#name ElastictranscoderPreset#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def thumbnails(self) -> typing.Optional["ElastictranscoderPresetThumbnails"]:
        '''thumbnails block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#thumbnails ElastictranscoderPreset#thumbnails}
        '''
        result = self._values.get("thumbnails")
        return typing.cast(typing.Optional["ElastictranscoderPresetThumbnails"], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#type ElastictranscoderPreset#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def video(self) -> typing.Optional["ElastictranscoderPresetVideo"]:
        '''video block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video ElastictranscoderPreset#video}
        '''
        result = self._values.get("video")
        return typing.cast(typing.Optional["ElastictranscoderPresetVideo"], result)

    @builtins.property
    def video_codec_options(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_codec_options ElastictranscoderPreset#video_codec_options}.'''
        result = self._values.get("video_codec_options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def video_watermarks(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPresetVideoWatermarks"]]]:
        '''video_watermarks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#video_watermarks ElastictranscoderPreset#video_watermarks}
        '''
        result = self._values.get("video_watermarks")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ElastictranscoderPresetVideoWatermarks"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoderPreset.ElastictranscoderPresetThumbnails",
    jsii_struct_bases=[],
    name_mapping={
        "aspect_ratio": "aspectRatio",
        "format": "format",
        "interval": "interval",
        "max_height": "maxHeight",
        "max_width": "maxWidth",
        "padding_policy": "paddingPolicy",
        "resolution": "resolution",
        "sizing_policy": "sizingPolicy",
    },
)
class ElastictranscoderPresetThumbnails:
    def __init__(
        self,
        *,
        aspect_ratio: typing.Optional[builtins.str] = None,
        format: typing.Optional[builtins.str] = None,
        interval: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        padding_policy: typing.Optional[builtins.str] = None,
        resolution: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.
        :param format: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#format ElastictranscoderPreset#format}.
        :param interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#interval ElastictranscoderPreset#interval}.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param padding_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.
        :param resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        '''
        if __debug__:
            def stub(
                *,
                aspect_ratio: typing.Optional[builtins.str] = None,
                format: typing.Optional[builtins.str] = None,
                interval: typing.Optional[builtins.str] = None,
                max_height: typing.Optional[builtins.str] = None,
                max_width: typing.Optional[builtins.str] = None,
                padding_policy: typing.Optional[builtins.str] = None,
                resolution: typing.Optional[builtins.str] = None,
                sizing_policy: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument aspect_ratio", value=aspect_ratio, expected_type=type_hints["aspect_ratio"])
            check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument max_height", value=max_height, expected_type=type_hints["max_height"])
            check_type(argname="argument max_width", value=max_width, expected_type=type_hints["max_width"])
            check_type(argname="argument padding_policy", value=padding_policy, expected_type=type_hints["padding_policy"])
            check_type(argname="argument resolution", value=resolution, expected_type=type_hints["resolution"])
            check_type(argname="argument sizing_policy", value=sizing_policy, expected_type=type_hints["sizing_policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aspect_ratio is not None:
            self._values["aspect_ratio"] = aspect_ratio
        if format is not None:
            self._values["format"] = format
        if interval is not None:
            self._values["interval"] = interval
        if max_height is not None:
            self._values["max_height"] = max_height
        if max_width is not None:
            self._values["max_width"] = max_width
        if padding_policy is not None:
            self._values["padding_policy"] = padding_policy
        if resolution is not None:
            self._values["resolution"] = resolution
        if sizing_policy is not None:
            self._values["sizing_policy"] = sizing_policy

    @builtins.property
    def aspect_ratio(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.'''
        result = self._values.get("aspect_ratio")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def format(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#format ElastictranscoderPreset#format}.'''
        result = self._values.get("format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interval(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#interval ElastictranscoderPreset#interval}.'''
        result = self._values.get("interval")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_height(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.'''
        result = self._values.get("max_height")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_width(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.'''
        result = self._values.get("max_width")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def padding_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.'''
        result = self._values.get("padding_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolution(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.'''
        result = self._values.get("resolution")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sizing_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.'''
        result = self._values.get("sizing_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetThumbnails(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPresetThumbnailsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoderPreset.ElastictranscoderPresetThumbnailsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAspectRatio")
    def reset_aspect_ratio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAspectRatio", []))

    @jsii.member(jsii_name="resetFormat")
    def reset_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFormat", []))

    @jsii.member(jsii_name="resetInterval")
    def reset_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterval", []))

    @jsii.member(jsii_name="resetMaxHeight")
    def reset_max_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxHeight", []))

    @jsii.member(jsii_name="resetMaxWidth")
    def reset_max_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWidth", []))

    @jsii.member(jsii_name="resetPaddingPolicy")
    def reset_padding_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPaddingPolicy", []))

    @jsii.member(jsii_name="resetResolution")
    def reset_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResolution", []))

    @jsii.member(jsii_name="resetSizingPolicy")
    def reset_sizing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizingPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="aspectRatioInput")
    def aspect_ratio_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aspectRatioInput"))

    @builtins.property
    @jsii.member(jsii_name="formatInput")
    def format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formatInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="maxHeightInput")
    def max_height_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxHeightInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWidthInput")
    def max_width_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxWidthInput"))

    @builtins.property
    @jsii.member(jsii_name="paddingPolicyInput")
    def padding_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "paddingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="resolutionInput")
    def resolution_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="sizingPolicyInput")
    def sizing_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="aspectRatio")
    def aspect_ratio(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aspectRatio"))

    @aspect_ratio.setter
    def aspect_ratio(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aspectRatio", value)

    @builtins.property
    @jsii.member(jsii_name="format")
    def format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "format"))

    @format.setter
    def format(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "format", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="maxHeight")
    def max_height(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxHeight"))

    @max_height.setter
    def max_height(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxHeight", value)

    @builtins.property
    @jsii.member(jsii_name="maxWidth")
    def max_width(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxWidth"))

    @max_width.setter
    def max_width(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWidth", value)

    @builtins.property
    @jsii.member(jsii_name="paddingPolicy")
    def padding_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "paddingPolicy"))

    @padding_policy.setter
    def padding_policy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paddingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="resolution")
    def resolution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resolution"))

    @resolution.setter
    def resolution(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolution", value)

    @builtins.property
    @jsii.member(jsii_name="sizingPolicy")
    def sizing_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sizingPolicy"))

    @sizing_policy.setter
    def sizing_policy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastictranscoderPresetThumbnails]:
        return typing.cast(typing.Optional[ElastictranscoderPresetThumbnails], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPresetThumbnails],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[ElastictranscoderPresetThumbnails]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoderPreset.ElastictranscoderPresetVideo",
    jsii_struct_bases=[],
    name_mapping={
        "aspect_ratio": "aspectRatio",
        "bit_rate": "bitRate",
        "codec": "codec",
        "display_aspect_ratio": "displayAspectRatio",
        "fixed_gop": "fixedGop",
        "frame_rate": "frameRate",
        "keyframes_max_dist": "keyframesMaxDist",
        "max_frame_rate": "maxFrameRate",
        "max_height": "maxHeight",
        "max_width": "maxWidth",
        "padding_policy": "paddingPolicy",
        "resolution": "resolution",
        "sizing_policy": "sizingPolicy",
    },
)
class ElastictranscoderPresetVideo:
    def __init__(
        self,
        *,
        aspect_ratio: typing.Optional[builtins.str] = None,
        bit_rate: typing.Optional[builtins.str] = None,
        codec: typing.Optional[builtins.str] = None,
        display_aspect_ratio: typing.Optional[builtins.str] = None,
        fixed_gop: typing.Optional[builtins.str] = None,
        frame_rate: typing.Optional[builtins.str] = None,
        keyframes_max_dist: typing.Optional[builtins.str] = None,
        max_frame_rate: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        padding_policy: typing.Optional[builtins.str] = None,
        resolution: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.
        :param bit_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.
        :param codec: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.
        :param display_aspect_ratio: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#display_aspect_ratio ElastictranscoderPreset#display_aspect_ratio}.
        :param fixed_gop: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#fixed_gop ElastictranscoderPreset#fixed_gop}.
        :param frame_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#frame_rate ElastictranscoderPreset#frame_rate}.
        :param keyframes_max_dist: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#keyframes_max_dist ElastictranscoderPreset#keyframes_max_dist}.
        :param max_frame_rate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_frame_rate ElastictranscoderPreset#max_frame_rate}.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param padding_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.
        :param resolution: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        '''
        if __debug__:
            def stub(
                *,
                aspect_ratio: typing.Optional[builtins.str] = None,
                bit_rate: typing.Optional[builtins.str] = None,
                codec: typing.Optional[builtins.str] = None,
                display_aspect_ratio: typing.Optional[builtins.str] = None,
                fixed_gop: typing.Optional[builtins.str] = None,
                frame_rate: typing.Optional[builtins.str] = None,
                keyframes_max_dist: typing.Optional[builtins.str] = None,
                max_frame_rate: typing.Optional[builtins.str] = None,
                max_height: typing.Optional[builtins.str] = None,
                max_width: typing.Optional[builtins.str] = None,
                padding_policy: typing.Optional[builtins.str] = None,
                resolution: typing.Optional[builtins.str] = None,
                sizing_policy: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument aspect_ratio", value=aspect_ratio, expected_type=type_hints["aspect_ratio"])
            check_type(argname="argument bit_rate", value=bit_rate, expected_type=type_hints["bit_rate"])
            check_type(argname="argument codec", value=codec, expected_type=type_hints["codec"])
            check_type(argname="argument display_aspect_ratio", value=display_aspect_ratio, expected_type=type_hints["display_aspect_ratio"])
            check_type(argname="argument fixed_gop", value=fixed_gop, expected_type=type_hints["fixed_gop"])
            check_type(argname="argument frame_rate", value=frame_rate, expected_type=type_hints["frame_rate"])
            check_type(argname="argument keyframes_max_dist", value=keyframes_max_dist, expected_type=type_hints["keyframes_max_dist"])
            check_type(argname="argument max_frame_rate", value=max_frame_rate, expected_type=type_hints["max_frame_rate"])
            check_type(argname="argument max_height", value=max_height, expected_type=type_hints["max_height"])
            check_type(argname="argument max_width", value=max_width, expected_type=type_hints["max_width"])
            check_type(argname="argument padding_policy", value=padding_policy, expected_type=type_hints["padding_policy"])
            check_type(argname="argument resolution", value=resolution, expected_type=type_hints["resolution"])
            check_type(argname="argument sizing_policy", value=sizing_policy, expected_type=type_hints["sizing_policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aspect_ratio is not None:
            self._values["aspect_ratio"] = aspect_ratio
        if bit_rate is not None:
            self._values["bit_rate"] = bit_rate
        if codec is not None:
            self._values["codec"] = codec
        if display_aspect_ratio is not None:
            self._values["display_aspect_ratio"] = display_aspect_ratio
        if fixed_gop is not None:
            self._values["fixed_gop"] = fixed_gop
        if frame_rate is not None:
            self._values["frame_rate"] = frame_rate
        if keyframes_max_dist is not None:
            self._values["keyframes_max_dist"] = keyframes_max_dist
        if max_frame_rate is not None:
            self._values["max_frame_rate"] = max_frame_rate
        if max_height is not None:
            self._values["max_height"] = max_height
        if max_width is not None:
            self._values["max_width"] = max_width
        if padding_policy is not None:
            self._values["padding_policy"] = padding_policy
        if resolution is not None:
            self._values["resolution"] = resolution
        if sizing_policy is not None:
            self._values["sizing_policy"] = sizing_policy

    @builtins.property
    def aspect_ratio(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#aspect_ratio ElastictranscoderPreset#aspect_ratio}.'''
        result = self._values.get("aspect_ratio")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bit_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#bit_rate ElastictranscoderPreset#bit_rate}.'''
        result = self._values.get("bit_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def codec(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#codec ElastictranscoderPreset#codec}.'''
        result = self._values.get("codec")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_aspect_ratio(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#display_aspect_ratio ElastictranscoderPreset#display_aspect_ratio}.'''
        result = self._values.get("display_aspect_ratio")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fixed_gop(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#fixed_gop ElastictranscoderPreset#fixed_gop}.'''
        result = self._values.get("fixed_gop")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def frame_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#frame_rate ElastictranscoderPreset#frame_rate}.'''
        result = self._values.get("frame_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keyframes_max_dist(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#keyframes_max_dist ElastictranscoderPreset#keyframes_max_dist}.'''
        result = self._values.get("keyframes_max_dist")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_frame_rate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_frame_rate ElastictranscoderPreset#max_frame_rate}.'''
        result = self._values.get("max_frame_rate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_height(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.'''
        result = self._values.get("max_height")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_width(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.'''
        result = self._values.get("max_width")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def padding_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#padding_policy ElastictranscoderPreset#padding_policy}.'''
        result = self._values.get("padding_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolution(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#resolution ElastictranscoderPreset#resolution}.'''
        result = self._values.get("resolution")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sizing_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.'''
        result = self._values.get("sizing_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetVideo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPresetVideoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoderPreset.ElastictranscoderPresetVideoOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAspectRatio")
    def reset_aspect_ratio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAspectRatio", []))

    @jsii.member(jsii_name="resetBitRate")
    def reset_bit_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBitRate", []))

    @jsii.member(jsii_name="resetCodec")
    def reset_codec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodec", []))

    @jsii.member(jsii_name="resetDisplayAspectRatio")
    def reset_display_aspect_ratio(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayAspectRatio", []))

    @jsii.member(jsii_name="resetFixedGop")
    def reset_fixed_gop(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFixedGop", []))

    @jsii.member(jsii_name="resetFrameRate")
    def reset_frame_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFrameRate", []))

    @jsii.member(jsii_name="resetKeyframesMaxDist")
    def reset_keyframes_max_dist(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyframesMaxDist", []))

    @jsii.member(jsii_name="resetMaxFrameRate")
    def reset_max_frame_rate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxFrameRate", []))

    @jsii.member(jsii_name="resetMaxHeight")
    def reset_max_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxHeight", []))

    @jsii.member(jsii_name="resetMaxWidth")
    def reset_max_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWidth", []))

    @jsii.member(jsii_name="resetPaddingPolicy")
    def reset_padding_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPaddingPolicy", []))

    @jsii.member(jsii_name="resetResolution")
    def reset_resolution(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResolution", []))

    @jsii.member(jsii_name="resetSizingPolicy")
    def reset_sizing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizingPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="aspectRatioInput")
    def aspect_ratio_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "aspectRatioInput"))

    @builtins.property
    @jsii.member(jsii_name="bitRateInput")
    def bit_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bitRateInput"))

    @builtins.property
    @jsii.member(jsii_name="codecInput")
    def codec_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codecInput"))

    @builtins.property
    @jsii.member(jsii_name="displayAspectRatioInput")
    def display_aspect_ratio_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayAspectRatioInput"))

    @builtins.property
    @jsii.member(jsii_name="fixedGopInput")
    def fixed_gop_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fixedGopInput"))

    @builtins.property
    @jsii.member(jsii_name="frameRateInput")
    def frame_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frameRateInput"))

    @builtins.property
    @jsii.member(jsii_name="keyframesMaxDistInput")
    def keyframes_max_dist_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyframesMaxDistInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFrameRateInput")
    def max_frame_rate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxFrameRateInput"))

    @builtins.property
    @jsii.member(jsii_name="maxHeightInput")
    def max_height_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxHeightInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWidthInput")
    def max_width_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxWidthInput"))

    @builtins.property
    @jsii.member(jsii_name="paddingPolicyInput")
    def padding_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "paddingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="resolutionInput")
    def resolution_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resolutionInput"))

    @builtins.property
    @jsii.member(jsii_name="sizingPolicyInput")
    def sizing_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="aspectRatio")
    def aspect_ratio(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "aspectRatio"))

    @aspect_ratio.setter
    def aspect_ratio(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aspectRatio", value)

    @builtins.property
    @jsii.member(jsii_name="bitRate")
    def bit_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bitRate"))

    @bit_rate.setter
    def bit_rate(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bitRate", value)

    @builtins.property
    @jsii.member(jsii_name="codec")
    def codec(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "codec"))

    @codec.setter
    def codec(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codec", value)

    @builtins.property
    @jsii.member(jsii_name="displayAspectRatio")
    def display_aspect_ratio(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayAspectRatio"))

    @display_aspect_ratio.setter
    def display_aspect_ratio(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayAspectRatio", value)

    @builtins.property
    @jsii.member(jsii_name="fixedGop")
    def fixed_gop(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fixedGop"))

    @fixed_gop.setter
    def fixed_gop(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fixedGop", value)

    @builtins.property
    @jsii.member(jsii_name="frameRate")
    def frame_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frameRate"))

    @frame_rate.setter
    def frame_rate(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frameRate", value)

    @builtins.property
    @jsii.member(jsii_name="keyframesMaxDist")
    def keyframes_max_dist(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyframesMaxDist"))

    @keyframes_max_dist.setter
    def keyframes_max_dist(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyframesMaxDist", value)

    @builtins.property
    @jsii.member(jsii_name="maxFrameRate")
    def max_frame_rate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxFrameRate"))

    @max_frame_rate.setter
    def max_frame_rate(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFrameRate", value)

    @builtins.property
    @jsii.member(jsii_name="maxHeight")
    def max_height(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxHeight"))

    @max_height.setter
    def max_height(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxHeight", value)

    @builtins.property
    @jsii.member(jsii_name="maxWidth")
    def max_width(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxWidth"))

    @max_width.setter
    def max_width(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWidth", value)

    @builtins.property
    @jsii.member(jsii_name="paddingPolicy")
    def padding_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "paddingPolicy"))

    @padding_policy.setter
    def padding_policy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "paddingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="resolution")
    def resolution(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resolution"))

    @resolution.setter
    def resolution(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolution", value)

    @builtins.property
    @jsii.member(jsii_name="sizingPolicy")
    def sizing_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sizingPolicy"))

    @sizing_policy.setter
    def sizing_policy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ElastictranscoderPresetVideo]:
        return typing.cast(typing.Optional[ElastictranscoderPresetVideo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ElastictranscoderPresetVideo],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[ElastictranscoderPresetVideo]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.elastictranscoderPreset.ElastictranscoderPresetVideoWatermarks",
    jsii_struct_bases=[],
    name_mapping={
        "horizontal_align": "horizontalAlign",
        "horizontal_offset": "horizontalOffset",
        "id": "id",
        "max_height": "maxHeight",
        "max_width": "maxWidth",
        "opacity": "opacity",
        "sizing_policy": "sizingPolicy",
        "target": "target",
        "vertical_align": "verticalAlign",
        "vertical_offset": "verticalOffset",
    },
)
class ElastictranscoderPresetVideoWatermarks:
    def __init__(
        self,
        *,
        horizontal_align: typing.Optional[builtins.str] = None,
        horizontal_offset: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        max_height: typing.Optional[builtins.str] = None,
        max_width: typing.Optional[builtins.str] = None,
        opacity: typing.Optional[builtins.str] = None,
        sizing_policy: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        vertical_align: typing.Optional[builtins.str] = None,
        vertical_offset: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param horizontal_align: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#horizontal_align ElastictranscoderPreset#horizontal_align}.
        :param horizontal_offset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#horizontal_offset ElastictranscoderPreset#horizontal_offset}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param max_height: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.
        :param max_width: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.
        :param opacity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#opacity ElastictranscoderPreset#opacity}.
        :param sizing_policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#target ElastictranscoderPreset#target}.
        :param vertical_align: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#vertical_align ElastictranscoderPreset#vertical_align}.
        :param vertical_offset: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#vertical_offset ElastictranscoderPreset#vertical_offset}.
        '''
        if __debug__:
            def stub(
                *,
                horizontal_align: typing.Optional[builtins.str] = None,
                horizontal_offset: typing.Optional[builtins.str] = None,
                id: typing.Optional[builtins.str] = None,
                max_height: typing.Optional[builtins.str] = None,
                max_width: typing.Optional[builtins.str] = None,
                opacity: typing.Optional[builtins.str] = None,
                sizing_policy: typing.Optional[builtins.str] = None,
                target: typing.Optional[builtins.str] = None,
                vertical_align: typing.Optional[builtins.str] = None,
                vertical_offset: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument horizontal_align", value=horizontal_align, expected_type=type_hints["horizontal_align"])
            check_type(argname="argument horizontal_offset", value=horizontal_offset, expected_type=type_hints["horizontal_offset"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument max_height", value=max_height, expected_type=type_hints["max_height"])
            check_type(argname="argument max_width", value=max_width, expected_type=type_hints["max_width"])
            check_type(argname="argument opacity", value=opacity, expected_type=type_hints["opacity"])
            check_type(argname="argument sizing_policy", value=sizing_policy, expected_type=type_hints["sizing_policy"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument vertical_align", value=vertical_align, expected_type=type_hints["vertical_align"])
            check_type(argname="argument vertical_offset", value=vertical_offset, expected_type=type_hints["vertical_offset"])
        self._values: typing.Dict[str, typing.Any] = {}
        if horizontal_align is not None:
            self._values["horizontal_align"] = horizontal_align
        if horizontal_offset is not None:
            self._values["horizontal_offset"] = horizontal_offset
        if id is not None:
            self._values["id"] = id
        if max_height is not None:
            self._values["max_height"] = max_height
        if max_width is not None:
            self._values["max_width"] = max_width
        if opacity is not None:
            self._values["opacity"] = opacity
        if sizing_policy is not None:
            self._values["sizing_policy"] = sizing_policy
        if target is not None:
            self._values["target"] = target
        if vertical_align is not None:
            self._values["vertical_align"] = vertical_align
        if vertical_offset is not None:
            self._values["vertical_offset"] = vertical_offset

    @builtins.property
    def horizontal_align(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#horizontal_align ElastictranscoderPreset#horizontal_align}.'''
        result = self._values.get("horizontal_align")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def horizontal_offset(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#horizontal_offset ElastictranscoderPreset#horizontal_offset}.'''
        result = self._values.get("horizontal_offset")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#id ElastictranscoderPreset#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_height(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_height ElastictranscoderPreset#max_height}.'''
        result = self._values.get("max_height")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_width(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#max_width ElastictranscoderPreset#max_width}.'''
        result = self._values.get("max_width")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def opacity(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#opacity ElastictranscoderPreset#opacity}.'''
        result = self._values.get("opacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sizing_policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#sizing_policy ElastictranscoderPreset#sizing_policy}.'''
        result = self._values.get("sizing_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#target ElastictranscoderPreset#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vertical_align(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#vertical_align ElastictranscoderPreset#vertical_align}.'''
        result = self._values.get("vertical_align")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vertical_offset(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/elastictranscoder_preset#vertical_offset ElastictranscoderPreset#vertical_offset}.'''
        result = self._values.get("vertical_offset")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ElastictranscoderPresetVideoWatermarks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ElastictranscoderPresetVideoWatermarksList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoderPreset.ElastictranscoderPresetVideoWatermarksList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                wraps_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ElastictranscoderPresetVideoWatermarksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ElastictranscoderPresetVideoWatermarksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            def stub(value: cdktf.IInterpolatingParent) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            def stub(value: builtins.bool) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastictranscoderPresetVideoWatermarks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastictranscoderPresetVideoWatermarks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastictranscoderPresetVideoWatermarks]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ElastictranscoderPresetVideoWatermarks]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ElastictranscoderPresetVideoWatermarksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.elastictranscoderPreset.ElastictranscoderPresetVideoWatermarksOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            def stub(
                terraform_resource: cdktf.IInterpolatingParent,
                terraform_attribute: builtins.str,
                complex_object_index: jsii.Number,
                complex_object_is_from_set: builtins.bool,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetHorizontalAlign")
    def reset_horizontal_align(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHorizontalAlign", []))

    @jsii.member(jsii_name="resetHorizontalOffset")
    def reset_horizontal_offset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHorizontalOffset", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMaxHeight")
    def reset_max_height(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxHeight", []))

    @jsii.member(jsii_name="resetMaxWidth")
    def reset_max_width(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxWidth", []))

    @jsii.member(jsii_name="resetOpacity")
    def reset_opacity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOpacity", []))

    @jsii.member(jsii_name="resetSizingPolicy")
    def reset_sizing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSizingPolicy", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetVerticalAlign")
    def reset_vertical_align(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerticalAlign", []))

    @jsii.member(jsii_name="resetVerticalOffset")
    def reset_vertical_offset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerticalOffset", []))

    @builtins.property
    @jsii.member(jsii_name="horizontalAlignInput")
    def horizontal_align_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "horizontalAlignInput"))

    @builtins.property
    @jsii.member(jsii_name="horizontalOffsetInput")
    def horizontal_offset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "horizontalOffsetInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="maxHeightInput")
    def max_height_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxHeightInput"))

    @builtins.property
    @jsii.member(jsii_name="maxWidthInput")
    def max_width_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxWidthInput"))

    @builtins.property
    @jsii.member(jsii_name="opacityInput")
    def opacity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "opacityInput"))

    @builtins.property
    @jsii.member(jsii_name="sizingPolicyInput")
    def sizing_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sizingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="verticalAlignInput")
    def vertical_align_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "verticalAlignInput"))

    @builtins.property
    @jsii.member(jsii_name="verticalOffsetInput")
    def vertical_offset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "verticalOffsetInput"))

    @builtins.property
    @jsii.member(jsii_name="horizontalAlign")
    def horizontal_align(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "horizontalAlign"))

    @horizontal_align.setter
    def horizontal_align(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "horizontalAlign", value)

    @builtins.property
    @jsii.member(jsii_name="horizontalOffset")
    def horizontal_offset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "horizontalOffset"))

    @horizontal_offset.setter
    def horizontal_offset(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "horizontalOffset", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="maxHeight")
    def max_height(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxHeight"))

    @max_height.setter
    def max_height(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxHeight", value)

    @builtins.property
    @jsii.member(jsii_name="maxWidth")
    def max_width(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxWidth"))

    @max_width.setter
    def max_width(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxWidth", value)

    @builtins.property
    @jsii.member(jsii_name="opacity")
    def opacity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "opacity"))

    @opacity.setter
    def opacity(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "opacity", value)

    @builtins.property
    @jsii.member(jsii_name="sizingPolicy")
    def sizing_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sizingPolicy"))

    @sizing_policy.setter
    def sizing_policy(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sizingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="verticalAlign")
    def vertical_align(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "verticalAlign"))

    @vertical_align.setter
    def vertical_align(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verticalAlign", value)

    @builtins.property
    @jsii.member(jsii_name="verticalOffset")
    def vertical_offset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "verticalOffset"))

    @vertical_offset.setter
    def vertical_offset(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verticalOffset", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ElastictranscoderPresetVideoWatermarks, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ElastictranscoderPresetVideoWatermarks, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ElastictranscoderPresetVideoWatermarks, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[ElastictranscoderPresetVideoWatermarks, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ElastictranscoderPreset",
    "ElastictranscoderPresetAudio",
    "ElastictranscoderPresetAudioCodecOptions",
    "ElastictranscoderPresetAudioCodecOptionsOutputReference",
    "ElastictranscoderPresetAudioOutputReference",
    "ElastictranscoderPresetConfig",
    "ElastictranscoderPresetThumbnails",
    "ElastictranscoderPresetThumbnailsOutputReference",
    "ElastictranscoderPresetVideo",
    "ElastictranscoderPresetVideoOutputReference",
    "ElastictranscoderPresetVideoWatermarks",
    "ElastictranscoderPresetVideoWatermarksList",
    "ElastictranscoderPresetVideoWatermarksOutputReference",
]

publication.publish()
