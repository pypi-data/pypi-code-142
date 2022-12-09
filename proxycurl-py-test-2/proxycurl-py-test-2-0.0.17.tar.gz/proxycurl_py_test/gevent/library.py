from proxycurl.config import (
    BASE_URL, PROXYCURL_API_KEY, TIMEOUT, MAX_RETRIES, MAX_BACKOFF_SECONDS
)
from proxycurl.gevent.base import ProxycurlBase
from proxycurl.models import (
    PersonEndpointResponse,
    UrlResult,
    ExtractionEmailResult,
    PDLPhoneNumberResult,
    PDLEmailResult,
    LinkedinCompany,
    JobListPage,
    EmployeeCount,
    EmployeeList,
    RoleSearchResult,
    CompanyReveal,
    LinkedinSchool,
    LinkedinJob,
    CreditBalance,
)


class _LinkedinPerson:
    def __init__(self, linkedin):
        self.linkedin = linkedin

    def get(
        self,
        url: str,
        use_cache: str = 'if-recent',
        skills: str = 'exclude',
        inferred_salary: str = 'exclude',
        extra: str = 'exclude',
    ) -> PersonEndpointResponse:
        """Person Profile Endpoint
        
                
        Get structured data of a Personal Profile

        
        :param url: URL of the LinkedIn Profile to crawl.

            URL should be in the format of `https://www.linkedin.com/in/<public-identifier>`
        :type url: str
        :param use_cache: `if-present` Fetches profile from cache regardless of age of profile. If profile is not available in cache, API will attempt to source profile externally.

            `if-recent` The default behavior. API will make a best effort to return a fresh profile no older than 29 days., defaults to 'if-recent'
        :type use_cache: str
        :param skills: Include skills data from external sources.

            This parameter accepts the following values:
            - `exclude` (default value) - Does not provide skills data field.
            - `include` - Append skills data to the person profile object. Costs an extra `1` credit on top of the cost of the base endpoint (if data is available)., defaults to 'exclude'
        :type skills: str
        :param inferred_salary: Include inferred salary range from external sources.

            This parameter accepts the following values:
            - `exclude` (default value) - Does not provide inferred salary data field.
            - `include` - Append inferred salary range data to the person profile object. Costs an extra `1` credit on top of the cost of the base endpoint (if data is available)., defaults to 'exclude'
        :type inferred_salary: str
        :param extra: Enriches the Person Profile with extra details from external sources. Extra details include IDs of social media accounts such as Github and Facebook, gender, birth date, industry and interests.

            This parameter accepts the following values:
            - `exclude` (default value) - Does not provide extra data field.
            - `include` - Append extra data to the person profile object. Costs an extra `1` credit on top of the cost of the base endpoint (if data is available)., defaults to 'exclude'
        :type extra: str
        :return: An object of :class:`proxycurl.models.PersonEndpointResponse` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.PersonEndpointResponse`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/v2/linkedin',
            params={
                'url': url,
                'use_cache': use_cache,
                'skills': skills,
                'inferred_salary': inferred_salary,
                'extra': extra,
            },
            data={
            },
            result_class=PersonEndpointResponse
        )

    def resolve(
        self,
        first_name: str,
        company_domain: str,
        location: str = '',
        title: str = '',
        last_name: str = '',
    ) -> UrlResult:
        """Person Lookup Endpoint
        
        Resolve LinkedIn Profile
        
        :param first_name: First name of the user
        :type first_name: str
        :param company_domain: Company name or domain
        :type company_domain: str
        :param location: The location of this user.

            Name of country, city or state.
        :type location: str
        :param title: Title that user is holding at his/her current job
        :type title: str
        :param last_name: Last name of the user
        :type last_name: str
        :return: An object of :class:`proxycurl.models.UrlResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.UrlResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/profile/resolve',
            params={
                'first_name': first_name,
                'company_domain': company_domain,
                'location': location,
                'title': title,
                'last_name': last_name,
            },
            data={
            },
            result_class=UrlResult
        )

    def resolve_by_email(
        self,
        work_email: str,
    ) -> UrlResult:
        """Reverse Work Email Lookup Endpoint
        
        Resolve LinkedIn Profile from a work email address
        
        :param work_email: Work email address of the user
        :type work_email: str
        :return: An object of :class:`proxycurl.models.UrlResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.UrlResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/profile/resolve/email',
            params={
                'work_email': work_email,
            },
            data={
            },
            result_class=UrlResult
        )

    def lookup_email(
        self,
        linkedin_profile_url: str,
        callback_url: str = '',
    ) -> ExtractionEmailResult:
        """Work Email Lookup Endpoint
        
                
        Lookup work email address of a LinkedIn Person Profile.

        Email addresses returned are verified to not be role-based or catch-all emails. Email addresses
        returned by our API endpoint come with a 95+% deliverability guarantee

        **Endpoint behavior**

        *This endpoint* **_may not_** *return results immediately.*

        For some profiles, email addresses are returned immediately when the endpoint is called. For such
        requests, we will respond with a `200` status code. Credits will be consumed immediately

        Some profiles require more time to extract email address from. For such requests, we will respond
        with a `202` status code. No credits are consumed.

        If you provided a webhook in your request parameter, our application will call your webhook with
        the result once. See `Webhook payload` below.

        Alternatively, you can also poll (repeat the request) our API and we will return the result once it is
        successful.

        Successful responses to requests are cached for up to 24 hours. We will also not charge you for the
        same request in a 24 hour window

        
        :param linkedin_profile_url: Linkedin Profile URL of the person you want to
            extract work email address from.
        :type linkedin_profile_url: str
        :param callback_url: Webhook to notify your application when
            the request has finished processing.
        :type callback_url: str
        :return: An object of :class:`proxycurl.models.ExtractionEmailResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.ExtractionEmailResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/profile/email',
            params={
                'linkedin_profile_url': linkedin_profile_url,
                'callback_url': callback_url,
            },
            data={
            },
            result_class=ExtractionEmailResult
        )

    def personal_contact(
        self,
        linkedin_profile_url: str,
    ) -> PDLPhoneNumberResult:
        """Personal Contact Number Lookup Endpoint
        
        Given an LinkedIn profile, returns a list of personal contact numbers belonging to this identity.
        
        :param linkedin_profile_url: LinkedIn Profile URL of the person you want to extract personal contact numbers from.
        :type linkedin_profile_url: str
        :return: An object of :class:`proxycurl.models.PDLPhoneNumberResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.PDLPhoneNumberResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/contact-api/personal-contact',
            params={
                'linkedin_profile_url': linkedin_profile_url,
            },
            data={
            },
            result_class=PDLPhoneNumberResult
        )

    def personal_email(
        self,
        linkedin_profile_url: str,
    ) -> PDLEmailResult:
        """Personal Email Lookup Endpoint
        
        Given an LinkedIn profile, returns a list of personal emails belonging to this identity. Emails are verified to be deliverable.
        
        :param linkedin_profile_url: LinkedIn Profile URL of the person you want to extract personal email addresses from.
        :type linkedin_profile_url: str
        :return: An object of :class:`proxycurl.models.PDLEmailResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.PDLEmailResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/contact-api/personal-email',
            params={
                'linkedin_profile_url': linkedin_profile_url,
            },
            data={
            },
            result_class=PDLEmailResult
        )


