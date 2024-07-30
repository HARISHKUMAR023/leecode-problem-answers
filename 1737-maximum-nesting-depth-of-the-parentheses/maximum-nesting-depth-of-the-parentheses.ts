function maxDepth(s: string): number {
     let maxDepth = 0;
        let currentDepth = 0;

        for (const char of s) {
            if (char === '(') {
                currentDepth++;
                maxDepth = Math.max(maxDepth, currentDepth);
            } else if (char === ')') {
                currentDepth--;
            }
        }

        return maxDepth;
};