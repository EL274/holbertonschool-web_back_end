import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(req, res) {
    const databasePath = process.argv[2];
    readDatabase(databasePath)
      .then((fields) => {
        let response = 'This is the list of our students\n';
        for (const [field, students] of Object.entries(fields)) {
          response += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
        }
        res.status(200).send(response.trim());
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    const databasePath = process.argv[2];
    readDatabase(databasePath)
      .then((fields) => {
        const students = fields[major] || [];
        res.status(200).send(`List: ${students.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}
