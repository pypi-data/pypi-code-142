"""
The `HTTPStatus` class stores HTTP status codes from your message.
Use the instance of this class to get the status codes.
"""


class HTTPStatus:
    continue_100 = 100
    switching_protocol_101 = 101
    processing_102 = 102
    early_hints_103 = 103

    ok_200 = 200
    created_201 = 201
    accepted_202 = 202
    non_authoritative_information_203 = 203
    no_content_204 = 204
    reset_content_205 = 205
    partial_content_206 = 206
    multi_status_207 = 207
    im_used_226 = 226

    multiple_choice_300 = 300
    moved_permanently_301 = 301
    found_302 = 302
    see_other_303 = 303
    not_modified_304 = 304
    temporary_redirect_307 = 307
    permanent_redirect_308 = 308

    bad_request_400 = 400
    unauthorized_401 = 401
    payment_required_402 = 402
    forbidden_403 = 403
    not_found_404 = 404
    method_not_allowed_405 = 405
    not_acceptable_406 = 406
    proxy_authentication_required_407 = 407
    request_timeout_408 = 408
    conflict_409 = 409
    gone_410 = 410
    length_required_411 = 411
    precondition_failed_412 = 412
    payload_too_large_413 = 413
    uri_too_long_414 = 414
    unsupported_media_type_415 = 415
    requested_range_not_satisfiable_416 = 416
    expectation_failed_417 = 417
    im_a_teapot_418 = 418
    misdirected_request_421 = 421
    unprocessable_entity_422 = 422
    locked_423 = 423
    failed_dependency_424 = 424
    too_early_425 = 425
    upgrade_required_426 = 426
    precondition_required_428 = 428
    too_many_requests_429 = 429
    request_header_fields_too_large_431 = 431
    unavailable_for_legal_reasons_451 = 451

    internal_server_error_500 = 500
    not_implemented_501 = 501
    bad_gateway_502 = 502
    service_unavailable_503 = 503
    gateway_timeout_504 = 504
    http_version_not_supported_505 = 505
    variant_also_negotiates_506 = 506
    insufficient_storage_507 = 507
    loop_detected_508 = 508
    not_extended_510 = 510
    network_authentication_required_511 = 511


status = HTTPStatus()
