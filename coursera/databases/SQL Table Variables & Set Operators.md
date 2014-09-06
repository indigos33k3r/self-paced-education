#Introduction to Databases
_Lecture 13: Table variables and set operators_

###Table Variables
* Used in the 'from' clause
	* Original:
	
			select Student.sID, sName, GPA, Apply.cName, enrollment
			from Student, College, Apply
			where Student.sID = Apply.sID and Apply.cName = College.cName;
			
	* With Table Variables:
	
			select S.sID, sName, GPA, A.cName, enrollment
			from Student S, College C, Apply A
			where A.sID = S.sID and A.cName = C.cName;
			
			
* Getting all pairs students with the same GPA
	* Avoid duplicate pairs by using '<' or '>' to order GPA by high or low in each pair	 

			select S1.sID, S1.sName, S1.GPA, S2.sID, S2.sName, S2.GPA
			from Student S1, Student S2
			where S1.GPA = S2.GPA and S1.sID < S2.sID; 
			
###Set Operators

* Union
	* Eliminates duplicates:
	
			select cName as name from College 
			union
			select sName as name from Student
			order by name;
		
	* We can retain duplicates as follows:
	
			select cName as name from College 
			union all
			select sName as name from Student;
			
* Intersect
	* All students who applied to CS and EE:
	
			select sID from Apply where major = 'CS'
			intersect
			select sID from Apply where major = 'EE';
	
	* This doesn't always work, so here is an alternative:
	
			select distinct A1.sID
			from Apply A1, Apply A2
			where A1.sID = A2.sID and A1.major = 'CS' and A2.major = 'EE';
			
* Difference (Except)
	* Students who applied to CS and not EE:
	
			select sID from Apply where major = 'CS'
			except
			select sID from Apply where major = 'EE';
			
	* This doesn't always work, here's an alternative:
		 
			select distinct A1.sID
			from Apply A1, Apply A2
			where A1.sID = A2.sID and A1.major = 'CS' and A2.major <> 'EE';
			
	__OR SO WE THOUGHT! Impossible to replicate the above query without using 'except' for now.__
	