async function selectRole() {
  const role = document.getElementById('role-select').value;
  // Call Python function with role
  await eel.create_user(role)();
  // Open respective window
  await eel.open_window(role)();
}
