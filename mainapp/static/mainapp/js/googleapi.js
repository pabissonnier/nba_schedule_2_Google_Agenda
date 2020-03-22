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
  // The ID token you need to pass to your backend:
  var id_token = googleUser.getAuthResponse().id_token;
  console.log("ID Token: " + id_token);
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
  // Useful data for your client-side scripts:
  var profile = googleUser.getBasicProfile();
  console.log("ID: " + profile.getId()); // Don't send this directly to your server!
  console.log('Full Name: ' + profile.getName());
  console.log('Given Name: ' + profile.getGivenName());
  console.log('Family Name: ' + profile.getFamilyName());
  console.log("Image URL: " + profile.getImageUrl());
  console.log("Email: " + profile.getEmail());

  // The ID token you need to pass to your backend:
  var id_token = googleUser.getAuthResponse().id_token;
  console.log("ID Token: " + id_token);
}

function signOut() {
  var auth2 = gapi.auth2.getAuthInstance();
  auth2.signOut().then(function () {
    window.location.assign( '/');
  });
}

