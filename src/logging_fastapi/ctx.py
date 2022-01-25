from contextvars import ContextVar

span_ctx = ContextVar("span")
error_ctx = ContextVar("error")
request_id_ctx = ContextVar("requestId")
