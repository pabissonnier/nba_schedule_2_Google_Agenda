function onSuccess(googleUser) {
  console.log('Logged in as: ' + googleUser.getBasicProfile().getName());
  var profile = googleUser.getBasicProfile();
  console.log('Email: ' + profile.getEmail());
  var signout_button = document.getElementById('signout');
  signout_button.style.visibility = 'visible';
  var name = profile.getGivenName();
  var upload_button = document.getElementById('upload_button');
  upload_button.style.visibility = 'visible';
  var account_button = document.getElementById('account');
  account_button.style.visibility = 'visible';
  account_button.innerHTML = name;
  var google_button_block = document.getElementById('google_button_block');
  google_button_block.style.visibility = 'hidden';
}

function onFailure(error) {
console.log(error); // add error message visible
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
  var profile = googleUser.getBasicProfile();
  console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  console.log('Name: ' + profile.getName());
  console.log('Image URL: ' + profile.getImageUrl());
   // This is null if the 'email' scope is not present.

}

function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut().then(function () {
    window.location.assign( '/');
  });
}

