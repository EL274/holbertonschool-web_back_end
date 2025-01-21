// 7-http_express.js

const express = require('express');
const fs = require('fs').promises;

// Créer une instance d'Express
const app = express();

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

// Définir la route pour l'endpoint "/"
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Définir la route pour l'endpoint "/students"
app.get('/students', async (req, res) => {
  try {
    const databasePath = process.argv[2]; // Chemin de la base de données passé en argument
    if (!databasePath) {
      throw new Error('Database path is required');
    }

    const studentsInfo = await countStudents(databasePath);
    res.send(`This is the list of our students\n${studentsInfo}`);
  } catch (error) {
    res.send(`This is the list of our students\n${error.message}`);
  }
});

// Faire écouter le serveur sur le port 1245
app.listen(1245, () => {
  console.log('Server is listening on port 1245');
});

// Exporter l'application
module.exports = app; 
