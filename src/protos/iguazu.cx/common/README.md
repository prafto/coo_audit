# Entities

A key business object such as an Item, Store, or Cart, or a business concept with a unique data model such as Filters, Banners, or Campaigns. Entities have individual properties, for example a Store has an id, name, and vertical. Entities can have state changes based on the actions that users perform when interacting with the app such as adding items to Cart. All references to these entities in our schemas need to be identical without exception.

**Contents**

- [Entity Types](#entity-types)
- [Development](#development)

---

## Entity Types

Entities come in different shapes and sizes. Common categories of entities include:

### Business Entity

A singular entity such as Item, Store, Business, Campaign, Cuisine, or Collection. Business entities typically correspond to objects stored in other dbs.

### Group Entity

A group, or collection, of multiple entities such as `CxAppContext` or `CxEntity`. Group entities are a useful way to group several related entities into one place.

### Data Entity

An entity that stores information related to a data object that does not represent a physical business object such as `Category_l1` or `Category_l2`.

### App Entity

Any other entity related to the app that can be linked to user actions such as Autocomplete, Search, Selected Filters or Selected Sorts.

### App Context Entity

A meta entity that stores *shared* context about the state app or other entity types, for example [`CxAppContext`][cx-app-context].

| Name | Type | Description | Emitted By |
|------|------|-------------|------------|
| item | `Item` | The Item being clicked or viewed | [`CxView`][cx-view], [`CxViewClick`][cx-view-click] |
| campaign | `Campaign`] | The Item being clicked or viewed | [`CxView`][cx-view], [`CxViewClick`][cx-view-click] |
| category_l1 | `CategoryL1` | The CategoryL1 being clicked or viewed | [`CxView`][cx-view], [`CxViewClick`][cx-view-click] |
| store | `Store` | The Store being clicked or viewed | [`CxView`][cx-view], [`CxViewClick`][cx-view-click] |
| filter | `Filter` | The Filter being clicked or viewed | [`CxView`][cx-view], [`CxViewClick`][cx-view-click]|
| vertical | `Vertical` | The Vertical being clicked or viewed | [`CxView`][cx-view], [`CxViewClick`][cx-view-click]|
| map_area | `MapArea` | The MapArea in a map gesture | CxMapGesture |
| tab | `Tab` | The Tab being clicked or viewed | [`CxView`][cx-view], [`CxViewClick`][cx-view-click] |
| fulfillment_option | [`FulfillmentOption`][cx-fulfillment-option] | The FulfillmentOption being clicked or viewed | [`CxView`][cx-view], [`CxViewClick`][cx-view-click] |
| delivery_option | `DeliveryOption` | The DeliveryOption being clicked or viewed | [`CxView`][cx-view], [`CxViewClick`][cx-view-click] |
| price_line_item | `PriceLineItem` | The PriceLineItem being clicked or viewed | [`CxView`][cx-view], [`CxViewClick`][cx-view-click] |

## Development

### Updating entities

To update an entity, simply add a new field to the entity `.proto` file.

> [!IMPORTANT]
> Never change the numeric identifiers of fields once they are in use.

If you need to deprecate an entity field, add the `deprecated` option to the field.

```protobuf
message CxStore {
  google.protobuf.StringValue store_id = 1;
  google.protobuf.StringValue store_name = 2;
  google.protobuf.Int32Value store_position = 3;
  google.protobuf.StringValue store_cuisine = 4 [deprecated = true];
}
```

### Adding entities

A new entity should be defined whenever there is a new data object that is currently not represented by an existing `entity` in this repository. To define a new entity, create a new `.proto` file with the entity name and prefix `cx_`. The file name should correspond to the entity name (eg. `cx_store` containts `message CxStore`).

> [!NOTE]
> You should always attempt to extend an exisiting entity by adding new fields to the entity when two entities are quite similar or overlapping. When in doubt, refer to how the corresponding data objects are modeled in the db.


[cx-app-context]: https://github.com/doordash/services-protobuf/protos/iguazu.cx/common/cx_app_context.proto
[cx-view]: https://github.com/doordash/services-protobuf/protos/iguazu.cx/events/cx_view.proto
[cx-view-click]: https://github.com/doordash/services-protobuf/protos/iguazu.cx/events/cx_view_click.proto
