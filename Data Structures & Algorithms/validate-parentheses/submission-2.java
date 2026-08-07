class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> cache = new HashMap<>(Map.of(
            ')','(',
            ']','[',
            '}','{'
            ));
        
        for (char c : s.toCharArray()){
            if(cache.containsKey(c)){
                if(!stack.isEmpty() && stack.peek() == cache.get(c)){
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();

    }
}
