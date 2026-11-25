# What to provide for the best analysis

| Input | What can be analyzed | Important limitation |
|---|---|---|
| Full source repository | Code structure, app logic, frontend, backend if included | Missing services remain unknown |
| APK | Manifest, package metadata, resources, some client code with suitable tools | Not the original complete source; no private server code |
| Backend repository | Routes, services, schema, auth, jobs, integrations | Production infrastructure may still be external |
| API documentation | Documented API contracts | Does not reveal hidden server implementation |
| Screenshots | Visual layout, typography, colors, visible components | Hidden states and behavior require walkthroughs |
| Screen recording/walkthrough | Observable navigation and interactions | Cannot prove internal implementation |
| Database migrations/schema | Data model and relationships | Production data should not be supplied |
| Authorized test environment | Observable API and app behavior | Stay within written scope; use synthetic accounts/data |

Never provide production secrets, real customer records, or credentials in reports.
