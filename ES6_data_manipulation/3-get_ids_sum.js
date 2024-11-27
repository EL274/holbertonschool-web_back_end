export default function getStudentIdsSum(list) {
    return list.reduce((a, l) => a + l.id, 0);
  }
