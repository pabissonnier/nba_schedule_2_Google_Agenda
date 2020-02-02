function onSuccess(googleUser) {
  console.log('Logged in as: ' + googleUser.getBasicProfile().getName());
  var profile = googleUser.getBasicProfile();
  console.log('Email: ' + profile.getEmail());
  document.getElementById('signinbutton').style.visibility = 'none';
  window.location = '/upload';
}
function onFailure(error) {
console.log(error);
}
function renderButton() {
gapi.signin2.render('my-signin2', {
'scope': 'profile email',
'width': 650,
'height': 70,
'longtitle': true,
'theme': 'dark',
'onsuccess': onSuccess,
'onfailure': onFailure
});
}

function onSignIn(googleUser) {
  var signin_button = document.getElementById('my-signin2');
  var signout_button = document.getElementById('signout');
  signin_button.style.visibility = 'none';
  var profile = googleUser.getBasicProfile();
  console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  console.log('Name: ' + profile.getName());
  console.log('Image URL: ' + profile.getImageUrl());
   // This is null if the 'email' scope is not present.

}

function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut().then(function () {
    window.location = '/';
  });
}

