A delivery kafka event will be sent for every mutation of a delivery object.  The payload of the kafka event will contain data on exactly what fields changed as part of the mutation.
In addition to representing a mutation to a delivery, delivery kafka events may also contain some metadata about the delivery.  Consumers of the events can expect to receive a DeliveryEvent message for each delivery event.  See the DeliveryEvent protobuf for info the fields available.

The complete list of delivery events sent in production can be found here:
https://github.com/doordash/services-protobuf/blob/master/protos/state_change_events/delivery_state_change.proto#L171-L188

Delivery events are sent to the "delivery_lifecycle_events" kafka topic

Limitations and Guarantees:
1. We guarantee at-least-once publication (possibly more than once in rare instance) of delivery events
2. Messages are not guaranteed to be in order. The timestamp field of the delivery event can be used to determine true ordering when needed. 
