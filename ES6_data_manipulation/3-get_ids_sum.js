export default function getStudentIdsSum(list) {
    return list.reduce((accumulator, list) => accumulator + list.id, 0);
  }
