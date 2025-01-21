// Afficher le message de bienvenue
console.log("Welcome to Holberton School, what is your name?");

// Configurer stdin pour lire l'entrée de l'utilisateur
process.stdin.setEncoding('utf8');

// Lire l'entrée de l'utilisateur
process.stdin.on('data', (input) => {
  // Supprimer les espaces blancs inutiles (comme le saut de ligne)
  const name = input.trim();

  // Afficher le nom de l'utilisateur
  console.log(`Your name is: ${name}`);

  // Fermer le programme proprement
  process.exit();
});

// Gérer la fin du flux stdin (Ctrl+D)
process.stdin.on('end', () => {
  console.log("This important software is now closing");
});
