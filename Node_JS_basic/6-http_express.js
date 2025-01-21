// 6-http_express.js

const express = require('express');

// Créer une instance d'Express
const app = express();

// Définir la route pour l'endpoint "/"
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Faire écouter le serveur sur le port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Exporter l'application
module.exports = app;
