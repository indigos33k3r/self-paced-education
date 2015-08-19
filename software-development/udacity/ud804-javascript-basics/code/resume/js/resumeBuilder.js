/*global $*/

//My info

var bio = {
    name: "John Doe",
    role: "Web Developer",
    welcomeMessage: "Welcome to my project!",
    contacts: {
        mobile: "111-111-1111",
        email: "me@example.com",
        github: "johndoe",
        twitter: "@johndoe",
        location: "Earth"
    },
    skills: [
        "Programming",
        "Eating",
        "Sleeping"
    ]
};

var projects = {
    projects: [
        {
            title: "Personal Website",
            dates: "2012 - 2014",
            description: "Foo bar baz",
            images: [
                "http://placehold.it/100x100/e33",
                "http://placehold.it/100x100/000"
            ]
        },
        {
            title: "Linux Kernel",
            dates: "1991 - Present",
            description: "It's kind of a big deal.",
            images: [
                "http://placehold.it/100x100/0f0",
                "http://placehold.it/100x100/ff4"
            ]
        }
    ]
};

var work = {
    jobs: [
        {
            employer: "Google",
            title: "CEO",
            location: "Mars",
            dates: "2004 - 2008",
            description: "I'm the best."
        },
        {
            employer: "MongoDB",
            title: "Janitor",
            location: "New York",
            dates: "2008 - 2012",
            description: "I'm not the best."
        }
    ]
};

var education = {
    schools: [
        {
            name: "University of Hello",
            location: "BlahBlah",
            degree: "B.S.",
            dates: "2014 - 0000",
            majors: [
                "Computer Science",
                "Pumpkins"
            ]
        }
    ],
    onlineCoruses: [
        {
            title: "JavaScript Basics",
            school: "Udacity",
            dates: "2014",
            url: "http://udacity.com/course/ud804"
        }
    ]
};

var c = "%contact%";
var d = "%data%";

//I like to use the $ at the start of any jQuery object for my own reference
var $main = $("#main");
var $header = $('#header');
var $contact = $('#topContacts');
var $work = $('#workExperience');
var $projects = $('#projects');
var $education = $('#education');
var $skills = $('#skillsChart');
var $map = $('mapDiv');

//add bio pic

var bioPicURL = 'images/fry.jpg';
var formattedBioPic = HTMLbioPic.replace(d, bioPicURL);

//add name and job

var formattedName = HTMLheaderName.replace(d, bio.name);
var formattedRole = HTMLheaderRole.replace(d, bio.role);
$header.append(formattedName);
$header.append(formattedRole);
$main.prepend(formattedBioPic);

//add contact info

for (var i in bio.contacts) {
    var formattedContactInfoItem = HTMLcontactGeneric.replace(d, bio.contacts[i]);
    formattedContactInfoItem = formattedContactInfoItem.replace(c, i);
    $contact.append(formattedContactInfoItem);
}

//add work experience

for (var j in work.jobs) {
    var $workDiv = $(HTMLworkStart);
    
    var formattedWorkTitle = HTMLworkTitle.replace(d, work.jobs[j].title);
    var formattedWorkEmployer = HTMLworkEmployer.replace(d, work.jobs[j].employer);
    var formattedWorkDates = HTMLworkDates.replace(d, work.jobs[j].dates);
    var formattedWorkLocation = HTMLworkLocation.replace(d, work.jobs[j].location);
    var formattedWorkDescription = HTMLworkDescription.replace(d, work.jobs[j].description);
    
    $workDiv.append(formattedWorkEmployer);
    $workDiv.append(formattedWorkTitle);
    $workDiv.append(formattedWorkDates);
    $workDiv.append(formattedWorkLocation);
    $workDiv.append(formattedWorkDescription);
    
    $work.append($workDiv);
}

//add projects

for (var p in projects.projects) {
    var $projectDiv = $(HTMLprojectStart);
    
    var formattedProjectTitle = HTMLprojectTitle.replace(d, projects.projects[p].title);
    var formattedProjectDates = HTMLprojectDates.replace(d, projects.projects[p].dates);
    var formattedProjectDescription = HTMLprojectDescription.replace(d, projects.projects[p].description);
    
    $projectDiv.append(formattedProjectTitle);
    $projectDiv.append(formattedProjectDates);
    $projectDiv.append(formattedProjectDescription);
    
    //images
    for (var img in projects.projects[p].images) {
        var formattedProjectImage = HTMLprojectImage.replace(d, projects.projects[p].images[img]);
        $projectDiv.append(formattedProjectImage);
    }
    
    $projects.append($projectDiv);
}

//add education
var HTMLonlineStart = "<div class='education-entry'></div>"

for (var s in education.schools) {
    var $schoolDiv = $(HTMLschoolStart);
    
    var formattedSchoolName = HTMLschoolName.replace(d, education.schools[s].name);
    var formattedSchoolDegree = HTMLschoolDegree.replace(d, education.schools[s].degree);
    var formattedSchoolDates = HTMLschoolDates.replace(d, education.schools[s].dates);
    var formattedSchoolLocation = HTMLschoolLocation.replace(d, education.schools[s].location);
    
    $schoolDiv.append(formattedSchoolName);
    $schoolDiv.append(formattedSchoolDegree);
    $schoolDiv.append(formattedSchoolDates);
    $schoolDiv.append(formattedSchoolLocation);
    
    for (var m in education.schools[s].majors) { 
        var formattedSchoolMajor = HTMLschoolMajor.replace(d, education.schools[s].majors[m]);
        $schoolDiv.append(formattedSchoolMajor);
    }
    
    $education.append($schoolDiv);
}

$education.append(HTMLonlineClasses);

for (var s in education.onlineCoruses) {
    var $onlineEduDiv = $(HTMLonlineStart);
    
    var formattedOnlineSchool = HTMLonlineSchool.replace(d, education.onlineCoruses[s].school);
    var formattedOnlineURL = HTMLonlineURL.replace(d, education.onlineCoruses[s].url);
    var formattedOnlineTitle = HTMLonlineTitle.replace(d, education.onlineCoruses[s].title);
    var formattedOnlineDates = HTMLonlineDates.replace(d, education.onlineCoruses[s].dates);

    $onlineEduDiv.append(formattedOnlineTitle);
    $onlineEduDiv.append(formattedOnlineSchool);
    $onlineEduDiv.append(formattedOnlineDates);
    $onlineEduDiv.append(formattedOnlineURL);
    
    $education.append($onlineEduDiv);
}

//add skills

for (var s in bio.skills) {
    var $skillDiv = $(HTMLskillsStart);
    var formattedSkill = HTMLskills.replace(d, bio.skills[s]);
    $skillDiv.append(formattedSkill);
    
    $skills.append($skillDiv);
}