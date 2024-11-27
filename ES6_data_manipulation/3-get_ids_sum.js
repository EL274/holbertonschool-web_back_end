export default function getStudentIdsSum(list) {
    return list.reduce((accumulator, list) => accumulator + student.id, 0);
  }
