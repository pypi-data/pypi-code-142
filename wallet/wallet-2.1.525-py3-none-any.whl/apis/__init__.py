
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.advertisement_credits_api import AdvertisementCreditsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from wallet.api.advertisement_credits_api import AdvertisementCreditsApi
from wallet.api.analytics_api import AnalyticsApi
from wallet.api.apple_wallet_subscribers_api import AppleWalletSubscribersApi
from wallet.api.billing_api import BillingApi
from wallet.api.club_members__points_api import ClubMembersPointsApi
from wallet.api.configuration_api import ConfigurationApi
from wallet.api.countries_api import CountriesApi
from wallet.api.customer_api import CustomerApi
from wallet.api.dashboard_api import DashboardApi
from wallet.api.dynamic_vouchers_api import DynamicVouchersApi
from wallet.api.employee_api_keys_api import EmployeeAPIKeysApi
from wallet.api.employee_access_api import EmployeeAccessApi
from wallet.api.employees_api import EmployeesApi
from wallet.api.image_grid_api import ImageGridApi
from wallet.api.industries_api import IndustriesApi
from wallet.api.info_genesis_reports_api import InfoGenesisReportsApi
from wallet.api.integrated_terminals_api import IntegratedTerminalsApi
from wallet.api.interactions_api import InteractionsApi
from wallet.api.link_book_api import LinkBookApi
from wallet.api.link_book_section_api import LinkBookSectionApi
from wallet.api.login_and_logout_api import LoginAndLogoutApi
from wallet.api.membership_tiers_api import MembershipTiersApi
from wallet.api.merchant_api import MerchantApi
from wallet.api.merchant_credits_api import MerchantCreditsApi
from wallet.api.merchant_urls_api import MerchantURLsApi
from wallet.api.mobile_terminal_api import MobileTerminalApi
from wallet.api.news_api import NewsApi
from wallet.api.payment_designs_api import PaymentDesignsApi
from wallet.api.performances_api import PerformancesApi
from wallet.api.promo_codes_api import PromoCodesApi
from wallet.api.sms_api import SMSApi
from wallet.api.settings_api import SettingsApi
from wallet.api.shopify_terminal_api import ShopifyTerminalApi
from wallet.api.static_voucher_campaign_groups_api import StaticVoucherCampaignGroupsApi
from wallet.api.static_voucher_campaigns_api import StaticVoucherCampaignsApi
from wallet.api.static_vouchers_api import StaticVouchersApi
from wallet.api.system_api import SystemApi
from wallet.api.transaction_ledger_api import TransactionLedgerApi
from wallet.api.utilities_api import UtilitiesApi
from wallet.api.web_terminal_api import WebTerminalApi
from wallet.api.wix_terminal_api import WixTerminalApi
from wallet.api.woo_commerce_terminal_api import WooCommerceTerminalApi
