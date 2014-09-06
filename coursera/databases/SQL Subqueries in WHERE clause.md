#Introduction to Databases
_Lecture 14: Subqueries in WHERE Clause_

###Subqueries
Nested select statements within the WHERE clause

* Find all students who have applied as CS majors
	
		select sID, sName
		from Student
		where sID in (select sID from Apply where major = 'CS');
		
	* Without a subquery:

			select distinct Student.sID, sName
			from Student, Apply
			where Student.sID = Apply.sID and major = 'CS';
		
		
__Duplicates matter!__

* Get GPA of students applying to be a CS major

		select GPA
		from Student
		where sID in (select sID from Apply where major = 'CS')
		
		
	* Without subquery (duplicates everywhere)
	
			select GPA
			from Student, Apply
			where Student.sID = Apply.sID and major = 'CS'
			
			
		This is unfixable! Need subqueries.
		

* Get students applying for CS and NOT EE

		select sID, sName
		from Student
		where sID in (select sID from Apply where major = 'CS')
			and sID not in (select sID from Apply where major = 'EE');
			
	We couldn't do this before! Now we can.
	

* Applying exists operator to subquery
	* Query: colleges that have other colleges in the same state
	
			select cName, state
			from College C1
			where exists (select * from College C2 where C2.state = C1.state and C1.cName <> C2.cName);	 
			

* Getting largest value
	* College with highest enrollment
	
			select cName
			from College C1
			where not exists (select * from College C2 where C2.enrollment > C1.enrollment);
			
			
	* Student with highest GPA
	
			select sName, GPA
			from Student
			where GPA >= all (select GPA from Student);
			
	* Students not from smallest high school
	
			select sID, sName, sizeHS
			from Student
			where sizeHS > any (select sizeHS from Student);
			
	Note: not all systems support 'any' and 'all'
			
			
