# Enums

A data type in Protobuf that represents a group of constants. The primary goal of telemetry standardization is to ensure data consistency and integrety across our clients. Enums are critical for ensuring the generated payload is correct for fields with defined constants.

According to the Iguazu [codelab][codelab], enums, while commonly used in Protobuf, are not recommended for the Iguazu system today. However, we choose to define `enums` for forwards compatibility and data validation purposes.

**Contents**

- [Development](#development)
- [Images](#images)

---

## Development

### Updating enums

To update an enum, simply add a new value to the enum `.proto` file. For each enum value, a corresponding text value must be defined.


```protobuf
enum CxPageType {
  UNSPECIFIED = 0;
  NONE = 1;
  CART_PAGE = 2 [iguazu.cx.metadata.v1.value = "cart_page"];
}
```


If you need to deprecate an enum value, add the `deprecated` option to the enum value.

```protobuf
enum CxPageType {
  UNSPECIFIED = 0;
  NONE = 1;
  CART_PAGE = 2 [deprecated = true];
}
```

### Adding enums

To define a new `enum`, create a new `.proto` file with the enum name and prefix `cx_`. The file name should correspond to the enum name (eg. `cx_page_type` containts `enum CxPageType`). Each file should contain a single enum.

> [!IMPORTANT]
> When creating a new enum, the field name must correspond to the enum name without the  `cx_` prefix (eg. field `page_type` corresponds to `enum CxPageType`). These assumptions are used during validation to check that the field values is a valid enum value.


[codelab]: https://devconsole.doordash.team/codelabs/iguazu+proxy+client+onboarding%2ftutorial?step=4
[cx-enum]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/enums/cx_enum.proto
[cx-page-type]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/enums/cx_page_type.proto
[cx-view-type]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/enums/cx_view_type.proto
[cx-section-type]: https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/enums/cx_section_type.proto
[ui-element]:https://github.com/doordash/services-protobuf/tree/master/protos/iguazu.cx/docs/concepts.md#ui-element
