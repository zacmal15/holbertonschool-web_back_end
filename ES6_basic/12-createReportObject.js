export default function createReportObject(employeeList) {
    return {
        allEmployees: {
            ...employeeList,
        },
        getNumberOfDepartments(employeeList) {
            return Object.keys(employeeList).length;
        },
    };
}
