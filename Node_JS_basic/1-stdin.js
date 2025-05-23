//1-stdin.js

// Affiche le message de bienvenue dans la sortie standard (STDOUT)
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Écoute l'événement 'readable' sur l'entrée standard (STDIN)
// Cela se déclenche quand l'utilisateur entre quelque chose
process.stdin.on('readable', () => {
  // Lit les données entrées par l'utilisateur
  const name = process.stdin.read();
  
  // Si l'utilisateur a entré quelque chose (name n'est pas null)
  if (name) {
    // Affiche le nom dans la sortie standard
    process.stdout.write(`Your name is: ${name}`);
  }
});

// Écoute l'événement 'end' qui se déclenche quand l'utilisateur ferme le programme
// (par exemple en appuyant sur CTRL+D)
process.stdin.on('end', () => {
  // Affiche le message de fermeture
  process.stdout.write('This important software is now closing\n');
});
