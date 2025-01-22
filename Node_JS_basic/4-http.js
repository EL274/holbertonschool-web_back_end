// 4-http.js

const http = require('http');

// Créer le serveur HTTP
const app = http.createServer((req, res) => {
  // Définir le code de statut et l'en-tête de la réponse
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  // Envoyer la réponse
  res.end('Hello Holberton School!');
});

// Faire écouter le serveur sur le port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Exporter le serveur
module.exports = app;
