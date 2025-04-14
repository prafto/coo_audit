[![slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)][slack][![jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=Jira&logoColor=white)][jira]

# Cx Unified Telemetry

`iguazu.cx` is the protobuf repository for `UnitifedTelemetry` for Cx, designed to define and organize all schemas releated to the consumer journey and experience across mobile and web clients.

**Contents**

- [Implementations](#implementations)
- [Coverage](#coverage)
- [File Organization](#file-structure)
- [Protobuf Schemas](#protobuf-schemas)
- [Development](#development)
- [Documentation](#documentation)

---

## Implementations

Platform implementations of `UnitifedTelemetry` can be found in their own repositories:

- Android: [`unifiedmonitoring`][android]
- iOS: [`UnifiedTelemetry`][ios]
- Web: [`unified-telemetry`][web]

## File Structure

Proto files are organized to manage dependencies and prevent circular dependencies. When defining a proto schema, there should be a single message per file ([1-1-1 Rule][1-1-1-rule]).

| 📁 | Purpose |
|----|---------|
| [`/common`][entity] | all [entities][entity-concept] |
| [`/events`][event] | all [raw events][event-concept] |
| [`/events_agg_server`][server-agg-event] | all backend [aggregated events][server-agg-event-concept] are implemented by the realtime team |
| [`/events_agg_app`][client-agg-event] | all client side [aggregated events][client-agg-event-concept] that are done app side |

```
📁iguazu.cx/
├── 📁common/
│   └── 📝 cx_page_type.proto
│   └── 📝 cx_app_context.proto
├── events/
│   ├── 📝 cx_page_launch.proto
│   └── 📝 cx_view.proto
│   └── 📝 cx_view_click.proto
└──  📄 placeholder.proto
```

### File Conventions

The file name must correspond to the Event or Entityname defined in the file (eg. `cx_page_launch.proto` containts `message CxPageLaunch`). Files should contain a single Event or Entity.

## Protobuf Schemas

The following are general schema design principles that apply to all protos in the project. Head over to the [`events`][event-schema] repository for event schema design principles. Also see refer to general [best-practices][best-practices] for protobuf.

### Best Practices

1. Avoid representing objects as strings. Instead, define a new [Entity][entity]. While non-standard, historically this was a common practice  in segment and iguazu as some downstream teams were not familiar with nested field types.
2. Avoid [breaking changes][breaking-changes]. Breaking changes can result in data loss due to deserialization errors. If you need to make breaking change, please notify downstream teams ahead of time.

**Bad**
```json
{
  "value_keys": [
    "id1:value1:range1",
    "id2:value2:range2"
  ]
}
```
**Good**
```json
{
  "selected_filters": [
    // filter 1
    {
      "filter_id": "id1",
      "filter_values": [
        "value1",
        "value2",
        "value3,"
      ],
      "filter_range": "range1"
    },
    // filter 2
    {
      "filter_id": "id2",
      "filter_values": [
        "value2",
        "value5",
        "value6,"
      ],
      "filter_range": "range2"
    }
  ]
}

```

### Fields

* Never change the numeric identifiers of fields once they are in use.
* Use the `[deprecated=true]` option for fields that are no longer in use.
* Use `string` type fields sparingly, considering memory implications.

### Reserved Words

* Do not use Iguazu reserved words such as `context`, `value`, and `envelope` in names.
* Do not use Protobuf [reserved words][reserved-words] such as `reserved`, `max`, `optional`, etc in names.
* Avoid using common [keywords][sql-keywords] in another languages (eg. SQL) such as `date`, `row`, `acceptable`, `true`, `values`, etc.

If you have to use keyword, consider using a prefix such as `cx_`.

### Data Types

Select the right optional vs non-optional designation

| Type | Optional  | Non-Optional | 
| ---- | --------- | ------------ |
| `String` | `StringValue` | `string` |
| `Int32` | `Int32Value` | `int32` |
| `Float` | `FloatValue` | `float` | 

Select the most appropriate type for each field based on the data it will store.

| Field | Bad | Good |
| ----- | --- | ---- |
| `num_star_rating` | `StringValue` | `Int32Value` |
| `star_rating` | `DoubleValue` | `FloatValue` |
| `num_star_rating` | `StringValue` | `Int32Value` |
| `minimum_subtotal_amount` | `StringValue` | `Int32Value` |
| `price_range` | `StringValue` | `FloatValue` |
| `pickup_available` | `StringValue` | `Boolean` |
| `shows_dashpass_badging` | `StringValue` | `Boolean` |

> [!WARNING]
> Choosing the wrong data type can result in **type conversion loss** in Iguazu.
>
> - `String` raw data type can be ingested into other types
> - `Float` (string or float) => IntValue will result in data loss
> - `Timestamp` type must be string

| Raw Data | Raw Data Type | Proto | Eventual |
| -------- | ------------- | ----- | -------- |
| 100 | int (expected) | `Int32Value` | 100 |
| "100" | string | `Int32Value` | 100 |
| "100.0" | string | `Int32Value` | 100 |
| "100.1" | string | `Int32Value` | **data loss** |
| 100.0 | float | `Int32Value` | 100 |
| 100.1 | float | `Int32Value` | **data loss** |
| 42.4 | float (expected) | `FloatValue` | 42.4 |
| 42.444444444444 | double | `FloatValue` | 42.444443 |
| "42.4" | string | `FloatValue` | 42.4 |
| "42.44444444444" | string | `FloatValue` | 42.444443 |
|  | int64 | Int64Value |  |
|  | double | Int64Value | **data loss** |
| {"seconds": 123, "nanos": 0} | timestamp | Timestamp | **data loss** |
| "2024-05-24T00:22:07Z" | string | Timestamp | 2024-05-24T00:22:07Z |

### Constants

#### Integers

| Constant| Definition | Example |
| --------| ---------- | ------- |
| -1 | Invalid value for position (aka index), and unitAmount</br> Context: position is a required parameter that should only be missing due to coverage issues.</br>Initially a P1 validation alert should be triggered, later P0. | `cx_view_click event`:</br> - view_type="card.store_item"</br> - entity_type = "item"</br> - event_context.item.item_position = -1</br></br>`entity.item`:</br> - actual_price = -1 (where we don’t know the unit amount) |
| 0 | Position when shown by itself, e.g. `item_position` on an item page | `item_position` in the `item` entity |

#### Identifiers (IDs)

| Constant| Definition | Example |
| --------| ---------- | ------- |
| "" | A constant to indicate no Id | When `entity_type` is `none`, entity_id is `""` |

## Schema Validation

TODO

## Development

1. **Update Service-Protobuf**

When adding new fields to a `.proto` file, bump the `release.json` version in `iguazu.cx` ([example][release])

2. **Run precommit checks**

When adding new files, run the precommit [hooks][precommit] for `iguazu.cx`.

```shell
pre-commit run --all-files
```

3. **Create pull request**

Create a pull request using the template for this repository.

```http
https://github.com/doordash/services-protobuf/compare/main...my-branch?quick_pull=1&template=iguazu.cx_template.md
```

4. **Upgrade Iguazu Pipelines**

Go to the [data portal][data-portal] and search for the event name.

Click the three dots menu on the left side and select "update schema" to perform the upgrade.

![update schema](https://drive.google.com/file/d/1notAfYCYO-kyBSb9_pTC8chAK0saq6Fg/view?usp=sharing)

> [!IMPORTANT]
> When a nested field is updated, for example `CxAppContext`, **all events** which use that field need to be updated from the portal.

## Documentation

`UnifiedTelemetry` provides a robust framework for defining and validating Protobuf messages by enforcing common standards. For a detailed overview, please refer to our [documentation][docs]. The key components include:

- [**Key Concepts**][concepts]: `UnitifedTelemetry` key concepts for modeling telemetry events.

- [**Migration**][migration]: Information, and tooling, for migrating to `UnitifedTelemetry`.


[1-1-1-rule]: https://protobuf.dev/programming-guides/1-1-1/
[android]: https://github.com/doordash/doordash-consumer-android/tree/master/libs/unifiedmonitoring
[best-practices]: https://protobuf.dev/programming-guides/dos-donts/
[breaking-changes]: https://doordash.atlassian.net/wiki/spaces/Eng/pages/3433791707/Services+Protobuf+Oncall+Runbook
[client-agg-event]:https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/events_agg_app/
[client-agg-event-concept]:https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/docs/concepts.md#aggregated-event
[concepts]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/docs/useage/concepts.md
[data-portal]: https://admin-gateway.doordash.com/data-portal/real-time/iguazu-event/pipelines
[docs]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/docs/
[entity]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/common/
[entity-concept]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/concepts.md#entity
[event]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/events/
[event-concept]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/docs/concepts.md#raw-event
[event-schema]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/events/README.md#schema-design
[ios]: https://github.com/doordash/doordash-consumer-ios/tree/develop/Layers/DomainInterfaces/Telemetry/Sources/UnifiedTelemetry
[jira]: https://doordash.atlassian.net/jira/software/c/projects/MCPLT/boards/5833
[migration]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/docs/migration.md
[precommit]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/hooks/README.md
[release]: https://github.com/doordash/services-protobuf/pull/37216/files
[reserved-words]: https://protobuf.dev/programming-guides/dos-donts/#well-known-common
[server-agg-event]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/events_agg_server/
[server-agg-event-concept]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/docs/concepts.md#aggregated-event
[slack]: https://doordash.slack.com/app_redirect?channel=ask-unified-telemetry
[sql-keywords]: https://docs.snowflake.com/en/sql-reference/reserved-keywords
[web]: https://github.com/doordash/web-next/tree/master/services/consumer-web-next/src/Common/unified-telemetry
[well-known-types]: https://protobuf.dev/reference/protobuf/google.protobuf/
