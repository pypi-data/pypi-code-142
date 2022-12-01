from datetime import datetime
from typing import Dict, List, Optional
from uuid import UUID
from pydantic import validator

from serenity_types.pricing.derivatives.options.volsurface import (
    InterpolatedVolatilitySurface, VolModel, DiscountingMethod
)
from serenity_types.pricing.derivatives.rates.yield_curve import InterpolatedYieldCurve
from serenity_types.refdata.options import OptionStyle, OptionType
from serenity_types.utils.serialization import CamelModel


class OptionValuation(CamelModel):
    """
    A collection of option economics and market data overrides used to describe a single option valuation
    requested from the service. This is intentionally meant to support both listed contract pricing and
    more general pricing of option economics. For market data, everything is defaulted, but the client can
    override or bump (shift) any of the inputs to get the exact pricing scenario desired.
    """

    option_valuation_id: str
    """
    Correlation ID to use for this requested option valuation. If pricing based on a listed contract
    with optionAssetId, by convention the unique ID or symbol of that option should be used.
    """

    qty: Optional[int]
    """
    Number of option contracts; used when computing the spot notional of the option position. Optional;
    if not provided the various position value calculations will be skipped.
    """

    option_asset_id: Optional[UUID]
    """
    Look up all option economics based on the unique ID of a specific listed option contract.
    """

    underlier_asset_id: Optional[UUID]
    """
    Serenity asset identifier of the underlier (currently only BTC, ETH or SOL). Not required if optionAssetId provided.
    """

    strike: Optional[float]
    """
    Absolute value of the strike. Not required if optionAssetId provided. In future we may wish to support different
    StrikeType representations here, but some cases (like DELTA) are potentially trickier, so not for initial version.
    """

    expiry: Optional[datetime]
    """
    Expiration expressed in absolute terms as a date/time. Not required if optionAssetId provided
    """

    option_type: Optional[OptionType]
    """
    Whether we are pricing a PUT or CALL option.
    """

    option_style: Optional[OptionStyle]
    """
    The variety of option being priced.
    """

    contract_size: Optional[float]
    """
    For scaling purposes, the # of underlying per contract. Optional;
    if not provided the various position value calculations will be skipped.
    """

    implied_vol_override: Optional[float]
    """
    Substitute a fixed IV when pricing this option, and ignore the volatility surface.
    """

    implied_vol_bump: Optional[float]
    """
    Include an additive bump on the IV extracted from the surface when pricing this option.
    """

    rate_overrides: Optional[Dict[UUID, float]]
    """
    In the case of DiscountingMethod.CURVE, override the interest rate assumptions used for BTC, USD, etc..
    """

    rate_bumps: Optional[Dict[UUID, float]]
    """
    In the case of DiscountingMethod.CURVE, include an additive bump for BTC, USD, etc. interest rates.
    """

    spot_price_override: Optional[float]
    """
    In the case of DiscountingMethod.CURVE, override the spot price used to compute the forward.
    """

    spot_price_bump: Optional[float]
    """
    In the case of DiscountingMethod.CURVE, bump the spot price used to compute the forward.
    """

    forward_price_override: Optional[float]
    """
    In the case of DiscountingMethod.FUTURES, directly override the input price for the forward.
    """

    forward_price_bump: Optional[float]
    """
    In the case of DiscountingMethod.FUTURES, bump the input price for the forward.
    """


