function onSuccess(googleUser) {
  console.log('Logged in as: ' + googleUser.getBasicProfile().getName());
  var profile = googleUser.getBasicProfile();
  console.log('Email: ' + profile.getEmail());
  var main_block = document.getElementById('homeblock');
  main_block.style.display = 'none';
  var signout_button = document.getElementById('signout');
  signout_button.style.visibility = 'visible';
  var name = profile.getName();
  var account_button = document.getElementById('account');
  account_button.style.visibility = 'visible';
  account_button.innerHTML = name;
  var upload_block = document.getElementById('upload_block')
  upload_block.style.display = 'block';
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
    window.location = '/';
  });
}

