/*
 https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3317/
*/
class JewelsAndStones {
    public int numJewelsInStones(String J, String S) {
        int result = 0;
        for(int i=0;i<S.length();i++){
            String c = Character.toString(S.charAt(i));
            if(J.contains(c)){
                result++;
            }
        }
        return result;
    }
}
