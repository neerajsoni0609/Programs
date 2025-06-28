select 
	emp.name,
    mgr.name
from emp_mgr as emp
inner join emp_mgr as mgr
on emp.manager_id = mgr.id;

-- This program was asked in Cybage Interview