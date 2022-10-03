import java.util.*;

class Solution {   
    
    private boolean toBePushed(Character c) {
        if (Character.compare(c, '(') == 0 || Character.compare(c, '[') == 0 || Character.compare(c, '{') == 0) {
            return true;
        }
        return false;
    }
    
    private boolean toBePoped(Character c) {
        if (Character.compare(c, ')') == 0 || Character.compare(c, ']') == 0 || Character.compare(c, '}') == 0) {
            return true;
        }
        return false;  
    }
    
    private Character getOppositeBrace(Character c) {
        switch(c) {
            case ')':
                return '(';                
            case '}':
                return '{';                  
            case ']':
                return '[';
        }
        return '(';
    }
    
    public boolean isValid(String s) {
        Stack<Character> braces = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            
            if (toBePushed(s.charAt(i))) {
                braces.push(s.charAt(i));
                continue;   
            } 
            if (toBePoped(s.charAt(i))) {
                if (braces.isEmpty() || Character.compare(braces.peek(), getOppositeBrace(s.charAt(i))) != 0) {
                    return false;
                }
                else {
                    braces.pop();
                }
                continue;
            }
        }
        return braces.isEmpty();
    }
}