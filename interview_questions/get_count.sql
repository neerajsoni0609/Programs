select
	distinct(name),
    count(name)
from employee_new
group by name;