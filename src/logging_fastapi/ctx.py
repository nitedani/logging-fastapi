from contextvars import ContextVar

span_ctx = ContextVar("span")
request_id_ctx = ContextVar("requestId")
error_ctx = ContextVar("error")
