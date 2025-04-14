# Sample Queries

Sample queries for unified telemetry events.

**Contents**

- [Core Funnel](#core-funnel)


## Funnels

<details><summary>Core Cx Funnel</summary>

*Store Page Load*
Event: `cx_action_page_load`
```sql
SELECT *
FROM iguazu.consumer.cx_action_page_load
WHERE app_context:current_page IN ('store_page', 'nv_store_page')
  AND app_context:store:store_id IN ('<store_id>')
```

*Add to Cart*
Event: `cx_action_order_cart`
```sql
SELECT *
FROM iguazu.consumer.cx_action_order_cart
WHERE action_type = 'add'
  AND app_context:store:store_id IN ('<store_id>')
```

*Order Cart Page Load*
Event: `cx_action_page_load`
```sql
SELECT *
FROM iguazu.consumer.cx_action_page_load
WHERE app_context:current_page = 'order_cart_page'
  AND app_context:store:store_id IN ('<store_id>')
```

*Checkout Page Load*
Event: `cx_action_page_load`
```sql
SELECT *
FROM iguazu.consumer.cx_action_page_load
WHERE app_context:current_page = 'checkout_page'
  AND app_context:order_cart:store:store_id IN ('<store_id>')
```

*Checkout Success*
Event: `cx_remote_action_payment_status`
```sql
SELECT *
FROM iguazu.consumer.cx_remote_action_payment_status
WHERE action_type = 'checkout'
  AND status_type = 'success'
  AND app_context:order_cart:store:store_id IN ('<store_id>')
```

*Checkout Error*
Event: `cx_remote_action_payment_status`
```sql
SELECT *
FROM iguazu.consumer.cx_remote_action_payment_status
WHERE action_type = 'checkout'
  AND status_type = 'failure'
  AND app_context:order_cart:store:store_id IN ('<store_id>')
```
</details>

