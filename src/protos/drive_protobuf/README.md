## [Protobuf Naming Convention](https://cloud.google.com/apis/design/naming_convention)


- **Method names:**
Naming Convention
```markdown
Verb   | Noun | Method name | Request message   | Response message
---    | --   | --          | --                | --
List   | Book | ListBooks   | ListBooksRequest  | ListBooksResponse
Get    | Book | GetBook     | GetBookRequest    | Book
Create | Book | CreateBook  | CreateBookRequest | Book
Update | Book | UpdateBook  | UpdateBookRequest | Book
Rename | Book | RenameBook  | RenameBookRequest | RenameBookResponse
Delete | Book | DeleteBook  | DeleteBookRequest | google.protobuf.Empty
```
Example
```proto
service CalendarApi {
  rpc ListEvents(ListEventsRequest) returns (ListEventsResponse);
}
message ListEventsRequest {
  string parent = 1;
  int32 page_size = 2;
  string page_token = 3;
}
message ListEventsResponse {
  repeated Event events = 1;
  string next_page_token = 2;
}
```

- **Package names:**
Package names declared in the API .proto files should be consistent with Product and Service Names. Package names for APIs that have a version must end with the version. For example:
```markdown
// Google Calendar API
package google.calendar.v3;
```


Java package names specified in the API .proto files must match the proto package names with standard Java package name prefix (com., edu., net., etc). For example:
```markdown
package google.calendar.v3;
// Specifies Java package name, using the standard prefix "com."
option java_package = "com.google.calendar.v3";
```

- **Enum names:**
Enum types must use UpperCamelCase names.Enum values must use CAPITALIZED_NAMES_WITH_UNDERSCORES. Each enum value must end with a semicolon, not a comma. The first value should be named ENUM_TYPE_UNSPECIFIED as it is returned when an enum value is not explicitly specified.
```
enum FooBar {
  // The first value represents the default and must be == 0.
  FOO_BAR_UNSPECIFIED = 0;
  FIRST_VALUE = 1;
  SECOND_VALUE = 2;
}
```