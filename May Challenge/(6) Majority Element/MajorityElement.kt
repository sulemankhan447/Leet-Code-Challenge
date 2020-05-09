/*
URL = https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3321/
*/
fun main() {
    //TODO Can Change Input Values For Testing
    val values: IntArray = intArrayOf(2, 2, 1, 1, 1, 2, 2, 2, 3)
    println(majorityElement(values))

}

fun majorityElement(nums: IntArray): Int {
    var majorityElementKey = 0
    var majorityElementValue = 0
    val count = HashMap<Int, Int>()
    // build hash map : character and how often it appears
    for (i in 0 until nums.size) {
        val c = nums[i]
        count[c] = count.getOrDefault(c, 0) + 1
    }
    val iterator = count.entries.iterator()
    while (iterator.hasNext()) {
        val pair = iterator.next()
        val key = pair.key
        val value = pair.value
        if (value > majorityElementValue) {
            majorityElementValue = value
            majorityElementKey = key
        }
    }

    return majorityElementKey

}
