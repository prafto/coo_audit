# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: delivery_experience/order_health_monitor_service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'delivery_experience/order_health_monitor_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6delivery_experience/order_health_monitor_service.proto\x12\x16\x64\x65livery_experience.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\":\n!CreateOrderMonitorWorkflowRequest\x12\x15\n\rdelivery_uuid\x18\x01 \x01(\t\";\n\"CreateOrderMonitorWorkflowResponse\x12\x15\n\rdelivery_uuid\x18\x01 \x01(\t\"=\n$CreateLatenessMonitorWorkflowRequest\x12\x15\n\rdelivery_uuid\x18\x01 \x01(\t\">\n%CreateLatenessMonitorWorkflowResponse\x12\x15\n\rdelivery_uuid\x18\x01 \x01(\t\"\x81\x02\n$UpdateLatenessMonitorWorkflowRequest\x12\x15\n\rdelivery_uuid\x18\x01 \x01(\t\x12\x13\n\x0b\x64ropped_off\x18\x02 \x01(\x08\x12\x11\n\tcancelled\x18\x03 \x01(\x08\x12S\n\x06\x64\x65tail\x18\x04 \x01(\x0b\x32\x43.delivery_experience.v1.UpdateLatenessMonitorWorkflowRequest.Detail\x1a\x45\n\x06\x44\x65tail\x12\x1c\n\x14is_far_away_delivery\x18\x01 \x01(\x08\x12\x1d\n\x15is_dasher_geospoofing\x18\x02 \x01(\x08\">\n%UpdateLatenessMonitorWorkflowResponse\x12\x15\n\rdelivery_uuid\x18\x01 \x01(\t\"\\\n\x1bUpdateDeliveryStatusRequest\x12\x15\n\rdelivery_uuid\x18\x01 \x01(\t\x12\x13\n\x0b\x64ropped_off\x18\x02 \x01(\x08\x12\x11\n\tcancelled\x18\x03 \x01(\x08\"5\n\x1cUpdateDeliveryStatusResponse\x12\x15\n\rdelivery_uuid\x18\x01 \x01(\t\"\x91\x01\n(CreatePickupMxLateConfirmWorkflowRequest\x12\x33\n\rdelivery_uuid\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\x0b\x64\x65livery_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"+\n)CreatePickupMxLateConfirmWorkflowResponse\"\x90\x01\n\'CreateCancellationRefundWorkflowRequest\x12\x33\n\rdelivery_uuid\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\norder_uuid\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"*\n(CreateCancellationRefundWorkflowResponse\"\x8f\x01\n\'UpdateCancellationRefundWorkflowRequest\x12\x33\n\rdelivery_uuid\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x0bis_refunded\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\"*\n(UpdateCancellationRefundWorkflowResponse\"\x91\x01\n(HandleOrderMayBeReadyNotificationRequest\x12\x33\n\rdelivery_uuid\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\x0b\x64\x65livery_id\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\"+\n)HandleOrderMayBeReadyNotificationResponse\"\x89\x01\n OrderHealthMonitorTimeBasedEvent\x12\x15\n\rdelivery_uuid\x18\x01 \x01(\t\x12\x39\n\x0cproblem_type\x18\x03 \x01(\x0e\x32#.delivery_experience.v1.ProblemTypeJ\x04\x08\x02\x10\x03R\rexpected_late\"\xb9\x01\n\x11\x45xpectedLateEvent\x12,\n\x08\x65stimate\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\trange_min\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\trange_max\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10lateness_seconds\x18\x04 \x01(\x03\"\xd3\x03\n/GetRealtimeDisasterTrackerLateDeliveriesRequest\x12.\n\tlist_size\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x37\n\x12time_range_minutes\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x36\n\x11pagination_offset\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12-\n\x08\x61gent_id\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x39\n\x0cproblem_type\x18\x05 \x01(\x0e\x32#.delivery_experience.v1.ProblemType\x12-\n\x07\x63ountry\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x66\n\x07\x63x_type\x18\x07 \x01(\x0e\x32U.delivery_experience.v1.GetRealtimeDisasterTrackerLateDeliveriesResponse.ConsumerType\"\xbc\x0c\n0GetRealtimeDisasterTrackerLateDeliveriesResponse\x12\x65\n\ndeliveries\x18\x01 \x03(\x0b\x32Q.delivery_experience.v1.GetRealtimeDisasterTrackerLateDeliveriesResponse.Delivery\x12\x34\n\x0ftotal_row_count\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x1a\xa0\t\n\x08\x44\x65livery\x12-\n\x08order_id\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x33\n\rconsumer_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0corder_status\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x15\x63onsumer_phone_number\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x14quoted_delivery_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x64ynamic_eta\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x08lateness\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12:\n\x15time_to_confirm_order\x18\x08 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x36\n\x11time_to_assign_dx\x18\t \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12;\n\x16number_of_dx_unassigns\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x30\n\x0bpickup_time\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12l\n\rdelivery_type\x18\x0c \x01(\x0e\x32U.delivery_experience.v1.GetRealtimeDisasterTrackerLateDeliveriesResponse.DeliveryType\x12\x38\n\x12salesforce_case_id\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x66\n\x07\x63x_type\x18\x0e \x01(\x0e\x32U.delivery_experience.v1.GetRealtimeDisasterTrackerLateDeliveriesResponse.ConsumerType\x12\x33\n\rdelivery_uuid\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x39\n\x0cproblem_type\x18\x10 \x01(\x0e\x32#.delivery_experience.v1.ProblemType\x12.\n\ncreated_at\x18\x11 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10pickup_timestamp\x18\x12 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x08\x61gent_id\x18\x13 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12-\n\x07\x63ountry\x18\x14 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"c\n\x0c\x43onsumerType\x12\x1d\n\x19\x43ONSUMER_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13\x43ONSUMER_TYPE_WHALE\x10\x01\x12\x1b\n\x17\x43ONSUMER_TYPE_NON_WHALE\x10\x02\"c\n\x0c\x44\x65liveryType\x12\x1d\n\x19\x44\x45LIVERY_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16\x44\x45LIVERY_TYPE_DELIVERY\x10\x01\x12\x18\n\x14\x44\x45LIVERY_TYPE_PICKUP\x10\x02\"\x88\x01\n#PickupOrderMayBeReadySegmentMessage\x12\x15\n\rdelivery_uuid\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65livery_id\x18\x02 \x01(\t\x12\x12\n\npickup_eta\x18\x03 \x01(\t\x12\x10\n\x08store_id\x18\x04 \x01(\t\x12\x0f\n\x07user_id\x18\x05 \x01(\t*\xcc\x04\n\x0bProblemType\x12\x1c\n\x18PROBLEM_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aPROBLEM_TYPE_EXPECTED_LATE\x10\x01\x12\x15\n\x11PROBLEM_TYPE_LATE\x10\x02\x12*\n\"PROBLEM_TYPE_DELIVERY_PROMISE_LATE\x10\x03\x1a\x02\x08\x01\x12)\n%PROBLEM_TYPE_EXPECTED_LATE_CALCULATED\x10\x04\x12\x30\n,PROBLEM_TYPE_DELIVERY_PROMISE_PREDICTED_LATE\x10\x05\x12-\n)PROBLEM_TYPE_DELIVERY_PROMISE_ACTUAL_LATE\x10\x06\x12\x1d\n\x19PROBLEM_TYPE_CANCELLATION\x10\x07\x12-\n)PROBLEM_TYPE_PICKUP_ORDER_MX_LATE_CONFIRM\x10\x08\x12+\n\'PROBLEM_TYPE_REFUND_METHOD_NOT_SELECTED\x10\t\x12\"\n\x1ePROBLEM_TYPE_FAR_AWAY_DELIVERY\x10\n\x12#\n\x1fPROBLEM_TYPE_DASHER_GEOSPOOFING\x10\x0b\x12&\n\"PROBLEM_TYPE_MCDONALD_CANCELLATION\x10\x0c\x12#\n\x1fPROBLEM_TYPE_VALENTINE_SCHEDULE\x10\r\x12\x1f\n\x1bPROBLEM_TYPE_VALENTINE_LATE\x10\x0e\x32\xeb\x0b\n\x19OrderHealthMonitorService\x12\x95\x01\n\x1a\x43reateOrderMonitorWorkflow\x12\x39.delivery_experience.v1.CreateOrderMonitorWorkflowRequest\x1a:.delivery_experience.v1.CreateOrderMonitorWorkflowResponse\"\x00\x12\x9e\x01\n\x1d\x43reateLatenessMonitorWorkflow\x12<.delivery_experience.v1.CreateLatenessMonitorWorkflowRequest\x1a=.delivery_experience.v1.CreateLatenessMonitorWorkflowResponse\"\x00\x12\x9e\x01\n\x1dUpdateLatenessMonitorWorkflow\x12<.delivery_experience.v1.UpdateLatenessMonitorWorkflowRequest\x1a=.delivery_experience.v1.UpdateLatenessMonitorWorkflowResponse\"\x00\x12\x83\x01\n\x14UpdateDeliveryStatus\x12\x33.delivery_experience.v1.UpdateDeliveryStatusRequest\x1a\x34.delivery_experience.v1.UpdateDeliveryStatusResponse\"\x00\x12\xaa\x01\n!CreatePickupMxLateConfirmWorkflow\x12@.delivery_experience.v1.CreatePickupMxLateConfirmWorkflowRequest\x1a\x41.delivery_experience.v1.CreatePickupMxLateConfirmWorkflowResponse\"\x00\x12\xa7\x01\n CreateCancellationRefundWorkflow\x12?.delivery_experience.v1.CreateCancellationRefundWorkflowRequest\x1a@.delivery_experience.v1.CreateCancellationRefundWorkflowResponse\"\x00\x12\xa7\x01\n UpdateCancellationRefundWorkflow\x12?.delivery_experience.v1.UpdateCancellationRefundWorkflowRequest\x1a@.delivery_experience.v1.UpdateCancellationRefundWorkflowResponse\"\x00\x12\xaa\x01\n!HandleOrderMayBeReadyNotification\x12@.delivery_experience.v1.HandleOrderMayBeReadyNotificationRequest\x1a\x41.delivery_experience.v1.HandleOrderMayBeReadyNotificationResponse\"\x00\x12\xbf\x01\n(GetRealtimeDisasterTrackerLateDeliveries\x12G.delivery_experience.v1.GetRealtimeDisasterTrackerLateDeliveriesRequest\x1aH.delivery_experience.v1.GetRealtimeDisasterTrackerLateDeliveriesResponse\"\x00\x42\x1a\n\x13\x64\x65livery.experienceP\x01\x88\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'delivery_experience.order_health_monitor_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023delivery.experienceP\001\210\001\001'
  _globals['_PROBLEMTYPE'].values_by_name["PROBLEM_TYPE_DELIVERY_PROMISE_LATE"]._loaded_options = None
  _globals['_PROBLEMTYPE'].values_by_name["PROBLEM_TYPE_DELIVERY_PROMISE_LATE"]._serialized_options = b'\010\001'
  _globals['_PROBLEMTYPE']._serialized_start=4172
  _globals['_PROBLEMTYPE']._serialized_end=4760
  _globals['_CREATEORDERMONITORWORKFLOWREQUEST']._serialized_start=147
  _globals['_CREATEORDERMONITORWORKFLOWREQUEST']._serialized_end=205
  _globals['_CREATEORDERMONITORWORKFLOWRESPONSE']._serialized_start=207
  _globals['_CREATEORDERMONITORWORKFLOWRESPONSE']._serialized_end=266
  _globals['_CREATELATENESSMONITORWORKFLOWREQUEST']._serialized_start=268
  _globals['_CREATELATENESSMONITORWORKFLOWREQUEST']._serialized_end=329
  _globals['_CREATELATENESSMONITORWORKFLOWRESPONSE']._serialized_start=331
  _globals['_CREATELATENESSMONITORWORKFLOWRESPONSE']._serialized_end=393
  _globals['_UPDATELATENESSMONITORWORKFLOWREQUEST']._serialized_start=396
  _globals['_UPDATELATENESSMONITORWORKFLOWREQUEST']._serialized_end=653
  _globals['_UPDATELATENESSMONITORWORKFLOWREQUEST_DETAIL']._serialized_start=584
  _globals['_UPDATELATENESSMONITORWORKFLOWREQUEST_DETAIL']._serialized_end=653
  _globals['_UPDATELATENESSMONITORWORKFLOWRESPONSE']._serialized_start=655
  _globals['_UPDATELATENESSMONITORWORKFLOWRESPONSE']._serialized_end=717
  _globals['_UPDATEDELIVERYSTATUSREQUEST']._serialized_start=719
  _globals['_UPDATEDELIVERYSTATUSREQUEST']._serialized_end=811
  _globals['_UPDATEDELIVERYSTATUSRESPONSE']._serialized_start=813
  _globals['_UPDATEDELIVERYSTATUSRESPONSE']._serialized_end=866
  _globals['_CREATEPICKUPMXLATECONFIRMWORKFLOWREQUEST']._serialized_start=869
  _globals['_CREATEPICKUPMXLATECONFIRMWORKFLOWREQUEST']._serialized_end=1014
  _globals['_CREATEPICKUPMXLATECONFIRMWORKFLOWRESPONSE']._serialized_start=1016
  _globals['_CREATEPICKUPMXLATECONFIRMWORKFLOWRESPONSE']._serialized_end=1059
  _globals['_CREATECANCELLATIONREFUNDWORKFLOWREQUEST']._serialized_start=1062
  _globals['_CREATECANCELLATIONREFUNDWORKFLOWREQUEST']._serialized_end=1206
  _globals['_CREATECANCELLATIONREFUNDWORKFLOWRESPONSE']._serialized_start=1208
  _globals['_CREATECANCELLATIONREFUNDWORKFLOWRESPONSE']._serialized_end=1250
  _globals['_UPDATECANCELLATIONREFUNDWORKFLOWREQUEST']._serialized_start=1253
  _globals['_UPDATECANCELLATIONREFUNDWORKFLOWREQUEST']._serialized_end=1396
  _globals['_UPDATECANCELLATIONREFUNDWORKFLOWRESPONSE']._serialized_start=1398
  _globals['_UPDATECANCELLATIONREFUNDWORKFLOWRESPONSE']._serialized_end=1440
  _globals['_HANDLEORDERMAYBEREADYNOTIFICATIONREQUEST']._serialized_start=1443
  _globals['_HANDLEORDERMAYBEREADYNOTIFICATIONREQUEST']._serialized_end=1588
  _globals['_HANDLEORDERMAYBEREADYNOTIFICATIONRESPONSE']._serialized_start=1590
  _globals['_HANDLEORDERMAYBEREADYNOTIFICATIONRESPONSE']._serialized_end=1633
  _globals['_ORDERHEALTHMONITORTIMEBASEDEVENT']._serialized_start=1636
  _globals['_ORDERHEALTHMONITORTIMEBASEDEVENT']._serialized_end=1773
  _globals['_EXPECTEDLATEEVENT']._serialized_start=1776
  _globals['_EXPECTEDLATEEVENT']._serialized_end=1961
  _globals['_GETREALTIMEDISASTERTRACKERLATEDELIVERIESREQUEST']._serialized_start=1964
  _globals['_GETREALTIMEDISASTERTRACKERLATEDELIVERIESREQUEST']._serialized_end=2431
  _globals['_GETREALTIMEDISASTERTRACKERLATEDELIVERIESRESPONSE']._serialized_start=2434
  _globals['_GETREALTIMEDISASTERTRACKERLATEDELIVERIESRESPONSE']._serialized_end=4030
  _globals['_GETREALTIMEDISASTERTRACKERLATEDELIVERIESRESPONSE_DELIVERY']._serialized_start=2644
  _globals['_GETREALTIMEDISASTERTRACKERLATEDELIVERIESRESPONSE_DELIVERY']._serialized_end=3828
  _globals['_GETREALTIMEDISASTERTRACKERLATEDELIVERIESRESPONSE_CONSUMERTYPE']._serialized_start=3830
  _globals['_GETREALTIMEDISASTERTRACKERLATEDELIVERIESRESPONSE_CONSUMERTYPE']._serialized_end=3929
  _globals['_GETREALTIMEDISASTERTRACKERLATEDELIVERIESRESPONSE_DELIVERYTYPE']._serialized_start=3931
  _globals['_GETREALTIMEDISASTERTRACKERLATEDELIVERIESRESPONSE_DELIVERYTYPE']._serialized_end=4030
  _globals['_PICKUPORDERMAYBEREADYSEGMENTMESSAGE']._serialized_start=4033
  _globals['_PICKUPORDERMAYBEREADYSEGMENTMESSAGE']._serialized_end=4169
  _globals['_ORDERHEALTHMONITORSERVICE']._serialized_start=4763
  _globals['_ORDERHEALTHMONITORSERVICE']._serialized_end=6278
# @@protoc_insertion_point(module_scope)
