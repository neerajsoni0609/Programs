select
	distinct(name),
    count(name)
from employee_new
group by name;

-- This program was asked in Cybage Interview