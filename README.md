# freestlye-libre-data
Give me my diabetes data

* User interface does not provide a means to get API token
* Use browser developer tools to look for `Bearer` token upon authorisation request to `api-eu.libreview.io`
* Set this token as environment variable `LIBREVIEW_API_TOKEN`
	* I used [gnu pass](https://www.passwordstore.org/)

## TODO
* Currently, just settings and downloaded, not glucose readings:
	- [ ] figure out how to form correct URLS to get glucose readings
