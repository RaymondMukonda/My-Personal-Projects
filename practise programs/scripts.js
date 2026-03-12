let userRole = "editor";

switch (userRole) {
  case "admin":
    console.log("Access granted: Full control");
    break;
  case "editor":
    console.log("Access granted: Can edit content");
    break;
  case "viewer":
    console.log("Access granted: Read-only mode");
    break;
  default:
    console.log("Access denied: Unknown role");
}