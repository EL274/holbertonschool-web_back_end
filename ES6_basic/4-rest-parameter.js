/**
 * Retourne le nombre d'arguments passés à la fonction.
 * 
 * @param {...*} args - Les arguments passés à la fonction (paramètre rest).
 * @return {number} Le nombre d'arguments passés.
 */
export default function returnHowManyArguments(...args) {
    // Retourne la longueur du tableau args, qui correspond au nombre d'arguments
    return args.length;
}
