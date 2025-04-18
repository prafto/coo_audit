# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from onboarding_service import estimated_sales_pb2 as onboarding__service_dot_estimated__sales__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in onboarding_service/estimated_sales_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class EstimatedSalesServiceStub(object):
    """Service used to get Estimated Sales in an area
    The options not listed here use Hermes default.
    The following applies for all RPCs in the service, if not overridden on individual RPCs.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetEstimatedSales = channel.unary_unary(
                '/doordash_onboarding_service.v1.EstimatedSalesService/GetEstimatedSales',
                request_serializer=onboarding__service_dot_estimated__sales__pb2.GetEstimatedSalesRequest.SerializeToString,
                response_deserializer=onboarding__service_dot_estimated__sales__pb2.GetEstimatedSalesResponse.FromString,
                _registered_method=True)


class EstimatedSalesServiceServicer(object):
    """Service used to get Estimated Sales in an area
    The options not listed here use Hermes default.
    The following applies for all RPCs in the service, if not overridden on individual RPCs.
    """

    def GetEstimatedSales(self, request, context):
        """API to get Estimated Sales based on ip address or physical address
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EstimatedSalesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetEstimatedSales': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEstimatedSales,
                    request_deserializer=onboarding__service_dot_estimated__sales__pb2.GetEstimatedSalesRequest.FromString,
                    response_serializer=onboarding__service_dot_estimated__sales__pb2.GetEstimatedSalesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'doordash_onboarding_service.v1.EstimatedSalesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('doordash_onboarding_service.v1.EstimatedSalesService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class EstimatedSalesService(object):
    """Service used to get Estimated Sales in an area
    The options not listed here use Hermes default.
    The following applies for all RPCs in the service, if not overridden on individual RPCs.
    """

    @staticmethod
    def GetEstimatedSales(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/doordash_onboarding_service.v1.EstimatedSalesService/GetEstimatedSales',
            onboarding__service_dot_estimated__sales__pb2.GetEstimatedSalesRequest.SerializeToString,
            onboarding__service_dot_estimated__sales__pb2.GetEstimatedSalesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
