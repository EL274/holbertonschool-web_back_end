export default function appendToEachArrayValue(array, appendString) {
    // Utilisation de 'for...of' pour itérer directement sur les valeurs du tableau
    for (let value of array) {
      // Mise à jour de la valeur dans le tableau
      // L'index de 'value' dans 'array' est trouvé avec indexOf
      array[array.indexOf(value)] = appendString + value;
    }
  
    return array;
  }
