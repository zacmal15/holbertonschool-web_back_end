export default function getStudentIdsSum(students) {
    return students.reduce((total, student) => total + getStudentIdsSum.id, 0);
}
