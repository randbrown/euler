package euler27;

public class Euler27 {

    public static void main(String[] args) {
        int start = -1000;
        int end = 1000;

        int numConsecPrimes = 0;
        int aMax = -1;
        int bMax = -1;

        for (int a = start+1; a < end; a++) {
            for (int b = start; b <= end; b++) {
                int n = 0;
                while (isPrime(evalFunction(a, b, n))) {

                    n = n + 1;
                    if (n > numConsecPrimes) {
                        numConsecPrimes = n;
                        aMax = a;
                        bMax = b;
                    }
                }
            }
        }

        System.out.format("Max a=%d, Max b=%d, Product = %d%n", aMax, bMax, aMax * bMax);
    }

    private static int evalFunction(Integer a, Integer b, Integer n) {
        return n * n + a * n + b;
    }

    private static boolean isPrime(Integer n) {
        n = Math.abs(n);
        int lim = (int)Math.sqrt(n / 2);
        for (int idx = 2; idx < lim; idx++) {
            if (n % idx == 0) {
                return false;
            }
        }
        return true;
    }
}
