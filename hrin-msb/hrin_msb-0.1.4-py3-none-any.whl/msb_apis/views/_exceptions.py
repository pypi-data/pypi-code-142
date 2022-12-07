from msb_exceptions import ApiException


class CrudApiExceptions:
	class CreateOperationFailed(ApiException):
		_message = "Failed to create the requested data."

	class DeleteOperationFailed(ApiException):
		_message = "Failed to delete the requested data."


	class UpdateOperationFailed(ApiException):
		_message = "Failed to update the requested data."


	class RetrieveOperationFailed(ApiException):
		_message = "Failed to retrieve the requested data."