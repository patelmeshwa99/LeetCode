class Solution {
    public boolean backspaceCompare(String s, String t) {
        return processString(s).equals(processString(t));
    }

    private Stack<Character> processString(String str) {
        Stack<Character> charStack = new Stack<>();
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) != '#') {
                charStack.push(str.charAt(i));
            } else {
                if (i != 0 && !charStack.isEmpty()) {
                    charStack.pop();
                }
            }
        }
        return charStack;
    }

}