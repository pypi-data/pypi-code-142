'''
# `aws_lex_intent`

Refer to the Terraform Registory for docs: [`aws_lex_intent`](https://www.terraform.io/docs/providers/aws/r/lex_intent).
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


class LexIntent(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntent",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/aws/r/lex_intent aws_lex_intent}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        fulfillment_activity: typing.Union["LexIntentFulfillmentActivity", typing.Dict[str, typing.Any]],
        name: builtins.str,
        conclusion_statement: typing.Optional[typing.Union["LexIntentConclusionStatement", typing.Dict[str, typing.Any]]] = None,
        confirmation_prompt: typing.Optional[typing.Union["LexIntentConfirmationPrompt", typing.Dict[str, typing.Any]]] = None,
        create_version: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        dialog_code_hook: typing.Optional[typing.Union["LexIntentDialogCodeHook", typing.Dict[str, typing.Any]]] = None,
        follow_up_prompt: typing.Optional[typing.Union["LexIntentFollowUpPrompt", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        parent_intent_signature: typing.Optional[builtins.str] = None,
        rejection_statement: typing.Optional[typing.Union["LexIntentRejectionStatement", typing.Dict[str, typing.Any]]] = None,
        sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
        slot: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentSlot", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["LexIntentTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/aws/r/lex_intent aws_lex_intent} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param fulfillment_activity: fulfillment_activity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#fulfillment_activity LexIntent#fulfillment_activity}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.
        :param conclusion_statement: conclusion_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#conclusion_statement LexIntent#conclusion_statement}
        :param confirmation_prompt: confirmation_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#confirmation_prompt LexIntent#confirmation_prompt}
        :param create_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create_version LexIntent#create_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.
        :param dialog_code_hook: dialog_code_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#dialog_code_hook LexIntent#dialog_code_hook}
        :param follow_up_prompt: follow_up_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#follow_up_prompt LexIntent#follow_up_prompt}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#id LexIntent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parent_intent_signature: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#parent_intent_signature LexIntent#parent_intent_signature}.
        :param rejection_statement: rejection_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        :param sample_utterances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.
        :param slot: slot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot LexIntent#slot}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#timeouts LexIntent#timeouts}
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
                fulfillment_activity: typing.Union[LexIntentFulfillmentActivity, typing.Dict[str, typing.Any]],
                name: builtins.str,
                conclusion_statement: typing.Optional[typing.Union[LexIntentConclusionStatement, typing.Dict[str, typing.Any]]] = None,
                confirmation_prompt: typing.Optional[typing.Union[LexIntentConfirmationPrompt, typing.Dict[str, typing.Any]]] = None,
                create_version: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                description: typing.Optional[builtins.str] = None,
                dialog_code_hook: typing.Optional[typing.Union[LexIntentDialogCodeHook, typing.Dict[str, typing.Any]]] = None,
                follow_up_prompt: typing.Optional[typing.Union[LexIntentFollowUpPrompt, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                parent_intent_signature: typing.Optional[builtins.str] = None,
                rejection_statement: typing.Optional[typing.Union[LexIntentRejectionStatement, typing.Dict[str, typing.Any]]] = None,
                sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
                slot: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentSlot, typing.Dict[str, typing.Any]]]]] = None,
                timeouts: typing.Optional[typing.Union[LexIntentTimeouts, typing.Dict[str, typing.Any]]] = None,
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
        config = LexIntentConfig(
            fulfillment_activity=fulfillment_activity,
            name=name,
            conclusion_statement=conclusion_statement,
            confirmation_prompt=confirmation_prompt,
            create_version=create_version,
            description=description,
            dialog_code_hook=dialog_code_hook,
            follow_up_prompt=follow_up_prompt,
            id=id,
            parent_intent_signature=parent_intent_signature,
            rejection_statement=rejection_statement,
            sample_utterances=sample_utterances,
            slot=slot,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putConclusionStatement")
    def put_conclusion_statement(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentConclusionStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentConclusionStatement(
            message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putConclusionStatement", [value]))

    @jsii.member(jsii_name="putConfirmationPrompt")
    def put_confirmation_prompt(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentConfirmationPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentConfirmationPrompt(
            max_attempts=max_attempts, message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putConfirmationPrompt", [value]))

    @jsii.member(jsii_name="putDialogCodeHook")
    def put_dialog_code_hook(
        self,
        *,
        message_version: builtins.str,
        uri: builtins.str,
    ) -> None:
        '''
        :param message_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.
        '''
        value = LexIntentDialogCodeHook(message_version=message_version, uri=uri)

        return typing.cast(None, jsii.invoke(self, "putDialogCodeHook", [value]))

    @jsii.member(jsii_name="putFollowUpPrompt")
    def put_follow_up_prompt(
        self,
        *,
        prompt: typing.Union["LexIntentFollowUpPromptPrompt", typing.Dict[str, typing.Any]],
        rejection_statement: typing.Union["LexIntentFollowUpPromptRejectionStatement", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param prompt: prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#prompt LexIntent#prompt}
        :param rejection_statement: rejection_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        '''
        value = LexIntentFollowUpPrompt(
            prompt=prompt, rejection_statement=rejection_statement
        )

        return typing.cast(None, jsii.invoke(self, "putFollowUpPrompt", [value]))

    @jsii.member(jsii_name="putFulfillmentActivity")
    def put_fulfillment_activity(
        self,
        *,
        type: builtins.str,
        code_hook: typing.Optional[typing.Union["LexIntentFulfillmentActivityCodeHook", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#type LexIntent#type}.
        :param code_hook: code_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#code_hook LexIntent#code_hook}
        '''
        value = LexIntentFulfillmentActivity(type=type, code_hook=code_hook)

        return typing.cast(None, jsii.invoke(self, "putFulfillmentActivity", [value]))

    @jsii.member(jsii_name="putRejectionStatement")
    def put_rejection_statement(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentRejectionStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentRejectionStatement(
            message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putRejectionStatement", [value]))

    @jsii.member(jsii_name="putSlot")
    def put_slot(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentSlot", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentSlot, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSlot", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create LexIntent#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#delete LexIntent#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#update LexIntent#update}.
        '''
        value = LexIntentTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetConclusionStatement")
    def reset_conclusion_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConclusionStatement", []))

    @jsii.member(jsii_name="resetConfirmationPrompt")
    def reset_confirmation_prompt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfirmationPrompt", []))

    @jsii.member(jsii_name="resetCreateVersion")
    def reset_create_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateVersion", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDialogCodeHook")
    def reset_dialog_code_hook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDialogCodeHook", []))

    @jsii.member(jsii_name="resetFollowUpPrompt")
    def reset_follow_up_prompt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFollowUpPrompt", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParentIntentSignature")
    def reset_parent_intent_signature(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParentIntentSignature", []))

    @jsii.member(jsii_name="resetRejectionStatement")
    def reset_rejection_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRejectionStatement", []))

    @jsii.member(jsii_name="resetSampleUtterances")
    def reset_sample_utterances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleUtterances", []))

    @jsii.member(jsii_name="resetSlot")
    def reset_slot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlot", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

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
    @jsii.member(jsii_name="checksum")
    def checksum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "checksum"))

    @builtins.property
    @jsii.member(jsii_name="conclusionStatement")
    def conclusion_statement(self) -> "LexIntentConclusionStatementOutputReference":
        return typing.cast("LexIntentConclusionStatementOutputReference", jsii.get(self, "conclusionStatement"))

    @builtins.property
    @jsii.member(jsii_name="confirmationPrompt")
    def confirmation_prompt(self) -> "LexIntentConfirmationPromptOutputReference":
        return typing.cast("LexIntentConfirmationPromptOutputReference", jsii.get(self, "confirmationPrompt"))

    @builtins.property
    @jsii.member(jsii_name="createdDate")
    def created_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdDate"))

    @builtins.property
    @jsii.member(jsii_name="dialogCodeHook")
    def dialog_code_hook(self) -> "LexIntentDialogCodeHookOutputReference":
        return typing.cast("LexIntentDialogCodeHookOutputReference", jsii.get(self, "dialogCodeHook"))

    @builtins.property
    @jsii.member(jsii_name="followUpPrompt")
    def follow_up_prompt(self) -> "LexIntentFollowUpPromptOutputReference":
        return typing.cast("LexIntentFollowUpPromptOutputReference", jsii.get(self, "followUpPrompt"))

    @builtins.property
    @jsii.member(jsii_name="fulfillmentActivity")
    def fulfillment_activity(self) -> "LexIntentFulfillmentActivityOutputReference":
        return typing.cast("LexIntentFulfillmentActivityOutputReference", jsii.get(self, "fulfillmentActivity"))

    @builtins.property
    @jsii.member(jsii_name="lastUpdatedDate")
    def last_updated_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lastUpdatedDate"))

    @builtins.property
    @jsii.member(jsii_name="rejectionStatement")
    def rejection_statement(self) -> "LexIntentRejectionStatementOutputReference":
        return typing.cast("LexIntentRejectionStatementOutputReference", jsii.get(self, "rejectionStatement"))

    @builtins.property
    @jsii.member(jsii_name="slot")
    def slot(self) -> "LexIntentSlotList":
        return typing.cast("LexIntentSlotList", jsii.get(self, "slot"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "LexIntentTimeoutsOutputReference":
        return typing.cast("LexIntentTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="conclusionStatementInput")
    def conclusion_statement_input(
        self,
    ) -> typing.Optional["LexIntentConclusionStatement"]:
        return typing.cast(typing.Optional["LexIntentConclusionStatement"], jsii.get(self, "conclusionStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="confirmationPromptInput")
    def confirmation_prompt_input(
        self,
    ) -> typing.Optional["LexIntentConfirmationPrompt"]:
        return typing.cast(typing.Optional["LexIntentConfirmationPrompt"], jsii.get(self, "confirmationPromptInput"))

    @builtins.property
    @jsii.member(jsii_name="createVersionInput")
    def create_version_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "createVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dialogCodeHookInput")
    def dialog_code_hook_input(self) -> typing.Optional["LexIntentDialogCodeHook"]:
        return typing.cast(typing.Optional["LexIntentDialogCodeHook"], jsii.get(self, "dialogCodeHookInput"))

    @builtins.property
    @jsii.member(jsii_name="followUpPromptInput")
    def follow_up_prompt_input(self) -> typing.Optional["LexIntentFollowUpPrompt"]:
        return typing.cast(typing.Optional["LexIntentFollowUpPrompt"], jsii.get(self, "followUpPromptInput"))

    @builtins.property
    @jsii.member(jsii_name="fulfillmentActivityInput")
    def fulfillment_activity_input(
        self,
    ) -> typing.Optional["LexIntentFulfillmentActivity"]:
        return typing.cast(typing.Optional["LexIntentFulfillmentActivity"], jsii.get(self, "fulfillmentActivityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parentIntentSignatureInput")
    def parent_intent_signature_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentIntentSignatureInput"))

    @builtins.property
    @jsii.member(jsii_name="rejectionStatementInput")
    def rejection_statement_input(
        self,
    ) -> typing.Optional["LexIntentRejectionStatement"]:
        return typing.cast(typing.Optional["LexIntentRejectionStatement"], jsii.get(self, "rejectionStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleUtterancesInput")
    def sample_utterances_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sampleUtterancesInput"))

    @builtins.property
    @jsii.member(jsii_name="slotInput")
    def slot_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexIntentSlot"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexIntentSlot"]]], jsii.get(self, "slotInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["LexIntentTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["LexIntentTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="createVersion")
    def create_version(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "createVersion"))

    @create_version.setter
    def create_version(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            def stub(value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createVersion", value)

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
    @jsii.member(jsii_name="parentIntentSignature")
    def parent_intent_signature(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parentIntentSignature"))

    @parent_intent_signature.setter
    def parent_intent_signature(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentIntentSignature", value)

    @builtins.property
    @jsii.member(jsii_name="sampleUtterances")
    def sample_utterances(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sampleUtterances"))

    @sample_utterances.setter
    def sample_utterances(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleUtterances", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentConclusionStatement",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "response_card": "responseCard"},
)
class LexIntentConclusionStatement:
    def __init__(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentConclusionStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            def stub(
                *,
                message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentConclusionStatementMessage, typing.Dict[str, typing.Any]]]],
                response_card: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexIntentConclusionStatementMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexIntentConclusionStatementMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConclusionStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentConclusionStatementMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentConclusionStatementMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            def stub(
                *,
                content: builtins.str,
                content_type: builtins.str,
                group_number: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConclusionStatementMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentConclusionStatementMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentConclusionStatementMessageList",
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
    ) -> "LexIntentConclusionStatementMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentConclusionStatementMessageOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConclusionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConclusionStatementMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConclusionStatementMessage]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConclusionStatementMessage]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentConclusionStatementMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentConclusionStatementMessageOutputReference",
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

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentConclusionStatementMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentConclusionStatementMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentConclusionStatementMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[LexIntentConclusionStatementMessage, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentConclusionStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentConclusionStatementOutputReference",
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

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentConclusionStatementMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentConclusionStatementMessage, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentConclusionStatementMessageList:
        return typing.cast(LexIntentConclusionStatementMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConclusionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConclusionStatementMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentConclusionStatement]:
        return typing.cast(typing.Optional[LexIntentConclusionStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentConclusionStatement],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[LexIntentConclusionStatement]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "fulfillment_activity": "fulfillmentActivity",
        "name": "name",
        "conclusion_statement": "conclusionStatement",
        "confirmation_prompt": "confirmationPrompt",
        "create_version": "createVersion",
        "description": "description",
        "dialog_code_hook": "dialogCodeHook",
        "follow_up_prompt": "followUpPrompt",
        "id": "id",
        "parent_intent_signature": "parentIntentSignature",
        "rejection_statement": "rejectionStatement",
        "sample_utterances": "sampleUtterances",
        "slot": "slot",
        "timeouts": "timeouts",
    },
)
class LexIntentConfig(cdktf.TerraformMetaArguments):
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
        fulfillment_activity: typing.Union["LexIntentFulfillmentActivity", typing.Dict[str, typing.Any]],
        name: builtins.str,
        conclusion_statement: typing.Optional[typing.Union[LexIntentConclusionStatement, typing.Dict[str, typing.Any]]] = None,
        confirmation_prompt: typing.Optional[typing.Union["LexIntentConfirmationPrompt", typing.Dict[str, typing.Any]]] = None,
        create_version: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        dialog_code_hook: typing.Optional[typing.Union["LexIntentDialogCodeHook", typing.Dict[str, typing.Any]]] = None,
        follow_up_prompt: typing.Optional[typing.Union["LexIntentFollowUpPrompt", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        parent_intent_signature: typing.Optional[builtins.str] = None,
        rejection_statement: typing.Optional[typing.Union["LexIntentRejectionStatement", typing.Dict[str, typing.Any]]] = None,
        sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
        slot: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentSlot", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["LexIntentTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param fulfillment_activity: fulfillment_activity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#fulfillment_activity LexIntent#fulfillment_activity}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.
        :param conclusion_statement: conclusion_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#conclusion_statement LexIntent#conclusion_statement}
        :param confirmation_prompt: confirmation_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#confirmation_prompt LexIntent#confirmation_prompt}
        :param create_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create_version LexIntent#create_version}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.
        :param dialog_code_hook: dialog_code_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#dialog_code_hook LexIntent#dialog_code_hook}
        :param follow_up_prompt: follow_up_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#follow_up_prompt LexIntent#follow_up_prompt}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#id LexIntent#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parent_intent_signature: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#parent_intent_signature LexIntent#parent_intent_signature}.
        :param rejection_statement: rejection_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        :param sample_utterances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.
        :param slot: slot block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot LexIntent#slot}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#timeouts LexIntent#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(fulfillment_activity, dict):
            fulfillment_activity = LexIntentFulfillmentActivity(**fulfillment_activity)
        if isinstance(conclusion_statement, dict):
            conclusion_statement = LexIntentConclusionStatement(**conclusion_statement)
        if isinstance(confirmation_prompt, dict):
            confirmation_prompt = LexIntentConfirmationPrompt(**confirmation_prompt)
        if isinstance(dialog_code_hook, dict):
            dialog_code_hook = LexIntentDialogCodeHook(**dialog_code_hook)
        if isinstance(follow_up_prompt, dict):
            follow_up_prompt = LexIntentFollowUpPrompt(**follow_up_prompt)
        if isinstance(rejection_statement, dict):
            rejection_statement = LexIntentRejectionStatement(**rejection_statement)
        if isinstance(timeouts, dict):
            timeouts = LexIntentTimeouts(**timeouts)
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
                fulfillment_activity: typing.Union[LexIntentFulfillmentActivity, typing.Dict[str, typing.Any]],
                name: builtins.str,
                conclusion_statement: typing.Optional[typing.Union[LexIntentConclusionStatement, typing.Dict[str, typing.Any]]] = None,
                confirmation_prompt: typing.Optional[typing.Union[LexIntentConfirmationPrompt, typing.Dict[str, typing.Any]]] = None,
                create_version: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
                description: typing.Optional[builtins.str] = None,
                dialog_code_hook: typing.Optional[typing.Union[LexIntentDialogCodeHook, typing.Dict[str, typing.Any]]] = None,
                follow_up_prompt: typing.Optional[typing.Union[LexIntentFollowUpPrompt, typing.Dict[str, typing.Any]]] = None,
                id: typing.Optional[builtins.str] = None,
                parent_intent_signature: typing.Optional[builtins.str] = None,
                rejection_statement: typing.Optional[typing.Union[LexIntentRejectionStatement, typing.Dict[str, typing.Any]]] = None,
                sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
                slot: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentSlot, typing.Dict[str, typing.Any]]]]] = None,
                timeouts: typing.Optional[typing.Union[LexIntentTimeouts, typing.Dict[str, typing.Any]]] = None,
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
            check_type(argname="argument fulfillment_activity", value=fulfillment_activity, expected_type=type_hints["fulfillment_activity"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument conclusion_statement", value=conclusion_statement, expected_type=type_hints["conclusion_statement"])
            check_type(argname="argument confirmation_prompt", value=confirmation_prompt, expected_type=type_hints["confirmation_prompt"])
            check_type(argname="argument create_version", value=create_version, expected_type=type_hints["create_version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dialog_code_hook", value=dialog_code_hook, expected_type=type_hints["dialog_code_hook"])
            check_type(argname="argument follow_up_prompt", value=follow_up_prompt, expected_type=type_hints["follow_up_prompt"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parent_intent_signature", value=parent_intent_signature, expected_type=type_hints["parent_intent_signature"])
            check_type(argname="argument rejection_statement", value=rejection_statement, expected_type=type_hints["rejection_statement"])
            check_type(argname="argument sample_utterances", value=sample_utterances, expected_type=type_hints["sample_utterances"])
            check_type(argname="argument slot", value=slot, expected_type=type_hints["slot"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "fulfillment_activity": fulfillment_activity,
            "name": name,
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
        if conclusion_statement is not None:
            self._values["conclusion_statement"] = conclusion_statement
        if confirmation_prompt is not None:
            self._values["confirmation_prompt"] = confirmation_prompt
        if create_version is not None:
            self._values["create_version"] = create_version
        if description is not None:
            self._values["description"] = description
        if dialog_code_hook is not None:
            self._values["dialog_code_hook"] = dialog_code_hook
        if follow_up_prompt is not None:
            self._values["follow_up_prompt"] = follow_up_prompt
        if id is not None:
            self._values["id"] = id
        if parent_intent_signature is not None:
            self._values["parent_intent_signature"] = parent_intent_signature
        if rejection_statement is not None:
            self._values["rejection_statement"] = rejection_statement
        if sample_utterances is not None:
            self._values["sample_utterances"] = sample_utterances
        if slot is not None:
            self._values["slot"] = slot
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def fulfillment_activity(self) -> "LexIntentFulfillmentActivity":
        '''fulfillment_activity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#fulfillment_activity LexIntent#fulfillment_activity}
        '''
        result = self._values.get("fulfillment_activity")
        assert result is not None, "Required property 'fulfillment_activity' is missing"
        return typing.cast("LexIntentFulfillmentActivity", result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def conclusion_statement(self) -> typing.Optional[LexIntentConclusionStatement]:
        '''conclusion_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#conclusion_statement LexIntent#conclusion_statement}
        '''
        result = self._values.get("conclusion_statement")
        return typing.cast(typing.Optional[LexIntentConclusionStatement], result)

    @builtins.property
    def confirmation_prompt(self) -> typing.Optional["LexIntentConfirmationPrompt"]:
        '''confirmation_prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#confirmation_prompt LexIntent#confirmation_prompt}
        '''
        result = self._values.get("confirmation_prompt")
        return typing.cast(typing.Optional["LexIntentConfirmationPrompt"], result)

    @builtins.property
    def create_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create_version LexIntent#create_version}.'''
        result = self._values.get("create_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dialog_code_hook(self) -> typing.Optional["LexIntentDialogCodeHook"]:
        '''dialog_code_hook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#dialog_code_hook LexIntent#dialog_code_hook}
        '''
        result = self._values.get("dialog_code_hook")
        return typing.cast(typing.Optional["LexIntentDialogCodeHook"], result)

    @builtins.property
    def follow_up_prompt(self) -> typing.Optional["LexIntentFollowUpPrompt"]:
        '''follow_up_prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#follow_up_prompt LexIntent#follow_up_prompt}
        '''
        result = self._values.get("follow_up_prompt")
        return typing.cast(typing.Optional["LexIntentFollowUpPrompt"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#id LexIntent#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent_intent_signature(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#parent_intent_signature LexIntent#parent_intent_signature}.'''
        result = self._values.get("parent_intent_signature")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rejection_statement(self) -> typing.Optional["LexIntentRejectionStatement"]:
        '''rejection_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        '''
        result = self._values.get("rejection_statement")
        return typing.cast(typing.Optional["LexIntentRejectionStatement"], result)

    @builtins.property
    def sample_utterances(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.'''
        result = self._values.get("sample_utterances")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def slot(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexIntentSlot"]]]:
        '''slot block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot LexIntent#slot}
        '''
        result = self._values.get("slot")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["LexIntentSlot"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["LexIntentTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#timeouts LexIntent#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["LexIntentTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentConfirmationPrompt",
    jsii_struct_bases=[],
    name_mapping={
        "max_attempts": "maxAttempts",
        "message": "message",
        "response_card": "responseCard",
    },
)
class LexIntentConfirmationPrompt:
    def __init__(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentConfirmationPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            def stub(
                *,
                max_attempts: jsii.Number,
                message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentConfirmationPromptMessage, typing.Dict[str, typing.Any]]]],
                response_card: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_attempts", value=max_attempts, expected_type=type_hints["max_attempts"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_attempts": max_attempts,
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def max_attempts(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.'''
        result = self._values.get("max_attempts")
        assert result is not None, "Required property 'max_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexIntentConfirmationPromptMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexIntentConfirmationPromptMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConfirmationPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentConfirmationPromptMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentConfirmationPromptMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            def stub(
                *,
                content: builtins.str,
                content_type: builtins.str,
                group_number: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentConfirmationPromptMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentConfirmationPromptMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentConfirmationPromptMessageList",
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
    ) -> "LexIntentConfirmationPromptMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentConfirmationPromptMessageOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentConfirmationPromptMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentConfirmationPromptMessageOutputReference",
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

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentConfirmationPromptMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentConfirmationPromptMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentConfirmationPromptMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[LexIntentConfirmationPromptMessage, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentConfirmationPromptOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentConfirmationPromptOutputReference",
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

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentConfirmationPromptMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentConfirmationPromptMessage, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentConfirmationPromptMessageList:
        return typing.cast(LexIntentConfirmationPromptMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsInput")
    def max_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentConfirmationPromptMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAttempts")
    def max_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAttempts"))

    @max_attempts.setter
    def max_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentConfirmationPrompt]:
        return typing.cast(typing.Optional[LexIntentConfirmationPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentConfirmationPrompt],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[LexIntentConfirmationPrompt]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentDialogCodeHook",
    jsii_struct_bases=[],
    name_mapping={"message_version": "messageVersion", "uri": "uri"},
)
class LexIntentDialogCodeHook:
    def __init__(self, *, message_version: builtins.str, uri: builtins.str) -> None:
        '''
        :param message_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.
        '''
        if __debug__:
            def stub(*, message_version: builtins.str, uri: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument message_version", value=message_version, expected_type=type_hints["message_version"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "message_version": message_version,
            "uri": uri,
        }

    @builtins.property
    def message_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.'''
        result = self._values.get("message_version")
        assert result is not None, "Required property 'message_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.'''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentDialogCodeHook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentDialogCodeHookOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentDialogCodeHookOutputReference",
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

    @builtins.property
    @jsii.member(jsii_name="messageVersionInput")
    def message_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="messageVersion")
    def message_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageVersion"))

    @message_version.setter
    def message_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageVersion", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentDialogCodeHook]:
        return typing.cast(typing.Optional[LexIntentDialogCodeHook], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LexIntentDialogCodeHook]) -> None:
        if __debug__:
            def stub(value: typing.Optional[LexIntentDialogCodeHook]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFollowUpPrompt",
    jsii_struct_bases=[],
    name_mapping={"prompt": "prompt", "rejection_statement": "rejectionStatement"},
)
class LexIntentFollowUpPrompt:
    def __init__(
        self,
        *,
        prompt: typing.Union["LexIntentFollowUpPromptPrompt", typing.Dict[str, typing.Any]],
        rejection_statement: typing.Union["LexIntentFollowUpPromptRejectionStatement", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param prompt: prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#prompt LexIntent#prompt}
        :param rejection_statement: rejection_statement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        '''
        if isinstance(prompt, dict):
            prompt = LexIntentFollowUpPromptPrompt(**prompt)
        if isinstance(rejection_statement, dict):
            rejection_statement = LexIntentFollowUpPromptRejectionStatement(**rejection_statement)
        if __debug__:
            def stub(
                *,
                prompt: typing.Union[LexIntentFollowUpPromptPrompt, typing.Dict[str, typing.Any]],
                rejection_statement: typing.Union[LexIntentFollowUpPromptRejectionStatement, typing.Dict[str, typing.Any]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument prompt", value=prompt, expected_type=type_hints["prompt"])
            check_type(argname="argument rejection_statement", value=rejection_statement, expected_type=type_hints["rejection_statement"])
        self._values: typing.Dict[str, typing.Any] = {
            "prompt": prompt,
            "rejection_statement": rejection_statement,
        }

    @builtins.property
    def prompt(self) -> "LexIntentFollowUpPromptPrompt":
        '''prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#prompt LexIntent#prompt}
        '''
        result = self._values.get("prompt")
        assert result is not None, "Required property 'prompt' is missing"
        return typing.cast("LexIntentFollowUpPromptPrompt", result)

    @builtins.property
    def rejection_statement(self) -> "LexIntentFollowUpPromptRejectionStatement":
        '''rejection_statement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#rejection_statement LexIntent#rejection_statement}
        '''
        result = self._values.get("rejection_statement")
        assert result is not None, "Required property 'rejection_statement' is missing"
        return typing.cast("LexIntentFollowUpPromptRejectionStatement", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentFollowUpPromptOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFollowUpPromptOutputReference",
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

    @jsii.member(jsii_name="putPrompt")
    def put_prompt(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentFollowUpPromptPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentFollowUpPromptPrompt(
            max_attempts=max_attempts, message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putPrompt", [value]))

    @jsii.member(jsii_name="putRejectionStatement")
    def put_rejection_statement(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentFollowUpPromptRejectionStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentFollowUpPromptRejectionStatement(
            message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putRejectionStatement", [value]))

    @builtins.property
    @jsii.member(jsii_name="prompt")
    def prompt(self) -> "LexIntentFollowUpPromptPromptOutputReference":
        return typing.cast("LexIntentFollowUpPromptPromptOutputReference", jsii.get(self, "prompt"))

    @builtins.property
    @jsii.member(jsii_name="rejectionStatement")
    def rejection_statement(
        self,
    ) -> "LexIntentFollowUpPromptRejectionStatementOutputReference":
        return typing.cast("LexIntentFollowUpPromptRejectionStatementOutputReference", jsii.get(self, "rejectionStatement"))

    @builtins.property
    @jsii.member(jsii_name="promptInput")
    def prompt_input(self) -> typing.Optional["LexIntentFollowUpPromptPrompt"]:
        return typing.cast(typing.Optional["LexIntentFollowUpPromptPrompt"], jsii.get(self, "promptInput"))

    @builtins.property
    @jsii.member(jsii_name="rejectionStatementInput")
    def rejection_statement_input(
        self,
    ) -> typing.Optional["LexIntentFollowUpPromptRejectionStatement"]:
        return typing.cast(typing.Optional["LexIntentFollowUpPromptRejectionStatement"], jsii.get(self, "rejectionStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentFollowUpPrompt]:
        return typing.cast(typing.Optional[LexIntentFollowUpPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[LexIntentFollowUpPrompt]) -> None:
        if __debug__:
            def stub(value: typing.Optional[LexIntentFollowUpPrompt]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFollowUpPromptPrompt",
    jsii_struct_bases=[],
    name_mapping={
        "max_attempts": "maxAttempts",
        "message": "message",
        "response_card": "responseCard",
    },
)
class LexIntentFollowUpPromptPrompt:
    def __init__(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentFollowUpPromptPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            def stub(
                *,
                max_attempts: jsii.Number,
                message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptPromptMessage, typing.Dict[str, typing.Any]]]],
                response_card: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_attempts", value=max_attempts, expected_type=type_hints["max_attempts"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_attempts": max_attempts,
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def max_attempts(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.'''
        result = self._values.get("max_attempts")
        assert result is not None, "Required property 'max_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexIntentFollowUpPromptPromptMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexIntentFollowUpPromptPromptMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPromptPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFollowUpPromptPromptMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentFollowUpPromptPromptMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            def stub(
                *,
                content: builtins.str,
                content_type: builtins.str,
                group_number: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPromptPromptMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentFollowUpPromptPromptMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFollowUpPromptPromptMessageList",
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
    ) -> "LexIntentFollowUpPromptPromptMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentFollowUpPromptPromptMessageOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFollowUpPromptPromptMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFollowUpPromptPromptMessageOutputReference",
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

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentFollowUpPromptPromptMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentFollowUpPromptPromptMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentFollowUpPromptPromptMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[LexIntentFollowUpPromptPromptMessage, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFollowUpPromptPromptOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFollowUpPromptPromptOutputReference",
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

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptPromptMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptPromptMessage, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentFollowUpPromptPromptMessageList:
        return typing.cast(LexIntentFollowUpPromptPromptMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsInput")
    def max_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptPromptMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAttempts")
    def max_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAttempts"))

    @max_attempts.setter
    def max_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentFollowUpPromptPrompt]:
        return typing.cast(typing.Optional[LexIntentFollowUpPromptPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentFollowUpPromptPrompt],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[LexIntentFollowUpPromptPrompt]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFollowUpPromptRejectionStatement",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "response_card": "responseCard"},
)
class LexIntentFollowUpPromptRejectionStatement:
    def __init__(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentFollowUpPromptRejectionStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            def stub(
                *,
                message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, typing.Dict[str, typing.Any]]]],
                response_card: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexIntentFollowUpPromptRejectionStatementMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexIntentFollowUpPromptRejectionStatementMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPromptRejectionStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFollowUpPromptRejectionStatementMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentFollowUpPromptRejectionStatementMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            def stub(
                *,
                content: builtins.str,
                content_type: builtins.str,
                group_number: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFollowUpPromptRejectionStatementMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentFollowUpPromptRejectionStatementMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFollowUpPromptRejectionStatementMessageList",
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
    ) -> "LexIntentFollowUpPromptRejectionStatementMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentFollowUpPromptRejectionStatementMessageOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFollowUpPromptRejectionStatementMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFollowUpPromptRejectionStatementMessageOutputReference",
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

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFollowUpPromptRejectionStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFollowUpPromptRejectionStatementOutputReference",
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

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentFollowUpPromptRejectionStatementMessage, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentFollowUpPromptRejectionStatementMessageList:
        return typing.cast(LexIntentFollowUpPromptRejectionStatementMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentFollowUpPromptRejectionStatementMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[LexIntentFollowUpPromptRejectionStatement]:
        return typing.cast(typing.Optional[LexIntentFollowUpPromptRejectionStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentFollowUpPromptRejectionStatement],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[LexIntentFollowUpPromptRejectionStatement],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFulfillmentActivity",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "code_hook": "codeHook"},
)
class LexIntentFulfillmentActivity:
    def __init__(
        self,
        *,
        type: builtins.str,
        code_hook: typing.Optional[typing.Union["LexIntentFulfillmentActivityCodeHook", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#type LexIntent#type}.
        :param code_hook: code_hook block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#code_hook LexIntent#code_hook}
        '''
        if isinstance(code_hook, dict):
            code_hook = LexIntentFulfillmentActivityCodeHook(**code_hook)
        if __debug__:
            def stub(
                *,
                type: builtins.str,
                code_hook: typing.Optional[typing.Union[LexIntentFulfillmentActivityCodeHook, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument code_hook", value=code_hook, expected_type=type_hints["code_hook"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if code_hook is not None:
            self._values["code_hook"] = code_hook

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#type LexIntent#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def code_hook(self) -> typing.Optional["LexIntentFulfillmentActivityCodeHook"]:
        '''code_hook block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#code_hook LexIntent#code_hook}
        '''
        result = self._values.get("code_hook")
        return typing.cast(typing.Optional["LexIntentFulfillmentActivityCodeHook"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFulfillmentActivity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFulfillmentActivityCodeHook",
    jsii_struct_bases=[],
    name_mapping={"message_version": "messageVersion", "uri": "uri"},
)
class LexIntentFulfillmentActivityCodeHook:
    def __init__(self, *, message_version: builtins.str, uri: builtins.str) -> None:
        '''
        :param message_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.
        '''
        if __debug__:
            def stub(*, message_version: builtins.str, uri: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument message_version", value=message_version, expected_type=type_hints["message_version"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[str, typing.Any] = {
            "message_version": message_version,
            "uri": uri,
        }

    @builtins.property
    def message_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.'''
        result = self._values.get("message_version")
        assert result is not None, "Required property 'message_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.'''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentFulfillmentActivityCodeHook(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentFulfillmentActivityCodeHookOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFulfillmentActivityCodeHookOutputReference",
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

    @builtins.property
    @jsii.member(jsii_name="messageVersionInput")
    def message_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "messageVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="messageVersion")
    def message_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageVersion"))

    @message_version.setter
    def message_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageVersion", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentFulfillmentActivityCodeHook]:
        return typing.cast(typing.Optional[LexIntentFulfillmentActivityCodeHook], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentFulfillmentActivityCodeHook],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[LexIntentFulfillmentActivityCodeHook],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentFulfillmentActivityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentFulfillmentActivityOutputReference",
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

    @jsii.member(jsii_name="putCodeHook")
    def put_code_hook(
        self,
        *,
        message_version: builtins.str,
        uri: builtins.str,
    ) -> None:
        '''
        :param message_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message_version LexIntent#message_version}.
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#uri LexIntent#uri}.
        '''
        value = LexIntentFulfillmentActivityCodeHook(
            message_version=message_version, uri=uri
        )

        return typing.cast(None, jsii.invoke(self, "putCodeHook", [value]))

    @jsii.member(jsii_name="resetCodeHook")
    def reset_code_hook(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeHook", []))

    @builtins.property
    @jsii.member(jsii_name="codeHook")
    def code_hook(self) -> LexIntentFulfillmentActivityCodeHookOutputReference:
        return typing.cast(LexIntentFulfillmentActivityCodeHookOutputReference, jsii.get(self, "codeHook"))

    @builtins.property
    @jsii.member(jsii_name="codeHookInput")
    def code_hook_input(self) -> typing.Optional[LexIntentFulfillmentActivityCodeHook]:
        return typing.cast(typing.Optional[LexIntentFulfillmentActivityCodeHook], jsii.get(self, "codeHookInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

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
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentFulfillmentActivity]:
        return typing.cast(typing.Optional[LexIntentFulfillmentActivity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentFulfillmentActivity],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[LexIntentFulfillmentActivity]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentRejectionStatement",
    jsii_struct_bases=[],
    name_mapping={"message": "message", "response_card": "responseCard"},
)
class LexIntentRejectionStatement:
    def __init__(
        self,
        *,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentRejectionStatementMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            def stub(
                *,
                message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentRejectionStatementMessage, typing.Dict[str, typing.Any]]]],
                response_card: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexIntentRejectionStatementMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexIntentRejectionStatementMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentRejectionStatement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentRejectionStatementMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentRejectionStatementMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            def stub(
                *,
                content: builtins.str,
                content_type: builtins.str,
                group_number: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentRejectionStatementMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentRejectionStatementMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentRejectionStatementMessageList",
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
    ) -> "LexIntentRejectionStatementMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentRejectionStatementMessageOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentRejectionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentRejectionStatementMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentRejectionStatementMessage]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentRejectionStatementMessage]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentRejectionStatementMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentRejectionStatementMessageOutputReference",
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

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentRejectionStatementMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentRejectionStatementMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentRejectionStatementMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[LexIntentRejectionStatementMessage, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentRejectionStatementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentRejectionStatementOutputReference",
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

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentRejectionStatementMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentRejectionStatementMessage, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentRejectionStatementMessageList:
        return typing.cast(LexIntentRejectionStatementMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentRejectionStatementMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentRejectionStatementMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentRejectionStatement]:
        return typing.cast(typing.Optional[LexIntentRejectionStatement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentRejectionStatement],
    ) -> None:
        if __debug__:
            def stub(value: typing.Optional[LexIntentRejectionStatement]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentSlot",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "slot_constraint": "slotConstraint",
        "slot_type": "slotType",
        "description": "description",
        "priority": "priority",
        "response_card": "responseCard",
        "sample_utterances": "sampleUtterances",
        "slot_type_version": "slotTypeVersion",
        "value_elicitation_prompt": "valueElicitationPrompt",
    },
)
class LexIntentSlot:
    def __init__(
        self,
        *,
        name: builtins.str,
        slot_constraint: builtins.str,
        slot_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        response_card: typing.Optional[builtins.str] = None,
        sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
        slot_type_version: typing.Optional[builtins.str] = None,
        value_elicitation_prompt: typing.Optional[typing.Union["LexIntentSlotValueElicitationPrompt", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.
        :param slot_constraint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_constraint LexIntent#slot_constraint}.
        :param slot_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_type LexIntent#slot_type}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#priority LexIntent#priority}.
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        :param sample_utterances: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.
        :param slot_type_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_type_version LexIntent#slot_type_version}.
        :param value_elicitation_prompt: value_elicitation_prompt block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#value_elicitation_prompt LexIntent#value_elicitation_prompt}
        '''
        if isinstance(value_elicitation_prompt, dict):
            value_elicitation_prompt = LexIntentSlotValueElicitationPrompt(**value_elicitation_prompt)
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                slot_constraint: builtins.str,
                slot_type: builtins.str,
                description: typing.Optional[builtins.str] = None,
                priority: typing.Optional[jsii.Number] = None,
                response_card: typing.Optional[builtins.str] = None,
                sample_utterances: typing.Optional[typing.Sequence[builtins.str]] = None,
                slot_type_version: typing.Optional[builtins.str] = None,
                value_elicitation_prompt: typing.Optional[typing.Union[LexIntentSlotValueElicitationPrompt, typing.Dict[str, typing.Any]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument slot_constraint", value=slot_constraint, expected_type=type_hints["slot_constraint"])
            check_type(argname="argument slot_type", value=slot_type, expected_type=type_hints["slot_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
            check_type(argname="argument sample_utterances", value=sample_utterances, expected_type=type_hints["sample_utterances"])
            check_type(argname="argument slot_type_version", value=slot_type_version, expected_type=type_hints["slot_type_version"])
            check_type(argname="argument value_elicitation_prompt", value=value_elicitation_prompt, expected_type=type_hints["value_elicitation_prompt"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "slot_constraint": slot_constraint,
            "slot_type": slot_type,
        }
        if description is not None:
            self._values["description"] = description
        if priority is not None:
            self._values["priority"] = priority
        if response_card is not None:
            self._values["response_card"] = response_card
        if sample_utterances is not None:
            self._values["sample_utterances"] = sample_utterances
        if slot_type_version is not None:
            self._values["slot_type_version"] = slot_type_version
        if value_elicitation_prompt is not None:
            self._values["value_elicitation_prompt"] = value_elicitation_prompt

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#name LexIntent#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slot_constraint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_constraint LexIntent#slot_constraint}.'''
        result = self._values.get("slot_constraint")
        assert result is not None, "Required property 'slot_constraint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def slot_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_type LexIntent#slot_type}.'''
        result = self._values.get("slot_type")
        assert result is not None, "Required property 'slot_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#description LexIntent#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#priority LexIntent#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sample_utterances(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#sample_utterances LexIntent#sample_utterances}.'''
        result = self._values.get("sample_utterances")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def slot_type_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#slot_type_version LexIntent#slot_type_version}.'''
        result = self._values.get("slot_type_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value_elicitation_prompt(
        self,
    ) -> typing.Optional["LexIntentSlotValueElicitationPrompt"]:
        '''value_elicitation_prompt block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#value_elicitation_prompt LexIntent#value_elicitation_prompt}
        '''
        result = self._values.get("value_elicitation_prompt")
        return typing.cast(typing.Optional["LexIntentSlotValueElicitationPrompt"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentSlot(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentSlotList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentSlotList",
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
    def get(self, index: jsii.Number) -> "LexIntentSlotOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentSlotOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlot]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlot]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlot]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlot]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentSlotOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentSlotOutputReference",
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

    @jsii.member(jsii_name="putValueElicitationPrompt")
    def put_value_elicitation_prompt(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentSlotValueElicitationPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        value = LexIntentSlotValueElicitationPrompt(
            max_attempts=max_attempts, message=message, response_card=response_card
        )

        return typing.cast(None, jsii.invoke(self, "putValueElicitationPrompt", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @jsii.member(jsii_name="resetSampleUtterances")
    def reset_sample_utterances(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSampleUtterances", []))

    @jsii.member(jsii_name="resetSlotTypeVersion")
    def reset_slot_type_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlotTypeVersion", []))

    @jsii.member(jsii_name="resetValueElicitationPrompt")
    def reset_value_elicitation_prompt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueElicitationPrompt", []))

    @builtins.property
    @jsii.member(jsii_name="valueElicitationPrompt")
    def value_elicitation_prompt(
        self,
    ) -> "LexIntentSlotValueElicitationPromptOutputReference":
        return typing.cast("LexIntentSlotValueElicitationPromptOutputReference", jsii.get(self, "valueElicitationPrompt"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="sampleUtterancesInput")
    def sample_utterances_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sampleUtterancesInput"))

    @builtins.property
    @jsii.member(jsii_name="slotConstraintInput")
    def slot_constraint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slotConstraintInput"))

    @builtins.property
    @jsii.member(jsii_name="slotTypeInput")
    def slot_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slotTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="slotTypeVersionInput")
    def slot_type_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slotTypeVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="valueElicitationPromptInput")
    def value_elicitation_prompt_input(
        self,
    ) -> typing.Optional["LexIntentSlotValueElicitationPrompt"]:
        return typing.cast(typing.Optional["LexIntentSlotValueElicitationPrompt"], jsii.get(self, "valueElicitationPromptInput"))

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
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="sampleUtterances")
    def sample_utterances(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sampleUtterances"))

    @sample_utterances.setter
    def sample_utterances(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            def stub(value: typing.List[builtins.str]) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sampleUtterances", value)

    @builtins.property
    @jsii.member(jsii_name="slotConstraint")
    def slot_constraint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slotConstraint"))

    @slot_constraint.setter
    def slot_constraint(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slotConstraint", value)

    @builtins.property
    @jsii.member(jsii_name="slotType")
    def slot_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slotType"))

    @slot_type.setter
    def slot_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slotType", value)

    @builtins.property
    @jsii.member(jsii_name="slotTypeVersion")
    def slot_type_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slotTypeVersion"))

    @slot_type_version.setter
    def slot_type_version(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slotTypeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentSlot, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentSlot, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentSlot, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[LexIntentSlot, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentSlotValueElicitationPrompt",
    jsii_struct_bases=[],
    name_mapping={
        "max_attempts": "maxAttempts",
        "message": "message",
        "response_card": "responseCard",
    },
)
class LexIntentSlotValueElicitationPrompt:
    def __init__(
        self,
        *,
        max_attempts: jsii.Number,
        message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["LexIntentSlotValueElicitationPromptMessage", typing.Dict[str, typing.Any]]]],
        response_card: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param max_attempts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.
        :param message: message block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        :param response_card: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.
        '''
        if __debug__:
            def stub(
                *,
                max_attempts: jsii.Number,
                message: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentSlotValueElicitationPromptMessage, typing.Dict[str, typing.Any]]]],
                response_card: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument max_attempts", value=max_attempts, expected_type=type_hints["max_attempts"])
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument response_card", value=response_card, expected_type=type_hints["response_card"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_attempts": max_attempts,
            "message": message,
        }
        if response_card is not None:
            self._values["response_card"] = response_card

    @builtins.property
    def max_attempts(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#max_attempts LexIntent#max_attempts}.'''
        result = self._values.get("max_attempts")
        assert result is not None, "Required property 'max_attempts' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def message(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["LexIntentSlotValueElicitationPromptMessage"]]:
        '''message block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#message LexIntent#message}
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["LexIntentSlotValueElicitationPromptMessage"]], result)

    @builtins.property
    def response_card(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#response_card LexIntent#response_card}.'''
        result = self._values.get("response_card")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentSlotValueElicitationPrompt(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentSlotValueElicitationPromptMessage",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "content_type": "contentType",
        "group_number": "groupNumber",
    },
)
class LexIntentSlotValueElicitationPromptMessage:
    def __init__(
        self,
        *,
        content: builtins.str,
        content_type: builtins.str,
        group_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.
        :param group_number: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.
        '''
        if __debug__:
            def stub(
                *,
                content: builtins.str,
                content_type: builtins.str,
                group_number: typing.Optional[jsii.Number] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument group_number", value=group_number, expected_type=type_hints["group_number"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "content_type": content_type,
        }
        if group_number is not None:
            self._values["group_number"] = group_number

    @builtins.property
    def content(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content LexIntent#content}.'''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#content_type LexIntent#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#group_number LexIntent#group_number}.'''
        result = self._values.get("group_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentSlotValueElicitationPromptMessage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentSlotValueElicitationPromptMessageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentSlotValueElicitationPromptMessageList",
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
    ) -> "LexIntentSlotValueElicitationPromptMessageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            def stub(index: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("LexIntentSlotValueElicitationPromptMessageOutputReference", jsii.invoke(self, "get", [index]))

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
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentSlotValueElicitationPromptMessageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentSlotValueElicitationPromptMessageOutputReference",
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

    @jsii.member(jsii_name="resetGroupNumber")
    def reset_group_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroupNumber", []))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupNumberInput")
    def group_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "groupNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="groupNumber")
    def group_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "groupNumber"))

    @group_number.setter
    def group_number(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "groupNumber", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentSlotValueElicitationPromptMessage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentSlotValueElicitationPromptMessage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentSlotValueElicitationPromptMessage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[LexIntentSlotValueElicitationPromptMessage, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class LexIntentSlotValueElicitationPromptOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentSlotValueElicitationPromptOutputReference",
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

    @jsii.member(jsii_name="putMessage")
    def put_message(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentSlotValueElicitationPromptMessage, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            def stub(
                value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[LexIntentSlotValueElicitationPromptMessage, typing.Dict[str, typing.Any]]]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMessage", [value]))

    @jsii.member(jsii_name="resetResponseCard")
    def reset_response_card(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseCard", []))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> LexIntentSlotValueElicitationPromptMessageList:
        return typing.cast(LexIntentSlotValueElicitationPromptMessageList, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="maxAttemptsInput")
    def max_attempts_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAttemptsInput"))

    @builtins.property
    @jsii.member(jsii_name="messageInput")
    def message_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[LexIntentSlotValueElicitationPromptMessage]]], jsii.get(self, "messageInput"))

    @builtins.property
    @jsii.member(jsii_name="responseCardInput")
    def response_card_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "responseCardInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAttempts")
    def max_attempts(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAttempts"))

    @max_attempts.setter
    def max_attempts(self, value: jsii.Number) -> None:
        if __debug__:
            def stub(value: jsii.Number) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAttempts", value)

    @builtins.property
    @jsii.member(jsii_name="responseCard")
    def response_card(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "responseCard"))

    @response_card.setter
    def response_card(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseCard", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[LexIntentSlotValueElicitationPrompt]:
        return typing.cast(typing.Optional[LexIntentSlotValueElicitationPrompt], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[LexIntentSlotValueElicitationPrompt],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[LexIntentSlotValueElicitationPrompt],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class LexIntentTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create LexIntent#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#delete LexIntent#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#update LexIntent#update}.
        '''
        if __debug__:
            def stub(
                *,
                create: typing.Optional[builtins.str] = None,
                delete: typing.Optional[builtins.str] = None,
                update: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#create LexIntent#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#delete LexIntent#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/aws/r/lex_intent#update LexIntent#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LexIntentTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LexIntentTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-aws.lexIntent.LexIntentTimeoutsOutputReference",
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

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            def stub(value: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[LexIntentTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[LexIntentTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[LexIntentTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            def stub(
                value: typing.Optional[typing.Union[LexIntentTimeouts, cdktf.IResolvable]],
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "LexIntent",
    "LexIntentConclusionStatement",
    "LexIntentConclusionStatementMessage",
    "LexIntentConclusionStatementMessageList",
    "LexIntentConclusionStatementMessageOutputReference",
    "LexIntentConclusionStatementOutputReference",
    "LexIntentConfig",
    "LexIntentConfirmationPrompt",
    "LexIntentConfirmationPromptMessage",
    "LexIntentConfirmationPromptMessageList",
    "LexIntentConfirmationPromptMessageOutputReference",
    "LexIntentConfirmationPromptOutputReference",
    "LexIntentDialogCodeHook",
    "LexIntentDialogCodeHookOutputReference",
    "LexIntentFollowUpPrompt",
    "LexIntentFollowUpPromptOutputReference",
    "LexIntentFollowUpPromptPrompt",
    "LexIntentFollowUpPromptPromptMessage",
    "LexIntentFollowUpPromptPromptMessageList",
    "LexIntentFollowUpPromptPromptMessageOutputReference",
    "LexIntentFollowUpPromptPromptOutputReference",
    "LexIntentFollowUpPromptRejectionStatement",
    "LexIntentFollowUpPromptRejectionStatementMessage",
    "LexIntentFollowUpPromptRejectionStatementMessageList",
    "LexIntentFollowUpPromptRejectionStatementMessageOutputReference",
    "LexIntentFollowUpPromptRejectionStatementOutputReference",
    "LexIntentFulfillmentActivity",
    "LexIntentFulfillmentActivityCodeHook",
    "LexIntentFulfillmentActivityCodeHookOutputReference",
    "LexIntentFulfillmentActivityOutputReference",
    "LexIntentRejectionStatement",
    "LexIntentRejectionStatementMessage",
    "LexIntentRejectionStatementMessageList",
    "LexIntentRejectionStatementMessageOutputReference",
    "LexIntentRejectionStatementOutputReference",
    "LexIntentSlot",
    "LexIntentSlotList",
    "LexIntentSlotOutputReference",
    "LexIntentSlotValueElicitationPrompt",
    "LexIntentSlotValueElicitationPromptMessage",
    "LexIntentSlotValueElicitationPromptMessageList",
    "LexIntentSlotValueElicitationPromptMessageOutputReference",
    "LexIntentSlotValueElicitationPromptOutputReference",
    "LexIntentTimeouts",
    "LexIntentTimeoutsOutputReference",
]

publication.publish()
