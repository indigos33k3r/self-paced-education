#Introduction to Databases
_Lecture 12: SELECT statement_

(Demo will use simple college admissions database)

###SELECT
Examples: 

__1.__

	select sID, sName, GPA
	from Student
	where GPA > 3.6;
	
__2.__
	
	select distinct sName, major
	from Student, Apply
	where Student.sID = Apply.sID;
	
We can concatenate conditions using 'and':
	
__3.__
	
	select sName, GPA, decision
	from Student, Apply
	where Student.sID = Apply.sID
		and sizeHS < 1000 and major = 'CS';
		
Note that there is ambiguity in simply saying 'select cName', so we must be specific:

__4.__
		
	select College.cName
	from College, Apply
	where College.cName = Apply.cName
		and enrollment > 20000 and major = 'CS';
__5.__
	
	select Student.sID, sName, GPA, Apply.cName, enrollment
	from Student, College, Apply
	where Apply.sID = Student.sID and Apply.cName = College.cName;
	
SQL is by default, unordered. We can sort however:

__6.__

	select Student.sID, sName, GPA, Apply.cName, enrollment
	from Student, College, Apply
	where Apply.sID = Student.sID and Apply.cName = College.cName
	order by GPA desc;
	
Use of the 'like' command for string-matching:

__7.__

	select sID, major
	from Apply
	where major like '%bio%';
	
Use of select * to get all attributes from expression

	select *
	from Student, College;
	
Using basic arithmetic within a clause to scale GPAs:

__8.__

	select sID, sName, GPA, sizeHS, GPA*(sizeHS/1000) as scaledGPA
	from Student;