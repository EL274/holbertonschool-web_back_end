export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const result = mathFunction();
    if (result instanceof Promise) {
      return result.then((value) => {
        queue.push(value);
        queue.push('Guardrail was processed');
        return queue;
      }).catch((error) => {
        queue.push(error.message);
        queue.push('Guardrail was processed');
        return queue;
      });
    }
    queue.push(result);
  } catch (error) {
    queue.push(error.message);
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
}
