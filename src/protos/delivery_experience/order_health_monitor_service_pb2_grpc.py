# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from delivery_experience import order_health_monitor_service_pb2 as delivery__experience_dot_order__health__monitor__service__pb2

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
        + f' but the generated code in delivery_experience/order_health_monitor_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class OrderHealthMonitorServiceStub(object):
    """The main Order Health Monitor gRPC service. 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateOrderMonitorWorkflow = channel.unary_unary(
                '/delivery_experience.v1.OrderHealthMonitorService/CreateOrderMonitorWorkflow',
                request_serializer=delivery__experience_dot_order__health__monitor__service__pb2.CreateOrderMonitorWorkflowRequest.SerializeToString,
                response_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.CreateOrderMonitorWorkflowResponse.FromString,
                _registered_method=True)
        self.CreateLatenessMonitorWorkflow = channel.unary_unary(
                '/delivery_experience.v1.OrderHealthMonitorService/CreateLatenessMonitorWorkflow',
                request_serializer=delivery__experience_dot_order__health__monitor__service__pb2.CreateLatenessMonitorWorkflowRequest.SerializeToString,
                response_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.CreateLatenessMonitorWorkflowResponse.FromString,
                _registered_method=True)
        self.UpdateLatenessMonitorWorkflow = channel.unary_unary(
                '/delivery_experience.v1.OrderHealthMonitorService/UpdateLatenessMonitorWorkflow',
                request_serializer=delivery__experience_dot_order__health__monitor__service__pb2.UpdateLatenessMonitorWorkflowRequest.SerializeToString,
                response_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.UpdateLatenessMonitorWorkflowResponse.FromString,
                _registered_method=True)
        self.UpdateDeliveryStatus = channel.unary_unary(
                '/delivery_experience.v1.OrderHealthMonitorService/UpdateDeliveryStatus',
                request_serializer=delivery__experience_dot_order__health__monitor__service__pb2.UpdateDeliveryStatusRequest.SerializeToString,
                response_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.UpdateDeliveryStatusResponse.FromString,
                _registered_method=True)
        self.CreatePickupMxLateConfirmWorkflow = channel.unary_unary(
                '/delivery_experience.v1.OrderHealthMonitorService/CreatePickupMxLateConfirmWorkflow',
                request_serializer=delivery__experience_dot_order__health__monitor__service__pb2.CreatePickupMxLateConfirmWorkflowRequest.SerializeToString,
                response_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.CreatePickupMxLateConfirmWorkflowResponse.FromString,
                _registered_method=True)
        self.CreateCancellationRefundWorkflow = channel.unary_unary(
                '/delivery_experience.v1.OrderHealthMonitorService/CreateCancellationRefundWorkflow',
                request_serializer=delivery__experience_dot_order__health__monitor__service__pb2.CreateCancellationRefundWorkflowRequest.SerializeToString,
                response_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.CreateCancellationRefundWorkflowResponse.FromString,
                _registered_method=True)
        self.UpdateCancellationRefundWorkflow = channel.unary_unary(
                '/delivery_experience.v1.OrderHealthMonitorService/UpdateCancellationRefundWorkflow',
                request_serializer=delivery__experience_dot_order__health__monitor__service__pb2.UpdateCancellationRefundWorkflowRequest.SerializeToString,
                response_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.UpdateCancellationRefundWorkflowResponse.FromString,
                _registered_method=True)
        self.HandleOrderMayBeReadyNotification = channel.unary_unary(
                '/delivery_experience.v1.OrderHealthMonitorService/HandleOrderMayBeReadyNotification',
                request_serializer=delivery__experience_dot_order__health__monitor__service__pb2.HandleOrderMayBeReadyNotificationRequest.SerializeToString,
                response_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.HandleOrderMayBeReadyNotificationResponse.FromString,
                _registered_method=True)
        self.GetRealtimeDisasterTrackerLateDeliveries = channel.unary_unary(
                '/delivery_experience.v1.OrderHealthMonitorService/GetRealtimeDisasterTrackerLateDeliveries',
                request_serializer=delivery__experience_dot_order__health__monitor__service__pb2.GetRealtimeDisasterTrackerLateDeliveriesRequest.SerializeToString,
                response_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.GetRealtimeDisasterTrackerLateDeliveriesResponse.FromString,
                _registered_method=True)


class OrderHealthMonitorServiceServicer(object):
    """The main Order Health Monitor gRPC service. 
    """

    def CreateOrderMonitorWorkflow(self, request, context):
        """Creates the order monitor workflow for the requested delivery. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateLatenessMonitorWorkflow(self, request, context):
        """Creates the order monitor workflow for expected lateness. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateLatenessMonitorWorkflow(self, request, context):
        """Updates the order monitor workflow for expected lateness. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDeliveryStatus(self, request, context):
        """Updates delivery's dropoff or cancel status. 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePickupMxLateConfirmWorkflow(self, request, context):
        """Creates the Mx late confirmation notification workflow for the requested pickup order 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCancellationRefundWorkflow(self, request, context):
        """Creates the Cancellation Refund workflow for the cancelled order 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateCancellationRefundWorkflow(self, request, context):
        """Updates the Cancellation Refund workflow for the cancelled order 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HandleOrderMayBeReadyNotification(self, request, context):
        """Kick off the notification flow for Order May Be Ready 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRealtimeDisasterTrackerLateDeliveries(self, request, context):
        """Returns a list of deliveries which are late, used by realtime disaster tracker only 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrderHealthMonitorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateOrderMonitorWorkflow': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOrderMonitorWorkflow,
                    request_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.CreateOrderMonitorWorkflowRequest.FromString,
                    response_serializer=delivery__experience_dot_order__health__monitor__service__pb2.CreateOrderMonitorWorkflowResponse.SerializeToString,
            ),
            'CreateLatenessMonitorWorkflow': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateLatenessMonitorWorkflow,
                    request_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.CreateLatenessMonitorWorkflowRequest.FromString,
                    response_serializer=delivery__experience_dot_order__health__monitor__service__pb2.CreateLatenessMonitorWorkflowResponse.SerializeToString,
            ),
            'UpdateLatenessMonitorWorkflow': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateLatenessMonitorWorkflow,
                    request_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.UpdateLatenessMonitorWorkflowRequest.FromString,
                    response_serializer=delivery__experience_dot_order__health__monitor__service__pb2.UpdateLatenessMonitorWorkflowResponse.SerializeToString,
            ),
            'UpdateDeliveryStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDeliveryStatus,
                    request_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.UpdateDeliveryStatusRequest.FromString,
                    response_serializer=delivery__experience_dot_order__health__monitor__service__pb2.UpdateDeliveryStatusResponse.SerializeToString,
            ),
            'CreatePickupMxLateConfirmWorkflow': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePickupMxLateConfirmWorkflow,
                    request_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.CreatePickupMxLateConfirmWorkflowRequest.FromString,
                    response_serializer=delivery__experience_dot_order__health__monitor__service__pb2.CreatePickupMxLateConfirmWorkflowResponse.SerializeToString,
            ),
            'CreateCancellationRefundWorkflow': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCancellationRefundWorkflow,
                    request_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.CreateCancellationRefundWorkflowRequest.FromString,
                    response_serializer=delivery__experience_dot_order__health__monitor__service__pb2.CreateCancellationRefundWorkflowResponse.SerializeToString,
            ),
            'UpdateCancellationRefundWorkflow': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateCancellationRefundWorkflow,
                    request_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.UpdateCancellationRefundWorkflowRequest.FromString,
                    response_serializer=delivery__experience_dot_order__health__monitor__service__pb2.UpdateCancellationRefundWorkflowResponse.SerializeToString,
            ),
            'HandleOrderMayBeReadyNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.HandleOrderMayBeReadyNotification,
                    request_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.HandleOrderMayBeReadyNotificationRequest.FromString,
                    response_serializer=delivery__experience_dot_order__health__monitor__service__pb2.HandleOrderMayBeReadyNotificationResponse.SerializeToString,
            ),
            'GetRealtimeDisasterTrackerLateDeliveries': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRealtimeDisasterTrackerLateDeliveries,
                    request_deserializer=delivery__experience_dot_order__health__monitor__service__pb2.GetRealtimeDisasterTrackerLateDeliveriesRequest.FromString,
                    response_serializer=delivery__experience_dot_order__health__monitor__service__pb2.GetRealtimeDisasterTrackerLateDeliveriesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'delivery_experience.v1.OrderHealthMonitorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('delivery_experience.v1.OrderHealthMonitorService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class OrderHealthMonitorService(object):
    """The main Order Health Monitor gRPC service. 
    """

    @staticmethod
    def CreateOrderMonitorWorkflow(request,
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
            '/delivery_experience.v1.OrderHealthMonitorService/CreateOrderMonitorWorkflow',
            delivery__experience_dot_order__health__monitor__service__pb2.CreateOrderMonitorWorkflowRequest.SerializeToString,
            delivery__experience_dot_order__health__monitor__service__pb2.CreateOrderMonitorWorkflowResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateLatenessMonitorWorkflow(request,
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
            '/delivery_experience.v1.OrderHealthMonitorService/CreateLatenessMonitorWorkflow',
            delivery__experience_dot_order__health__monitor__service__pb2.CreateLatenessMonitorWorkflowRequest.SerializeToString,
            delivery__experience_dot_order__health__monitor__service__pb2.CreateLatenessMonitorWorkflowResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateLatenessMonitorWorkflow(request,
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
            '/delivery_experience.v1.OrderHealthMonitorService/UpdateLatenessMonitorWorkflow',
            delivery__experience_dot_order__health__monitor__service__pb2.UpdateLatenessMonitorWorkflowRequest.SerializeToString,
            delivery__experience_dot_order__health__monitor__service__pb2.UpdateLatenessMonitorWorkflowResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateDeliveryStatus(request,
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
            '/delivery_experience.v1.OrderHealthMonitorService/UpdateDeliveryStatus',
            delivery__experience_dot_order__health__monitor__service__pb2.UpdateDeliveryStatusRequest.SerializeToString,
            delivery__experience_dot_order__health__monitor__service__pb2.UpdateDeliveryStatusResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreatePickupMxLateConfirmWorkflow(request,
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
            '/delivery_experience.v1.OrderHealthMonitorService/CreatePickupMxLateConfirmWorkflow',
            delivery__experience_dot_order__health__monitor__service__pb2.CreatePickupMxLateConfirmWorkflowRequest.SerializeToString,
            delivery__experience_dot_order__health__monitor__service__pb2.CreatePickupMxLateConfirmWorkflowResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def CreateCancellationRefundWorkflow(request,
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
            '/delivery_experience.v1.OrderHealthMonitorService/CreateCancellationRefundWorkflow',
            delivery__experience_dot_order__health__monitor__service__pb2.CreateCancellationRefundWorkflowRequest.SerializeToString,
            delivery__experience_dot_order__health__monitor__service__pb2.CreateCancellationRefundWorkflowResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateCancellationRefundWorkflow(request,
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
            '/delivery_experience.v1.OrderHealthMonitorService/UpdateCancellationRefundWorkflow',
            delivery__experience_dot_order__health__monitor__service__pb2.UpdateCancellationRefundWorkflowRequest.SerializeToString,
            delivery__experience_dot_order__health__monitor__service__pb2.UpdateCancellationRefundWorkflowResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def HandleOrderMayBeReadyNotification(request,
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
            '/delivery_experience.v1.OrderHealthMonitorService/HandleOrderMayBeReadyNotification',
            delivery__experience_dot_order__health__monitor__service__pb2.HandleOrderMayBeReadyNotificationRequest.SerializeToString,
            delivery__experience_dot_order__health__monitor__service__pb2.HandleOrderMayBeReadyNotificationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetRealtimeDisasterTrackerLateDeliveries(request,
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
            '/delivery_experience.v1.OrderHealthMonitorService/GetRealtimeDisasterTrackerLateDeliveries',
            delivery__experience_dot_order__health__monitor__service__pb2.GetRealtimeDisasterTrackerLateDeliveriesRequest.SerializeToString,
            delivery__experience_dot_order__health__monitor__service__pb2.GetRealtimeDisasterTrackerLateDeliveriesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
