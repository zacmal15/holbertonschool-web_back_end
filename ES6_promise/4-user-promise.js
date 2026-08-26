export default function signupUser(firstName, lastName) {
    return Promise.resolve({
        firstName,
        lastName,
    });
}
