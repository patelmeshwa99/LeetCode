class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet uniqueCharacters = findUniqueCharacters(s);
        for(int j=uniqueCharacters.size(); j>=0; j--){
            for(int i=0; i<=s.length()-j; i++){
                if(findUniqueCharacters(s.substring(i, i+j)).size() == j){
                    return j;
                }
            }   
        }
        return 0;
        
    }
    
    public HashSet<Character> findUniqueCharacters(String s) {
        HashSet uniqueCharacters = new HashSet<Character>();
        for(int i=0; i<s.length(); i++){
            uniqueCharacters.add(s.charAt(i));
        }
        return uniqueCharacters;
    }
    
}