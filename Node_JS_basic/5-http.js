// 5-http.js

const http = require('http');
const fs = require('fs').promises;

// Fonction pour compter les étudiants
async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);

    const fields = {};
    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    let result = `Number of students: ${students.length}\n`;
    for (const [field, list] of Object.entries(fields)) {
      result += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
    }
    return result;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

// Créer le serveur HTTP
const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    try {
      const databasePath = process.argv[2]; // Chemin de la base de données passé en argument
      if (!databasePath) {
        throw new Error('Database path is required');
      }

      const studentsInfo = await countStudents(databasePath);
      res.end(`This is the list of our students\n${studentsInfo}`);
    } catch (error) {
      res.end(`This is the list of our students\n${error.message}`);
    }
  } else {
    res.end('Not found');
  }
});

// Faire écouter le serveur sur le port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Exporter le serveur
module.exports = app;
