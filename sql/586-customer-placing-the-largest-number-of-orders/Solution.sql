select customer_number from(
    select customer_number,count(order_number) as cnt 
    from orders
    group by customer_number
    order by cnt desc
    limit 1
) as c