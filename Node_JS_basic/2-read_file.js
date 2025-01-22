// 2-read_file.js

const fs = require('fs');

function countStudents(path) {
  try {
    // Lire le fichier de manière synchrone
    const data = fs.readFileSync(path, 'utf8');

    // Diviser les lignes du fichier
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Supprimer la première ligne (en-tête)
    const students = lines.slice(1);

    // Objet pour stocker les étudiants par domaine
    const fields = {};

    // Parcourir chaque ligne d'étudiant
    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');

      // Vérifier si le domaine existe déjà dans l'objet
      if (!fields[field]) {
        fields[field] = [];
      }

      // Ajouter l'étudiant au domaine correspondant
      fields[field].push(firstname);
    });

    // Afficher le nombre total d'étudiants
    console.log(`Number of students: ${students.length}`);

    // Afficher le nombre d'étudiants par domaine et leurs noms
    for (const [field, list] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
    }
  } catch (error) {
    // Gérer l'erreur si le fichier n'est pas disponible
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
