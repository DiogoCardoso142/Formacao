const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send(`
    <h1>This is a simple Node Express App</h1>
  `);
})

app.listen(3000);
