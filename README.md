# Courses

Aggregates course data from education providers into a simple API.

---

A group of friends and I used to use a spreadsheet to aggregate and share free
online courses with each other in the early days of college; I decided to turn
that spreadsheet into a public API for getting information about those courses.

### Creating an Account

To create an account, simply visit 

### Authentication & Usage

The API is accessed over HTTPS, and authentication is handled via API keys.

To get an API key, 

```txt
GET https://selfpaced.education/api/v1/search?q=calculus&subject=03495348
```

### Objects

**Provider**

A provider is the institution teaching a course.

| Key  | Type   |
| ---- | ------ |
| id   | int    |
| name | string |
| url  | string |

**Course**

A course object provides metadata that describes an online class.

| Key         | Type           |
| ----------- | -------------- |
| id          | int            |
| name        | string         |
| description | string         |
| instructor  | string         |
| source      | string         |
| url         | string         |
| subject     | array[Subject] |
| tags        | array[Tag]     |

**Subject**

The subject is the general category of a course.

| Key         | Type           |
| ----------- | -------------- |
| id          | int            |
| name        | string         |
| tags        | array[Tag]     |

**Tag**

Tags are used to give additional information about the topics a course covers.

| Key  | Type   |
| ---- | ------ |
| id   | int    |
| name | string |

### Methods

The base URL is https://selfpaced.education. All methods are called via a GET
request.

*****Search forja course**

`GET /api/v1/search`

Search for courses that match your query. Can provide both a search
term as well as the names of providers, subjects, and tags for further qualification.

Query Parameters

| Key      | Type          |
| -------- | ------------- |
| q        | string        |
| provider | string        |
| subject  | string        |
| tags     | array[string] |

Returns an array of `Course` objects.

**List all courses**

`GET /api/v1/courses`

List all course information, and optionally takes parameters for the subject,
provider, and tags.

Query Parameters

| Key      | Type          |
| -------- | ------------- |
| provider | string        |
| subject  | string        |
| tags     | array[string] |

Returns an array of `Course` objects.

**Show course info**

`GET /api/v1/courses/:id`

Get metadata for a specific course.

Returns a `Course` object.

**List all providers**

`GET /api/v1/providers`

List all provider information.

Returns an array of `Provider` objects.

**Show provider info**

`GET /api/v1/providers/:id`

Get metadata for a specific provider.

Returns a `Provider` object.

**List all subjects**

`GET /api/v1/subjects`

List all subject information.

Returns an array of `Subject` objects.

**Show subject info**

`GET /api/v1/subjects/:id`

Get metadata for a specific subject.

Returns a `Subject` object.

**List all tags**

`GET /api/v1/tags`

List all tag information.

Returns an array of `Tag` objects.

**Show tag info**

`GET /api/v1/tags/:id`

Get metadata for a specific tag.

Returns a `Tag` object.

### Sources

Here is the current list of education providers the course data is sourced from:

* [Coursera](https://building.coursera.org/app-platform/catalog/)
* [edX](http://edx.readthedocs.io/projects/edx-platform-api/en/latest/courses/overview.html)
* [Khan Academy](http://api-explorer.khanacademy.org)
* [Open Courseware](http://data.oeconsortium.org)
* [Udacity](https://www.udacity.com/catalog-api)
* [YouTube](https://developers.google.com/youtube/v3/)

### Contributing

I recommend [filing a bug](https://github.com/tylucaskelley/courses/issues/new) if you:

* Find an issue with the API
* Want to add another education provider's set of courses
* Would like to request a feature

If you'd like to contribute, please see this document. I appreciate all pull
requests!

### Credits

To [@lawrencewilmore](https://github.com/lawrencewilmore), thank you for creating
the original spreadsheet of free courses.