class OptionValuationRequest(CamelModel):
    """
    A batch request to run one or more option valuations using a single model configuration and base
    set of curves and the vol surface. Reasonable defaults will be provided for any missing inputs, e.g.
    if you price a set of Deribit BTC options, the latest BTC volatility surface will be used along with
    the latest discounting curves for BTC and USD. Note that because the request only references a single
    volatility surface this means all included options must have the same underlier as the one in
    VolatilitySurfaceVersion.interpolated.definition.underlier_asset_id.
    """

    as_of_time: Optional[datetime]
    """
    The as-of time to use for loading all marketdata, surfaces, yield curves and refdata from the database.
    Defaulted to the latest up to this time.
    """

    model_config_id: Optional[UUID]
    """
    The specific derivatives analytics model configuration to load; this is used to drive defaults.
    """

    base_currency_id: Optional[UUID]
    """
    Base currency to use for expressing all notional values.
    """

    discounting_method: Optional[DiscountingMethod]
    """
    How to derive the forward price for the options: from curves or futures, or disregard the forward.
    """

    vol_surface_id: Optional[UUID]
    """
    The optional unique ID of the surface to load, latest version as-of the as_of_time.
    """

    vol_surface: Optional[InterpolatedVolatilitySurface]
    """
    The optional client-provided volatility surface to use. If the client provides neither a VS ID
    nor their own volatility surface, the system will load the default for the underlying as-of the as_of_time.
    """

    yield_curve_ids: Optional[Dict[UUID, UUID]]
    """
    The optional unique ID of the yield curves to load per asset, latest version as-of the as_of_time.
    """

    yield_curves: Optional[Dict[UUID, InterpolatedYieldCurve]]
    """
    The optional client-provided yield curves to use per asset. If the client provides neither a YC ID
    nor their own yield curve for any given asset, the system will load the default as-of the as_of_time.
    """

    vol_model: Optional[VolModel]
    """
    The volatility model used for evaluation purposes
    """

    options: List[OptionValuation]
    """
    The full set of option valuations to run with the given market data inputs. The client may provide
    individual overrides or bumps for all inputs as part of each valuation object.
    """

    @validator('yield_curves', always=True)
    def check_yield_curve_ids_or_yield_curves(cls, yield_curves, values):
        if values.get('yield_curve_ids') and yield_curves:
            raise ValueError("Please specify only one of 'yield_curve_ids' or 'yield_curves'")
        return yield_curves

    @validator('vol_surface', always=True)
    def check_vol_surface_id_or_vol_surface(cls, vol_surface, values):
        if values.get('vol_surface_id') and vol_surface:
            raise ValueError("Please specify only one of 'vol_surface_id' or 'vol_surface'")
        return vol_surface


class OptionValuationResult(CamelModel):
    """
    The result of a series of option valuations based on the parameters in the OptionValuationRequest.
    Note that the basic calculation is just Black-Scholes, but if you provide additional information
    regarding the position scaling it will also provide position notional and greek exposures
    in base currency to allow bucketing of greeks and NAV calculations.
    """

    option_valuation_id: str
    """
    Correlation ID for the original OptionValuation.
    """

    vol_model: VolModel
    """
    The specific volatility model used; as SVI calibrations yield different greeks, this needs to be explicit.
    """

    pv: float
    """
    Present value (PV) a.k.a. theoretical price or theo.
    """

    iv: float
    """
    Implied volatility (IV)
    """

    spot_notional: Optional[float]
    """
    The base currency notional of the position: number of contracts (qty) X  spot_price X contract_size.
    """

    spot_price: float
    """
    Input spot price for this valuation.
    """

    forward_price: float
    """
    Input forward price for this valuation.
    """

    rates: Dict[UUID, float]
    """
    Input interest rates, by asset ID.
    """

    delta: float
    """
    Greek output: delta, the option's sensitivity to spot changes.
    """

    delta_qty: Optional[float]
    """
    Delta X qty X contract_size, the delta exposure expressed in qty of underlying.
    """

    delta_ccy: Optional[float]
    """
    Delta X value, a.k.a. the partial derivative of position value with respect to spot,
    expressed in base currency
    """

    gamma: float
    """
    Greek output: gamma, the delta's sensitivity to spot changes.
    """

    gamma_ccy: Optional[float]
    """
    Gamma X value^2, a.k.a. the second derivative of position value with respect to spot,
    expressed in base currency.
    """

    vega: float
    """
    Greek output: vega, the option's sensitivity to volatility changes.
    """

    vega_ccy: Optional[float]
    """
    Partial derivative of the position value of the contract with respect to vega X 1%, expressed in base currency.
    """

    rho: float
    """
    Greek output: rho, the delta's sensitivity to interest rate changes.
    """

    rho_ccy: Optional[float]
    """
    Partial derivative of the spot notional value of the contract with respect to rho X 1bp, expressed in base currency.
    """

    theta: float
    """
    Greek output: theta, the delta's sensitivity to time decay.
    """

    theta_ccy: Optional[float]
    """
    Partial derivative of the spot notional value of the contract with respect to theta X 1 day,
    expressed in base currency.
    """
