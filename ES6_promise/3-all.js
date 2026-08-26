import { uploadPhoto, createUser } from './utils.js';

export default function handleProfileSignup() {
    return Promise.all([uploadPhoto(), createUser()])
      .then(([uploadPhoto, user]) => {
        console.log(uploadPhoto.body, user.firstName, user.lastName);
      })
      .catch(() => {
        console.log('Signup system offline');
      });
}
