#!/usr/bin/node

// script that display the status code of a GET request.

const axios = require('axios');

axios.get(process.argv[2])
  .then(resp => {
    console.log(`code: ${resp.status}`);
  })
  .catch(error => {
    console.log(`code: ${error.resp.status}`);
  });