class _LinkedinCompany:
    def __init__(self, linkedin):
        self.linkedin = linkedin

    def get(
        self,
        url: str,
        categories: str = 'exclude',
        funding_data: str = 'exclude',
        extra: str = 'exclude',
        exit_data: str = 'exclude',
        acquisitions: str = 'exclude',
        use_cache: str = 'if-recent',
    ) -> LinkedinCompany:
        """Company Profile Endpoint
        
        Get structured data of a Company Profile
        
        :param url: URL of the LinkedIn Company Profile to crawl.

            URL should be in the format of `https://www.linkedin.com/company/<public_identifier>`
        :type url: str
        :param categories: Appends categories data of this company.

            Default value is `"exclude"`.
            The other acceptable value is `"include"`, which will include these categories (if available) for `1` extra credit., defaults to 'exclude'
        :type categories: str
        :param funding_data: Returns a list of funding rounds that this company has received.

            Default value is `"exclude"`.
            The other acceptable value is `"include"`, which will include these categories (if available) for `1` extra credit., defaults to 'exclude'
        :type funding_data: str
        :param extra: Enriches the Company Profile with extra details from external sources. Details include Crunchbase ranking, contact email, phone number, Facebook account, Twitter account, funding rounds and amount, IPO status, investor information, etc.

            Default value is `"exclude"`.
            The other acceptable value is `"include"`, which will include these extra details (if available) for `1` extra credit., defaults to 'exclude'
        :type extra: str
        :param exit_data: Returns a list of investment portfolio exits.

            Default value is `"exclude"`.
            The other acceptable value is `"include"`, which will include these categories (if available) for `1` extra credit., defaults to 'exclude'
        :type exit_data: str
        :param acquisitions: Provides further enriched data on acquisitions made by this company from external sources.

            Default value is `"exclude"`.
            The other acceptable value is `"include"`, which will include these acquisition data (if available) for `1` extra credit., defaults to 'exclude'
        :type acquisitions: str
        :param use_cache: `if-present` Fetches profile from cache regardless of age of profile. If profile is not available in cache, API will attempt to source profile externally.

            `if-recent` The default behavior. API will make a best effort to return a fresh profile no older than 29 days., defaults to 'if-recent'
        :type use_cache: str
        :return: An object of :class:`proxycurl.models.LinkedinCompany` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.LinkedinCompany`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/company',
            params={
                'url': url,
                'categories': categories,
                'funding_data': funding_data,
                'extra': extra,
                'exit_data': exit_data,
                'acquisitions': acquisitions,
                'use_cache': use_cache,
            },
            data={
            },
            result_class=LinkedinCompany
        )

    def resolve(
        self,
        location: str = '',
        company_domain: str = '',
        company_name: str = '',
    ) -> UrlResult:
        """Company Lookup Endpoint
        
        Resolve Company LinkedIn Profile from company name, domain name and location.
        
        :param location: The location / region of company.
            ISO 3166-1 alpha-2 codes
        :type location: str
        :param company_domain: Company website or Company domain
        :type company_domain: str
        :param company_name: Company Name
        :type company_name: str
        :return: An object of :class:`proxycurl.models.UrlResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.UrlResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/company/resolve',
            params={
                'location': location,
                'company_domain': company_domain,
                'company_name': company_name,
            },
            data={
            },
            result_class=UrlResult
        )

    def find_job(
        self,
        search_id: str,
    ) -> JobListPage:
        """Jobs Listing Endpoint
        
        List jobs posted by a company on LinkedIn
        
        :param search_id: The `search_id` of the company on LinkedIn.
            You can get the `search_id` of a LinkedIn company via [Company Profile API](#company-api-linkedin-company-profile-endpoint).
        :type search_id: str
        :return: An object of :class:`proxycurl.models.JobListPage` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.JobListPage`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/v2/linkedin/company/job',
            params={
                'search_id': search_id,
            },
            data={
            },
            result_class=JobListPage
        )

    def employee_count(
        self,
        url: str,
        employment_status: str = 'current',
    ) -> EmployeeCount:
        """Employee Count Endpoint
        
                

        Get a number of total employees of a Company.

        This API endpoint is limited by LinkDB which is populated with profiles in the US, UK, Canada, Israel, Australia and Singapore. As such, this endpoint is best used to list employees working in companies based in the US, UK, Canada, Israel, Australia and Singapore only.


        
        :param url: URL of the LinkedIn Company Profile to target.

            URL should be in the format of `https://www.linkedin.com/company/<public_identifier>`
        :type url: str
        :param employment_status: Parameter to tell the API to filter past or current employees.

            Valid values are `current`, `past`, and `all`:

            * `current` (default) : count current employees
            * `past` : count past employees
            * `all` : count current & past employees, defaults to 'current'
        :type employment_status: str
        :return: An object of :class:`proxycurl.models.EmployeeCount` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.EmployeeCount`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/company/employees/count',
            params={
                'url': url,
                'employment_status': employment_status,
            },
            data={
            },
            result_class=EmployeeCount
        )

    def employee_list(
        self,
        url: str,
        employment_status: str = 'current',
    ) -> EmployeeList:
        """Employee Listing Endpoint
        
                

        Get a list of employees of a Company.

        This API endpoint is limited by LinkDB which is populated with profiles in the US, UK, Canada, Israel, Australia and Singapore. As such, this endpoint is best used to list employees working in companies based in the US, UK, Canada, Israel, Australia and Singapore only.

        
        :param url: URL of the LinkedIn Company Profile to target.

            URL should be in the format of `https://www.linkedin.com/company/<public_identifier>`
        :type url: str
        :param employment_status: Parameter to tell the API to return past or current employees.

            Valid values are `current`, `past`, and `all`:

            * `current` (default) : lists current employees
            * `past` : lists past employees
            * `all` : lists current & past employees, defaults to 'current'
        :type employment_status: str
        :return: An object of :class:`proxycurl.models.EmployeeList` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.EmployeeList`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/company/employees',
            params={
                'url': url,
                'employment_status': employment_status,
            },
            data={
            },
            result_class=EmployeeList
        )

    def role_lookup(
        self,
        company_name: str,
        role: str,
    ) -> RoleSearchResult:
        """Role Lookup Endpoint
        
        Finds the closest (person) profile with a given role in a Company. For example, you can use this endpoint to find the "CTO" of "Apple".
        
        :param company_name: Name of the company that you are searching for
        :type company_name: str
        :param role: Role of the profile that you are lookin up
        :type role: str
        :return: An object of :class:`proxycurl.models.RoleSearchResult` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.RoleSearchResult`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/find/company/role',
            params={
                'company_name': company_name,
                'role': role,
            },
            data={
            },
            result_class=RoleSearchResult
        )

    def reveal(
        self,
        ip: str,
        role: str = '',
        role_personal_email: str = 'exclude',
        role_contact_number: str = 'exclude',
    ) -> CompanyReveal:
        """Reveal Endpoint
        
        Deanonymize an IPv4 address and associate the Company behind the IPv4 address.
        
        :param ip: The target IPv4 address.
        :type ip: str
        :param role: Lookup and append an employee of a certain role of the company.
            Within the same API call, you can choose to lookup a person with a given role within this organisation that you might want to reach out to.
        :type role: str
        :param role_personal_email: Append personal email addresses to the response if the system finds a relevant person profile., defaults to 'exclude'
        :type role_personal_email: str
        :param role_contact_number: Append personal contact numbers to teh response if the system finds a relevant person profile., defaults to 'exclude'
        :type role_contact_number: str
        :return: An object of :class:`proxycurl.models.CompanyReveal` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.CompanyReveal`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/reveal/company',
            params={
                'ip': ip,
                'role': role,
                'role_personal_email': role_personal_email,
                'role_contact_number': role_contact_number,
            },
            data={
            },
            result_class=CompanyReveal
        )


class _LinkedinSchool:
    def __init__(self, linkedin):
        self.linkedin = linkedin

    def get(
        self,
        url: str,
        use_cache: str = 'if-recent',
    ) -> LinkedinSchool:
        """School Profile Endpoint
        
        Get structured data of a LinkedIn School Profile
        
        :param url: URL of the LinkedIn School Profile to crawl.

            URL should be in the format of `https://www.linkedin.com/school/<public_identifier>`
        :type url: str
        :param use_cache: `if-present` Fetches profile from cache regardless of age of profile. If profile is not available in cache, API will attempt to source profile externally..

            `if-recent` The default behavior. API will make a best effort to return a fresh profile no older than 29 days., defaults to 'if-recent'
        :type use_cache: str
        :return: An object of :class:`proxycurl.models.LinkedinSchool` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.LinkedinSchool`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/school',
            params={
                'url': url,
                'use_cache': use_cache,
            },
            data={
            },
            result_class=LinkedinSchool
        )


class _LinkedinJob:
    def __init__(self, linkedin):
        self.linkedin = linkedin

    def get(
        self,
        url: str,
    ) -> LinkedinJob:
        """Job Profile Endpoint
        
        Get structured data of a LinkedIn Job Profile
        
        :param url: URL of the LinkedIn Job Profile to target.

            URL should be in the format of `https://www.linkedin.com/jobs/view/<job_id>`.
            [Jobs Listing Endpoint](#jobs-api-linkedin-jobs-listing-endpoint) can be used to retrieve a job URL.
        :type url: str
        :return: An object of :class:`proxycurl.models.LinkedinJob` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.LinkedinJob`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/linkedin/job',
            params={
                'url': url,
            },
            data={
            },
            result_class=LinkedinJob
        )


class _Linkedin:
    person: _LinkedinPerson
    company: _LinkedinCompany
    school: _LinkedinSchool
    job: _LinkedinJob

    def __init__(self, proxycurl):
        self.proxycurl = proxycurl
        self.person = _LinkedinPerson(self)
        self.company = _LinkedinCompany(self)
        self.school = _LinkedinSchool(self)
        self.job = _LinkedinJob(self)


class Proxycurl(ProxycurlBase):
    linkedin: _Linkedin

    def __init__(
        self,
        api_key: str = PROXYCURL_API_KEY,
        base_url: str = BASE_URL,
        timeout: int = TIMEOUT,
        max_retries: int = MAX_RETRIES,
        max_backoff_seconds: int = MAX_BACKOFF_SECONDS
    ) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self.max_backoff_seconds = max_backoff_seconds
        self.linkedin = _Linkedin(self)

    def get_balance(
        self,
    ) -> CreditBalance:
        """View Credit Balance Endpoint
        
        Get your current credit(s) balance
        
        :return: An object of :class:`proxycurl.models.CreditBalance` or **None** if there is an error.
        :rtype: :class:`proxycurl.models.CreditBalance`
        :raise ProxycurlException: Every error will raise a :class:`proxycurl.gevent.ProxycurlException`

        """

        return self.linkedin.proxycurl.request(
            method='GET',
            url='/proxycurl/api/credit-balance',
            params={
            },
            data={
            },
            result_class=CreditBalance
        )
