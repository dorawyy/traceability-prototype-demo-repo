export const sanitizeArgs = (args: unknown[]): unknown[] => {
  return args.map(arg => sanitizeInput(String(arg)));
};

// arbitrary change for testing
// another change

export const sanitizeInput = (input: string): string => {
  if (/[\r\n]/.test(input)) {
    throw new Error('CRLF injection attempt detected');
  }
  return input;
};
