function getCurrentYear() {
    const date = new Date();
    return date.getFullYear();
  }
  
  export default function getBudgetForCurrentYear(income, gdp, capita) {
    // Utilisation des noms de propriétés calculés directement dans la déclaration de l'objet
    return {
      [`income-${getCurrentYear()}`]: income,
      [`gdp-${getCurrentYear()}`]: gdp,
      [`capita-${getCurrentYear()}`]: capita
    };
  }
