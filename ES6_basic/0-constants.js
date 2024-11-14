// Fonction taskFirst utilisant 'const'
export function taskFirst() {
    // Utilisation de 'const' car la valeur de 'task' ne change pas
    const task = 'I prefer const when I can.';
    return task;
  }
  
  // Fonction getLast reste inchangée
  export function getLast() {
    return ' is okay';
  }
  
  // Fonction taskNext utilisant 'let'
  export function taskNext() {
    // Utilisation de 'let' car 'combination' sera modifiée
    let combination = 'But sometimes let';
    
    // Modification de 'combination' en ajoutant le résultat de getLast()
    combination += getLast();
  
    return combination;
  }

