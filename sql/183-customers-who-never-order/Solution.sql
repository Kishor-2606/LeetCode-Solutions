select Customers.name as Customers from Customers
where Customers.id not in 
(
    select c.id
    from Customers as c
    join Orders as o
    on c.id=o.customerId
    
)