# XSS Playground

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

Getting the server started

- [https://medium.com/@onejohi/building-a-simple-rest-api-with-nodejs-and-express-da6273ed7ca9](https://medium.com/@onejohi/building-a-simple-rest-api-with-nodejs-and-express-da6273ed7ca9)