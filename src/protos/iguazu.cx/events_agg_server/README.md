# Aggregated Events

Aggregated events are computed, or derived, on top of raw events that occur in sequence or in relation to one another. For example, we combine a click event (interaction) with a navigation event (lifecycle) into a "click navigation" event, which captures a click that results in a page navigation.

**Contents**

- [Agg Event Types](#agg-event-types)
- [Development](#development)

---

## Agg Event Types

| Event | Description | Data Catalog |
| ----- | ----------- | ------------ |
| [`cx_click_action_agg_server`][cx-click-action-agg] | Aggregation of a [`cx_view_click`][cx-view-click] or [`cx_section_view_click`][cx-section-view-click] and the subsequent action event | [📄][cx-click-action-agg-dc] |
| [`cx_dead_click_agg_server`][cx-dead-click-agg] | Aggregation of a [`cx_view_click`][cx-view-click] or [`cx_section_view_click`][cx-section-view-click] where the click did not match to a subsequent action event | [📄][cx-dead-click-agg-dc] |
| [`cx_page_impression_agg_server`][cx-page-impression-agg] | Aggregation of [`cx_view`][cx-view] event and [`cx_action_page_load`][cx-action-page-load] error after page launch | [📄][cx-page-impression-agg-dc] |
| [`cx_repeat_click_agg_server`][cx-repeat-click-agg] | Aggregation of [`cx_view_click`][cx-view-click] or [`cx_section_view_click`][cx-section-view-click] events where the user repeated the same click 1+ times | [📄][cx-repeat-click-agg-dc] |
| [`cx_view_impression_agg_server`][cx-view-impression-agg] | Aggregation of [`cx_view`][cx-view] event that enforces [viewability][viewability] thresholds | [📄][cx-view-impression-agg-dc] |

## Development

TODO


[cx-action-page-load]: https://github.com/doordash/services-protobuf/protos/iguazu.cx/events/cx_action_page_load.proto
[cx-click-action-agg]: https://github.com/doordash/services-protobuf/protos/iguazu.cx/events_agg_server/cx_click_action_agg_server.proto
[cx-click-action-agg-dc]: https://datahub.doordash.team/dataset/urn:li:dataset:(urn:li:dataPlatform:snowflake,iguazu.consumer.cx_click_action_agg,PROD)/Schema
[cx-dead-click-agg]: https://github.com/doordash/services-protobuf/protos/iguazu.cx/events_agg_server/cx_dead_click_agg_server.proto
[cx-dead-click-agg-dc]: https://datahub.doordash.team/dataset/urn:li:dataset:(urn:li:dataPlatform:snowflake,iguazu.consumer.cx_dead_click_agg,PROD)/Schema
[cx-page-impression-agg]: https://github.com/doordash/services-protobuf/protos/iguazu.cx/events_agg_server/cx_page_impression_agg_server.proto
[cx-page-impression-agg-dc]: https://datahub.doordash.team/dataset/urn:li:dataset:(urn:li:dataPlatform:snowflake,iguazu.consumer.cx_page_impression_agg,PROD)/Schema
[cx-repeat-click-agg]: https://github.com/doordash/services-protobuf/protos/iguazu.cx/events_agg_server/cx_repeat_click_agg_server.proto
[cx-repeat-click-agg-dc]: https://datahub.doordash.team/dataset/urn:li:dataset:(urn:li:dataPlatform:snowflake,iguazu.consumer.cx_repeat_click_agg,PROD)/Schema
[cx-section-view-click]: https://github.com/doordash/services-protobuf/protos/iguazu.cx/events/cx_section_click.proto
[cx-view]: https://github.com/doordash/services-protobuf/protos/iguazu.cx/events/cx_view.proto
[cx-view-click]: https://github.com/doordash/services-protobuf/protos/iguazu.cx/events/cx_view_click.proto
[cx-view-impression-agg]: https://github.com/doordash/services-protobuf/protos/iguazu.cx/events_agg_server/cx_view_impression_agg_server.proto
[cx-view-impression-agg-dc]: https://datahub.doordash.team/dataset/urn:li:dataset:(urn:li:dataPlatform:snowflake,iguazu.consumer.cx_view_impression_agg,PROD)/Schema
[viewability]: https://github.com/doordash/services-protobuf/protos/iguazu.cx/docs/concepts.md#viewability

