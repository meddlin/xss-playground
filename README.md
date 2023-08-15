# XSS Playground

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This is a contrived and purposely vulnerable web application made to play with XSS vulnerabilities and exploits.

## Getting Started

```bash
cd xss-playground && npm install
```

## Working with Payloads

1. Start the server
2. Navigate to page: `http://localhost:3000`
3. Throw stuff at it

### working payloads

Reference: [https://github.com/payloadbox/xss-payload-list](https://github.com/payloadbox/xss-payload-list)

```html
<image/src/onerror=prompt(8)>
```


## Notes

**Getting the server started**

This was used to build the server and create a basic REST endpoint.

- [https://medium.com/@onejohi/building-a-simple-rest-api-with-nodejs-and-express-da6273ed7ca9](https://medium.com/@onejohi/building-a-simple-rest-api-with-nodejs-and-express-da6273ed7ca9)

**Serving static files from express**

This was used to host the webpage from express. It's not necessary to use the `index.html` file, but 
most XSS tools want to point at a URL. So, that's why this was necessary to make the exercise work.

- [https://stackoverflow.com/questions/10434001/static-files-with-express-js](https://stackoverflow.com/questions/10434001/static-files-with-express-js)
