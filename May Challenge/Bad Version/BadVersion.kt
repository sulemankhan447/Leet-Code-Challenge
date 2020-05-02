/*
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3316/
*/
class BadVersion: VersionControl() {
    override fun firstBadVersion(n: Int) : Int {
    
        var low = 1
        var high = n
        while(low<high){
            val mid = low+((high-low)/2)
            if(isBadVersion(mid)){
                high=mid                
            }
            else{

                low = mid +1
            }
        }
        return low
        
	}
}

