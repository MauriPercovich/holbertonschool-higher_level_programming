#!/usr/bin/node

// write

const fs = require('fs');

fs.writeFileSync(process.argv[2], process.argv[3]);
