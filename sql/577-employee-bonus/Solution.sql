select e.name,b.bonus
from Employee as e
left join Bonus as b
on b.empId=e.empId
having (b.bonus<1000 or b.bonus is null)