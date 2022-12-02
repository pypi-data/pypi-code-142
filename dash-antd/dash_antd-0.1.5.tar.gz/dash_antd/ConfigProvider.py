# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ConfigProvider(Component):
    """A ConfigProvider component.
Set components spacing.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; optional):
    Unique ID to identify this component in Dash callbacks.

- active_tokens (dict; optional):
    (ReadOnly) fully resolved global design tokens.

    `active_tokens` is a dict with keys:

    - blue (string; optional)

    - blue-1 (string; optional)

    - blue-10 (string; optional)

    - blue-2 (string; optional)

    - blue-3 (string; optional)

    - blue-4 (string; optional)

    - blue-5 (string; optional)

    - blue-6 (string; optional)

    - blue-7 (string; optional)

    - blue-8 (string; optional)

    - blue-9 (string; optional)

    - borderRadius (number; optional)

    - borderRadiusLG (number; optional)

    - borderRadiusOuter (number; optional)

    - borderRadiusSM (number; optional)

    - borderRadiusXS (number; optional)

    - boxShadow (string; optional)

    - boxShadowSecondary (string; optional)

    - colorBgBase (string; optional):
        Base component background color. Will derivative container
        background color with this @,desc,基础背景色.

    - colorBgContainer (string; optional)

    - colorBgContainerDisabled (string; optional)

    - colorBgElevated (string; optional)

    - colorBgLayout (string; optional)

    - colorBgMask (string; optional)

    - colorBgSpotlight (string; optional)

    - colorBgTextActive (string; optional)

    - colorBgTextHover (string; optional)

    - colorBorder (string; optional)

    - colorBorderBg (string; optional)

    - colorBorderSecondary (string; optional)

    - colorError (string; optional)

    - colorErrorActive (string; optional)

    - colorErrorBg (string; optional)

    - colorErrorBgHover (string; optional)

    - colorErrorBorder (string; optional)

    - colorErrorBorderHover (string; optional)

    - colorErrorHover (string; optional)

    - colorErrorOutline (string; optional)

    - colorErrorText (string; optional)

    - colorErrorTextActive (string; optional)

    - colorErrorTextHover (string; optional)

    - colorFill (string; optional)

    - colorFillAlter (string; optional)

    - colorFillContent (string; optional)

    - colorFillContentHover (string; optional)

    - colorFillQuaternary (string; optional)

    - colorFillSecondary (string; optional)

    - colorFillTertiary (string; optional)

    - colorHighlight (string; optional)

    - colorIcon (string; optional):
        Weak action. Such as `allowClear` or Alert close button.

    - colorIconHover (string; optional):
        Weak action hover color. Such as `allowClear` or Alert close
        button.

    - colorInfo (string; optional)

    - colorInfoActive (string; optional)

    - colorInfoBg (string; optional)

    - colorInfoBgHover (string; optional)

    - colorInfoBorder (string; optional)

    - colorInfoBorderHover (string; optional)

    - colorInfoHover (string; optional)

    - colorInfoText (string; optional)

    - colorInfoTextActive (string; optional)

    - colorInfoTextHover (string; optional)

    - colorLink (string; optional)

    - colorLinkActive (string; optional)

    - colorLinkHover (string; optional)

    - colorPrimary (string; optional)

    - colorPrimaryActive (string; optional)

    - colorPrimaryBg (string; optional)

    - colorPrimaryBgHover (string; optional)

    - colorPrimaryBorder (string; optional)

    - colorPrimaryBorderHover (string; optional)

    - colorPrimaryHover (string; optional)

    - colorPrimaryText (string; optional)

    - colorPrimaryTextActive (string; optional)

    - colorPrimaryTextHover (string; optional)

    - colorSplit (string; optional)

    - colorSuccess (string; optional)

    - colorSuccessActive (string; optional)

    - colorSuccessBg (string; optional)

    - colorSuccessBgHover (string; optional)

    - colorSuccessBorder (string; optional)

    - colorSuccessBorderHover (string; optional)

    - colorSuccessHover (string; optional)

    - colorSuccessText (string; optional)

    - colorSuccessTextActive (string; optional)

    - colorSuccessTextHover (string; optional)

    - colorText (string; optional)

    - colorTextBase (string; optional)

    - colorTextDescription (string; optional)

    - colorTextDisabled (string; optional)

    - colorTextHeading (string; optional)

    - colorTextLabel (string; optional)

    - colorTextLightSolid (string; optional)

    - colorTextPlaceholder (string; optional)

    - colorTextQuaternary (string; optional)

    - colorTextSecondary (string; optional)

    - colorTextTertiary (string; optional)

    - colorWarning (string; optional)

    - colorWarningActive (string; optional)

    - colorWarningBg (string; optional)

    - colorWarningBgHover (string; optional)

    - colorWarningBorder (string; optional)

    - colorWarningBorderHover (string; optional)

    - colorWarningHover (string; optional)

    - colorWarningOutline (string; optional)

    - colorWarningText (string; optional)

    - colorWarningTextActive (string; optional)

    - colorWarningTextHover (string; optional)

    - colorWhite (string; optional)

    - controlHeight (number; optional)

    - controlHeightLG (number; optional)

    - controlHeightSM (number; optional)

    - controlHeightXS (number; optional)

    - controlInteractiveSize (number; optional)

    - controlItemBgActive (string; optional)

    - controlItemBgActiveDisabled (string; optional)

    - controlItemBgActiveHover (string; optional)

    - controlItemBgHover (string; optional)

    - controlOutline (string; optional)

    - controlOutlineWidth (number; optional)

    - controlPaddingHorizontal (number; optional)

    - controlPaddingHorizontalSM (number; optional)

    - controlTmpOutline (string; optional):
        Used for DefaultButton, Switch which has default outline.

    - cyan (string; optional)

    - cyan-1 (string; optional)

    - cyan-10 (string; optional)

    - cyan-2 (string; optional)

    - cyan-3 (string; optional)

    - cyan-4 (string; optional)

    - cyan-5 (string; optional)

    - cyan-6 (string; optional)

    - cyan-7 (string; optional)

    - cyan-8 (string; optional)

    - cyan-9 (string; optional)

    - fontFamily (string; optional)

    - fontSize (number; optional)

    - fontSizeHeading1 (number; optional)

    - fontSizeHeading2 (number; optional)

    - fontSizeHeading3 (number; optional)

    - fontSizeHeading4 (number; optional)

    - fontSizeHeading5 (number; optional)

    - fontSizeIcon (number; optional):
        Operation icon in Select, Cascader, etc. icon fontSize. Normal
        is same as fontSizeSM.

    - fontSizeLG (number; optional)

    - fontSizeSM (number; optional)

    - fontSizeXL (number; optional)

    - fontWeightStrong (number; optional):
        For heading like h1, h2, h3 or option selected item.

    - geekblue (string; optional)

    - geekblue-1 (string; optional)

    - geekblue-10 (string; optional)

    - geekblue-2 (string; optional)

    - geekblue-3 (string; optional)

    - geekblue-4 (string; optional)

    - geekblue-5 (string; optional)

    - geekblue-6 (string; optional)

    - geekblue-7 (string; optional)

    - geekblue-8 (string; optional)

    - geekblue-9 (string; optional)

    - gold (string; optional)

    - gold-1 (string; optional)

    - gold-10 (string; optional)

    - gold-2 (string; optional)

    - gold-3 (string; optional)

    - gold-4 (string; optional)

    - gold-5 (string; optional)

    - gold-6 (string; optional)

    - gold-7 (string; optional)

    - gold-8 (string; optional)

    - gold-9 (string; optional)

    - green (string; optional)

    - green-1 (string; optional)

    - green-10 (string; optional)

    - green-2 (string; optional)

    - green-3 (string; optional)

    - green-4 (string; optional)

    - green-5 (string; optional)

    - green-6 (string; optional)

    - green-7 (string; optional)

    - green-8 (string; optional)

    - green-9 (string; optional)

    - lime (string; optional)

    - lime-1 (string; optional)

    - lime-10 (string; optional)

    - lime-2 (string; optional)

    - lime-3 (string; optional)

    - lime-4 (string; optional)

    - lime-5 (string; optional)

    - lime-6 (string; optional)

    - lime-7 (string; optional)

    - lime-8 (string; optional)

    - lime-9 (string; optional)

    - lineHeight (number; optional)

    - lineHeightHeading1 (number; optional)

    - lineHeightHeading2 (number; optional)

    - lineHeightHeading3 (number; optional)

    - lineHeightHeading4 (number; optional)

    - lineHeightHeading5 (number; optional)

    - lineHeightLG (number; optional)

    - lineHeightSM (number; optional)

    - lineType (string; optional)

    - lineWidth (number; optional):
        Border width of base components @,desc,基础线宽.

    - lineWidthBold (number; optional)

    - linkDecoration (string | number; optional)

    - linkFocusDecoration (string | number; optional)

    - linkHoverDecoration (string | number; optional)

    - magenta (string; optional)

    - magenta-1 (string; optional)

    - magenta-10 (string; optional)

    - magenta-2 (string; optional)

    - magenta-3 (string; optional)

    - magenta-4 (string; optional)

    - magenta-5 (string; optional)

    - magenta-6 (string; optional)

    - magenta-7 (string; optional)

    - magenta-8 (string; optional)

    - magenta-9 (string; optional)

    - margin (number; optional)

    - marginLG (number; optional)

    - marginMD (number; optional)

    - marginSM (number; optional)

    - marginXL (number; optional)

    - marginXS (number; optional)

    - marginXXL (number; optional)

    - marginXXS (number; optional)

    - motionBase (number; optional)

    - motionDurationFast (string; optional)

    - motionDurationMid (string; optional)

    - motionDurationSlow (string; optional)

    - motionEaseInBack (string; optional)

    - motionEaseInOut (string; optional)

    - motionEaseInOutCirc (string; optional)

    - motionEaseInQuint (string; optional)

    - motionEaseOut (string; optional)

    - motionEaseOutBack (string; optional)

    - motionEaseOutCirc (string; optional)

    - motionEaseOutQuint (string; optional)

    - motionUnit (number; optional)

    - opacityImage (number; optional)

    - opacityLoading (number; optional)

    - orange (string; optional)

    - orange-1 (string; optional)

    - orange-10 (string; optional)

    - orange-2 (string; optional)

    - orange-3 (string; optional)

    - orange-4 (string; optional)

    - orange-5 (string; optional)

    - orange-6 (string; optional)

    - orange-7 (string; optional)

    - orange-8 (string; optional)

    - orange-9 (string; optional)

    - padding (number; optional)

    - paddingContentHorizontal (number; optional)

    - paddingContentHorizontalLG (number; optional)

    - paddingContentHorizontalSM (number; optional)

    - paddingContentVertical (number; optional)

    - paddingContentVerticalLG (number; optional)

    - paddingContentVerticalSM (number; optional)

    - paddingLG (number; optional)

    - paddingMD (number; optional)

    - paddingSM (number; optional)

    - paddingXL (number; optional)

    - paddingXS (number; optional)

    - paddingXXS (number; optional)

    - pink (string; optional)

    - pink-1 (string; optional)

    - pink-10 (string; optional)

    - pink-2 (string; optional)

    - pink-3 (string; optional)

    - pink-4 (string; optional)

    - pink-5 (string; optional)

    - pink-6 (string; optional)

    - pink-7 (string; optional)

    - pink-8 (string; optional)

    - pink-9 (string; optional)

    - purple (string; optional)

    - purple-1 (string; optional)

    - purple-10 (string; optional)

    - purple-2 (string; optional)

    - purple-3 (string; optional)

    - purple-4 (string; optional)

    - purple-5 (string; optional)

    - purple-6 (string; optional)

    - purple-7 (string; optional)

    - purple-8 (string; optional)

    - purple-9 (string; optional)

    - red (string; optional)

    - red-1 (string; optional)

    - red-10 (string; optional)

    - red-2 (string; optional)

    - red-3 (string; optional)

    - red-4 (string; optional)

    - red-5 (string; optional)

    - red-6 (string; optional)

    - red-7 (string; optional)

    - red-8 (string; optional)

    - red-9 (string; optional)

    - screenLG (number; optional)

    - screenLGMax (number; optional)

    - screenLGMin (number; optional)

    - screenMD (number; optional)

    - screenMDMax (number; optional)

    - screenMDMin (number; optional)

    - screenSM (number; optional)

    - screenSMMax (number; optional)

    - screenSMMin (number; optional)

    - screenXL (number; optional)

    - screenXLMax (number; optional)

    - screenXLMin (number; optional)

    - screenXS (number; optional)

    - screenXSMax (number; optional)

    - screenXSMin (number; optional)

    - screenXXL (number; optional)

    - screenXXLMax (number; optional)

    - screenXXLMin (number; optional)

    - size (number; optional)

    - sizeLG (number; optional)

    - sizeMD (number; optional)

    - sizeMS (number; optional):
        Same as size by default, but could be larger in compact mode.

    - sizePopupArrow (number; optional)

    - sizeSM (number; optional)

    - sizeStep (number; optional)

    - sizeUnit (number; optional)

    - sizeXL (number; optional)

    - sizeXS (number; optional)

    - sizeXXL (number; optional)

    - sizeXXS (number; optional)

    - volcano (string; optional)

    - volcano-1 (string; optional)

    - volcano-10 (string; optional)

    - volcano-2 (string; optional)

    - volcano-3 (string; optional)

    - volcano-4 (string; optional)

    - volcano-5 (string; optional)

    - volcano-6 (string; optional)

    - volcano-7 (string; optional)

    - volcano-8 (string; optional)

    - volcano-9 (string; optional)

    - wireframe (boolean; optional)

    - yellow (string; optional)

    - yellow-1 (string; optional)

    - yellow-10 (string; optional)

    - yellow-2 (string; optional)

    - yellow-3 (string; optional)

    - yellow-4 (string; optional)

    - yellow-5 (string; optional)

    - yellow-6 (string; optional)

    - yellow-7 (string; optional)

    - yellow-8 (string; optional)

    - yellow-9 (string; optional)

    - zIndexBase (number; optional)

    - zIndexPopupBase (number; optional)

- components (dict; optional):
    Set component specific design tokens.

    `components` is a dict with keys:


- input (dict; optional):
    Set common properties for Input component.

    `input` is a dict with keys:

    - autoComplete (string; optional)

- key (string; optional):
    A unique identifier for the component, used to improve performance
    by React.js while rendering components See
    https://reactjs.org/docs/lists-and-keys.html for more info.

- space (dict; optional):
    Set sizing in Space component.

    `space` is a dict with keys:

    - size (number; optional)

- token (dict; optional):
    Set global design tokens.

    `token` is a dict with keys:


- use_compact (boolean; optional):
    Create a dark theming for all child components.

- use_dark_theme (boolean; optional):
    Create a dark theming for all child components."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_antd'
    _type = 'ConfigProvider'
    @_explicitize_args
    def __init__(self, children=None, input=Component.UNDEFINED, space=Component.UNDEFINED, components=Component.UNDEFINED, token=Component.UNDEFINED, use_dark_theme=Component.UNDEFINED, use_compact=Component.UNDEFINED, active_tokens=Component.UNDEFINED, id=Component.UNDEFINED, key=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'active_tokens', 'components', 'input', 'key', 'space', 'token', 'use_compact', 'use_dark_theme']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'active_tokens', 'components', 'input', 'key', 'space', 'token', 'use_compact', 'use_dark_theme']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(ConfigProvider, self).__init__(children=children, **args)
